#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Red Hat | Ansible
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: aws_deployment_info

short_description: Returns the AoC AWS deployment information.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "0.0.1"

description: Returns the AoC AWS deployment information. It includes data from the AWS CloudFormation stack outputs and the load balancer components.

options:
  foundation_stack_name:
    description: The name of the foundation stack deployment.
    required: true
    type: str

# There's many possible ways to authenticate with AWS, so maybe wouldn't make
# sense to enforce a specific authentication method via a documentation fragment.
# extends_documentation_fragment:
#   - aap.aoc.aws_auth

author:
  - Luiz Costa (@thenets)
"""

EXAMPLES = r"""
# Pass in a message
- name: Test with a message
  aap.aoc.aws_deployment_info:
    foundation_stack_name: my_deployment
"""

RETURN = r"""
foundation_stack_name:
  description: The foundation stack deployment name.
  type: str
  returned: always
  sample: 'my_deployment'
stack_outputs:
  description: The AWS CloudFormation stack outputs. The key is the CloudFormation 'output.ExportName'.
  type: dict
  returned: always
status:
    description: The AWS CloudFormation health check status. [healthy, unhealthy]
    type: str
    returned: always
    sample: 'healthy'
health_check:
  description: The AWS load balancer health check.
  type: dict
  returned: always
  sample:
    {
      "automation-controller": "HTTP:80/health",
      "automation-hub": "HTTP:80/health"
    }
"""

from ansible.module_utils.basic import AnsibleModule

try:
    import boto3
except ImportError as imp_exc:
    BOTO_3_IMPORT_ERROR = imp_exc
else:
    BOTO_3_IMPORT_ERROR = None


def _cloudformation_stack_outputs(stack_name, region):
    """Create a dict where 'output.ExportName' is the key and everything else is the value"""

    def _cloudformation_stack(stack_name):
        client = boto3.client("cloudformation", region_name=region)
        response = client.describe_stacks(StackName=stack_name)
        return response["Stacks"][0]

    data = {}
    for output in _cloudformation_stack(stack_name)["Outputs"]:
        data[output["ExportName"]] = {
            "description": output["Description"],
            "value": output["OutputValue"],
            "key": output["OutputKey"],
        }
    return data


def _get_target_group_arn_list(load_balancer_name, region):
    """Retrieve the target group ARNs from the load balancer.

    Returns:
        list<str>: A list of target group ARNs.
    """
    client = boto3.client("elbv2", region_name=region)
    response = client.describe_target_groups(LoadBalancerArn=load_balancer_name)
    # Must return the list of target group ARNs
    target_group_arn_list = []
    for target_group in response["TargetGroups"]:
        target_group_arn_list.append(target_group["TargetGroupArn"])
    return target_group_arn_list


def _get_health_check_by_load_balancer_name(load_balancer_name, region):
    """Retrieve the health check from the load balancer target group.

    Returns:
        list<dict>: A list of dictionaries. Each dictionary is a target group health check.
    """
    target_group_arn_list = _get_target_group_arn_list(load_balancer_name, region)
    list_formated_health_check = []

    for target_group_arn in target_group_arn_list:
        # Retrieve the health check from the target group
        client = boto3.client("elbv2", region_name=region)
        response = client.describe_target_health(TargetGroupArn=target_group_arn)

        formated_health_check = {
            "target_group_arn": target_group_arn,
            "last_checked": response["ResponseMetadata"]["HTTPHeaders"]["date"],
            "status_code": response["ResponseMetadata"]["HTTPStatusCode"],
            "status": response["TargetHealthDescriptions"][0]["TargetHealth"]["State"]
            # DEBUG - Uncomment the line below to see the full response
            # "all": response
        }

        list_formated_health_check.append(formated_health_check)

    return list_formated_health_check


def _stack_health_check(stack_outputs, region):
    """
    The stack health check function takes the outputs from the stacks and retrieves the load balancer names from the
    stack outputs. It then performs a health check against the load balancers and returns the results.

    If all load balancers are healthy, the deployment is healthy.

    Output schema:
    {
        "status": [healthy, unhealthy],
        "health_check": {
            <load_balancer_name>: <target_group_health_check>,
        }
    }
    """
    load_balancer_sufixes = [
        "-aap-hub-alb",
        "-aap-controller-alb",
        "-aap-hub-nlb",
        "-aap-controller-nlb",
    ]

    # Retrieve the load balancer names from the stack outputs
    load_balancer_names = []
    for key in stack_outputs:
        for sufix in load_balancer_sufixes:
            if key.endswith(sufix):
                load_balancer_names.append(stack_outputs[key]["value"])

    load_balancer_health_checks = {}
    for load_balancer_name in load_balancer_names:
        load_balancer_health_checks[
            load_balancer_name
        ] = _get_health_check_by_load_balancer_name(load_balancer_name, region)

    data = {}
    # If all load balancers are healthy, the deployment is healthy
    data["status"] = "healthy"
    for load_balancer_name in load_balancer_names:
        for health_check in load_balancer_health_checks[load_balancer_name]:
            if health_check["status"] != "healthy":
                data["status"] = "unhealthy"
                break

    data["load_balancers"] = load_balancer_health_checks

    return data


def _get_foundation_autoscaling_groups(cloudformation_stack_name, region):
    """Retrieve the autoscaling groups based on the CloudFormation stack name.
    1. List all resources in the CloudFormation stack
    2. Filter the resources to only autoscaling groups
    3. Retrieve the autoscaling group names from the resources

    Args:
        cloudformation_stack_name (str): The name of the CloudFormation stack.

    Returns:
        list<str>: A list of autoscaling group names.
    """
    client = boto3.client("cloudformation", region_name=region)
    response = client.list_stack_resources(StackName=cloudformation_stack_name)

    # Filter the resources to only autoscaling groups
    autoscaling_groups = []
    for resource in response["StackResourceSummaries"]:
        if resource["ResourceType"] == "AWS::AutoScaling::AutoScalingGroup":
            autoscaling_groups.append(resource)

    # Retrieve the autoscaling group names from the resources
    autoscaling_group_names = []
    for autoscaling_group in autoscaling_groups:
        autoscaling_group_names.append(autoscaling_group["PhysicalResourceId"])

    return autoscaling_group_names


def _get_extension_autoscaling_groups(cloudformation_stack_name, region):
    """Retrieve the autoscaling groups based on the CloudFormation stack name.
    1. List all resources in the CloudFormation stack
    2. Filter the resources to only autoscaling groups
    3. Retrieve the autoscaling group names from the resources
    Args:
        cloudformation_stack_name (str): The name of the CloudFormation stack.
    Returns:
        list<str>: A list of autoscaling group names.
    """

    client = boto3.client('autoscaling', region_name=region)
    paginator = client.get_paginator('describe_auto_scaling_groups')
    page_iterator = paginator.paginate(
        PaginationConfig={'PageSize': 100}
    )

    filtered_asgs = page_iterator.search(
        'AutoScalingGroups[] | [?contains(Tags[?Key==`{0}`].Value, `{1}`)]'.format(
            'aap:cloudformation:main-stack-name', cloudformation_stack_name)
    )

    autoscaling_group_names = []
    for asg in filtered_asgs:
        autoscaling_group_names.append(asg['AutoScalingGroupName'])

    return autoscaling_group_names


def run_module():
    # Define the module's arguments
    argument_spec = dict(foundation_stack_name=dict(type="str", required=True))

    # Define the initial result
    result = {
        "changed": False,
        "stack_outputs": {},
        "status": "unhealthy",
        "load_balancers": {},
        "autoscaling_groups": {},
        "region": "",
    }

    # Instantiate the module
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    if BOTO_3_IMPORT_ERROR:
        module.fail_json(
            msg="Failed to import boto3. Please install it. $ pip install boto3",
            exception=BOTO_3_IMPORT_ERROR.msg,
            **result
        )

    # Try to retrieve the current region
    try:
        client = boto3.client("s3")  # example client, could be any
        result["region"] = client.meta.region_name
    except Exception as e:
        module.fail_json(
            msg="Failed to retrieve the current region", exception=str(e), **result
        )

    # Try to retrieve the foundation autoscaling groups
    try:
        result["autoscaling_groups"]["foundation"] = _get_foundation_autoscaling_groups(
            module.params["foundation_stack_name"], result["region"]
        )
    except Exception as e:
        module.fail_json(
            msg="Failed to retrieve the autoscaling groups", exception=str(e), **result
        )
    # Try to retrieve the extension autoscaling groups
    try:
        result["autoscaling_groups"]["extension"] = _get_extension_autoscaling_groups(
            module.params["foundation_stack_name"], result["region"]
        )
    except Exception as e:
        module.fail_json(
            msg="Failed to retrieve the autoscaling groups", exception=str(e), **result
        )

    # Try to retrieve the AWS CloudFormation stack outputs
    try:
        result["stack_outputs"] = _cloudformation_stack_outputs(
            module.params["foundation_stack_name"], result["region"]
        )
    except Exception as e:
        module.fail_json(
            msg="Failed to retrieve the AWS CloudFormation stack outputs",
            exception=str(e),
            **result
        )

    # Try to retrieve the stack health check
    try:
        stack_health_check = _stack_health_check(result["stack_outputs"], result["region"])
        result["status"] = stack_health_check["status"]
        result["load_balancers"] = stack_health_check["load_balancers"]
    except Exception as e:
        module.fail_json(
            msg="Failed to retrieve the AWS load balancer health check",
            exception=str(e),
            **result
        )

    # Return the result
    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
