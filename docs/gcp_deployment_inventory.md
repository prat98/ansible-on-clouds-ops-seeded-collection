# AAP on GCP Generate inventory

## Requirements

[google.cloud.gcp_compute requirements](https://docs.ansible.com/ansible/latest/collections/google/cloud/gcp_compute_inventory.html#requirements)

## Generate Inventory

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credential

# Generate the inventory. Replace <deployment_name> with your deployment name
# A inventory file specified by the output parameter will be generated
# By default the output file will be <deployment_name>.gcp.yaml in the ansible working directory (playbooks)
ansible-playbook redhat.ansible_on_clouds.gcp_deployment_inventory --extra-vars="project=gc-ansible-cloud gcp_deployment_name=<deployment_name> output=<file-name>"

# You can verify the generated inventory by running
export ANSIBLE_CONFIG=gcp-ansible.cfg
ansible-inventory -i <file-name>.gcp.yaml --graph
```

## Troubleshoot

if you get timeout or UNREACHABLE try to setup the env var:
```bash
export ANSIBLE_PERSISTENT_COMMAND_TIMEOUT=30
export ANSIBLE_SSH_RETRIES=2
```
