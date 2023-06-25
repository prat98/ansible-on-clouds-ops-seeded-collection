# AAP on AWS Extension Nodes Playbooks

## About

These playbooks simplify the deployment and management of the extension nodes on AAP on AWS.

## Getting Started 

These playbooks require an active AAP on AWS foundation stack to be running. The instructions below guide how to add the credential, project, and templates required. Once added, they can be launched to add or remove the extension nodes.

1. In the AAP Controller, add the AoC Cloud EE execution environment
    1. Nav bar: Resources -> Execution Environments
    2. Click `Add`
    3. Name: `AoC Cloud EE`
    4. Image: `quay.io/scottharwell/cloud-ee:latest`
    5. Pull: `Always`
    6. Click `Save`
2. In the AAP Controller UUI, add your GitHub credentials
    1. Nav bar: Resources -> Credentials
    2. Click `Add`
    3. Enter credential name
    4. For **Credential Type** select `Source Control`
    5. Fill in your GitHub private key
    6. Click `Save`
3. In the AAP Controller UI, add your AWS credentials.
    1. Nav bar: Resources -> Credentials
    2. Click `Add`
    3. Enter credential name
    4. For **Credential Type** select `Amazon Web Services`
    5. Fill in AWS creds
    6. Click `Save`
4. Add this project
    1. Nav bar: Resources -> Projects
    2. Click `Add`
    3. Project Name: `AoC Playbooks`
    4. For  **Source Control Type** select `Git`
    5. Paste `git@github.com:ansible/aap-aoc-collections.git` in **Source Control URL**
    6. For **Source Control Branch/Tag/Commit**, enter `main` or a development branch name
    7. Select your **Source Control Credential** created earlier
    8. Click `Save`
5. Add the template - Add Extension Nodes
    1. Nav bar: Resources -> Templates
    2. Click: Add -> Add job template
    3. Name: `Add Extension Nodes`
    4. Project: `AoC Playbooks` or alternate name
    5. Execution Environment: `AoC Cloud EE`
    6. Playbook: `playbooks/aws_add_extension_nodes.yml`
    7. Credentials:
        1. Select Category - `Amazon Web Services`
        2. Select your AWS Creds
    8. Variables -
        ```
        ---
        aws_foundation_stack_name: ""                       # Name of your foundation stack
        aws_region: us-east-1                               # AWS region of foundation stack
        aws_offer_type:                                     # Must be 100, 200, or 400
        aws_ami_id: ""                                      # AMI ID of extension node offering
        aws_launch_template_name: extension-group-template  # EC2 Launch template name
        aws_autoscaling_group_name: extension-group-asg     # Autoscaling group name
        aws_asg_min_size: 1                                 # ASG minimum size
        aws_asg_desired_capacity: 1                         # ASG desired capacity
        ```
    9. Click `Save`
6. Add the template - Remove Extension Nodes
    1. Nav bar: Resources -> Templates
    2. Click: Add -> Add job template
    3. Name: `Remove Extension Nodes`
    4. Project: `AoC Playbooks` or alternate name
    5. Execution Environment: `AoC Cloud EE`
    6. Playbook: `playbooks/aws_remove_extension_nodes.yml`
    7. Credentials:
        1. Select Category - `Amazon Web Services`
        2. Select your AWS Creds
    8. Variables -
        ```
        ---
        aws_foundation_stack_name: ""                       # Name of your foundation stack
        aws_region: us-east-1                               # AWS region of foundation stack
        aws_launch_template_name: extension-group-template  # EC2 Launch template name
        aws_autoscaling_group_name: extension-group-asg     # Autoscaling group name
        ```
    9. Click `Save`
 
## Running using Ansible Navigator

To run these playbooks locally using ansible navigator, the following commands can be used as well. Be sure to set your AWS credentials via the environment variables below before running.

### Running Add Extension Nodes playbook

```bash
ansible-navigator run playbooks/aws_add_extension_nodes.yml  --set-environment-variable AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -m stdout --playbook-artifact-enable false --execution-environment-image quay.io/scottharwell/cloud-ee:latest
```

### Running Remove Extension Nodes playbook
```bash
ansible-navigator run playbooks/aws_remove_extension_nodes.yml --set-environment-variable AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -m stdout --playbook-artifact-enable false --execution-environment-image quay.io/scottharwell/cloud-ee:latest
```

