# AAP on AWS Generate Inventory

## Requirements

[amazon.aws.aws_ec2 requirements](https://docs.ansible.com/ansible/latest/collections/amazon/aws/aws_ec2_inventory.html#requirements)

## Generate Inventory

```bash
export AWS_ACCESS_KEY_ID=<ACCESS_KEY>
export AWS_SECRET_ACCESS_KEY=<SECRET>

# Generate the inventory. Replace <deployment_name> with your deployment name
# A inventory file specified by the output parameter will be generated
# By default the output file will be <deployment_name>-[regions].gcp.yaml in the ansible working directory (playbooks)
ansible-playbook redhat.ansible_on_clouds.aws_deployment_inventory --extra-vars="aws_foundation_stack_name=<deployment_name> regions=[<region1>,<region2>,...] output=<file-name>"

# You can verify the generated inventory by running
export ANSIBLE_CONFIG=aws-ansible.cfg
ansible-inventory -i <file-name>.aws_ec2.yaml --graph
```

## How to use with aws_ssm connection

[aws_ssm requirements](https://docs.ansible.com/ansible/latest/collections/community/aws/aws_ssm_connection.html#requirements)

To install `aws session manager plugin` follow instructions: [ssm plugin install](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)

Here an example on how to use it:

```yaml
- name: Get hostnames
  hosts: aap_deployment # Name of the group defined in the inventory
  connection: aws_ssm

  vars:
    # A bucket is needed
    ansible_aws_ssm_bucket_name: <bucket_name>
    ansible_aws_ssm_region: <bucket_region>

  tasks:
  - name: get hostname
    ansible.builtin.command:
      cmd: "hostname"
    register: hostname

  - name: Show hostname
    ansible.builtin.debug:
      msg:
        - "hostname: {{ hostname.stdout_lines }}"

```
and launch it with

```bash
ansible-playbook <the_playbook> -i <generated_inventory>
```

## Troubleshoot

### Timeout or UNREACHABLE
if you get timeout or UNREACHABLE try to setup the env var:
```bash
export ANSIBLE_PERSISTENT_COMMAND_TIMEOUT=30
export ANSIBLE_SSH_RETRIES=2
```

### Extension not part of the inventory

Check if the tag `aap:cloudformation:main-stack-name` is present on the extension node and its value is the name of the deployment.
