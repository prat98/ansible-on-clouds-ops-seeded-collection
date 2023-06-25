# Ansible Automation Platform for Ansible on Cloud collection - redhat.ansible_on_clouds
Miscellaneous playbooks for configuration and maintenance of Ansible Automation Platform deployments. The following cloud providers:
- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)

# Prerequisites
Every cloud provider requires certain prerequisites in order to gain access and be able to retrieve and manipulate data.  The following are the prerequisites for each cloud provider.

## Amazon Web Services (AWS)
- TODO

## Google Cloud Platform (GCP)
- `gcloud` command line interface must already be installed
- `gcloud` must already be authenticated ('logged in')
- Service account credentials JSON file downloaded and available for use

# To run playbooks from the cloned repo
During development you will want to test the playbooks in the collection easisly.  In order for the `ansible-playbooks` command to be able to find your collection of playbooks, use the following commands, from the base directory of the repo, to create a symbolic link from the ansible default collection path to your repo.
```bash
mkdir -p  ~/.ansible/collections/ansible_collections/redhat
ln -s $PWD ~/.ansible/collections/ansible_collections/redhat/ansible_on_clouds
```

Now you can run a playbook
```bash
ansible-playbook redhat.ansible_on_clouds.gcp_list_deployments -e gcp_service_account_credentials_json_path=/tmp/my_gcp_service_account_credentials.json
```

If you no longer need this symbolic link, simply run:
```bash
rm  ~/.ansible/collections/ansible_collections/redhat/ansible_on_clouds
```

# Playbooks

## logging and monitoring

```bash
cd playbooks
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credential
export ANSIBLE_CONFIG=gcp-ansible.cfg

# Generate the inventory. Replace <deployment_name> with your deployment name
# A inventory will be generated in
ansible-playbook gcp_deployment_inventory.yaml --extra-vars="deployment=<deployment_name>"

# You can verify the generated inventory by running
ansible-inventory -i <deployment-name>.gcp.yaml --graph

# Configure the vars/logging_monitoring_config.yaml

# Launch the playbook. Replace <deployment_name> with your deployment name
ansible-playbook setup_logging_metrics.yaml --extra-vars=@vars/logging_monitoring_config.yaml -i inventory/<deployment_name>.gcp.yaml
```

Possible issue if python not setup correctly: https://access.redhat.com/solutions/5674911

ssh the hub and run
```bash
alternatives  --config python #<== should be on /usr/bin/python3
alternatives  --config python3 #<== should be on /usr/bin/python3.6
```
# ansible-on-clouds-ops-seeded-collection
