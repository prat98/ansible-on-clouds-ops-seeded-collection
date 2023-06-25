# AAP on GCP Setup logging monitoring

## Requirements

[google.cloud.gcp_compute requirements](https://docs.ansible.com/ansible/latest/collections/google/cloud/gcp_compute_inventory.html#requirements)

## run locally

Create a yaml like this for extra-vars

```yaml
components: # default values ["controller","hub"]
- "controller"
- "hub"
monitoring_enabled: false # default value false
logging_enabled: false # default value false
default_collector_interval: 59s # default value 59s
db_user: awx # default aws
```

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credential
export ANSIBLE_CONFIG=gcp-ansible.cfg

# Generate the inventory. Replace <deployment_name> with your deployment name
# A inventory file specified by the output parameter will be generated
# By default the output file will be <deployment_name>.gcp.yaml in the ansible working directory (playbooks)
ansible-playbook redhat.ansible_on_clouds.gcp_deployment_inventory --extra-vars="project=<project_id> deployment=<deployment_name> output=<file-name>"

# You can verify the generated inventory by running
ansible-inventory -i <file-name>.gcp.yaml --graph

# Launch the playbook. Replace <deployment_name> with your deployment name

# They can be overwritten with `--extra-vars`
# for example to enable monitoring
ansible-playbook redhat.ansible_on_clouds.gcp_setup_logging_monitoring --extra-vars="monitoring_enabled=true" -i <file-name>.gcp.yaml


```

## run in container

```bash
# Add a dir an extra vars files as above
# Create the inventory as above and put it in the same directory
# Put your ansible.cfg in the same directory
export IMAGE=quay.io/ansible-on-clouds/ansible-on-clouds-ops:latest
docker pull $IMAGE
docker run \
--env PLATFORM=GCP \
--env CLOUDSDK_CORE_PROJECT=gc-ansible-cloud \
--env GOOGLE_APPLICATION_CREDENTIALS=$GOOGLE_APPLICATION_CREDENTIALS \
--env ANSIBLE_CONFIG=/config/gcp-ansible.cfg \
-v <secrets_dir>:/secrets \
-v <your_config_dir>:/config:ro \
$IMAGE \
redhat.ansible_on_clouds.gcp_setup_logging_monitoring \
-e @/config/extra_vars.yaml -i /config/myinventory.gcp.yaml

# You can add any extra parameters for the playbook such as -vvv
```

## Troubleshoot

if you get timeout or UNREACHABLE try to setup the env var:
```bash
export ANSIBLE_PERSISTENT_COMMAND_TIMEOUT=30
export ANSIBLE_SSH_RETRIES=2
```