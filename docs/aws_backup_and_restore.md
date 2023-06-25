# AAP on AWS Backup and Restore Playbooks

## About

These playbooks simplify the backup and restore of the AAP on AWS foundation stack.

These playbooks can be ran from the AAP Controller or using Ansible Navigator if restoring locally.

## Getting Started 

These playbooks require an active AAP on AWS foundation stack to be running. The instructions below guide how to add the credential, project, and templates required. Once added, they can be launched to backup and restore the stack.

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
5. Add the template - Backup AoC Stack
    1. Nav bar: Resources -> Templates
    2. Click: Add -> Add job template
    3. Name: `Backup AoC Stack`
    4. Project: `AoC Playbooks`
    5. Execution Environment: `AoC Cloud EE`
    6. Playbook: `playbooks/aws_backup_stack.yml`
    7. Credentials:
        1. Select Category - `Amazon Web Services`
        2. Select your AWS Creds
    8. Variables -
        ```
        ---
        aws_foundation_stack_name: ""                            # AAP foundation stack name
        aws_region: us-east-1                                    # AWS region
        aws_backup_vault_name: ""                                # AWS backup vault name. If left empty, EFS backup will be skipped. ex - aws/efs/automatic-backup-vault
        aws_backup_iam_role_arn: ""                              # AWS backup role name. Must be set if backing up EFS. ex - arn:aws:iam::<Account-ID>:role/service-role/AWSBackupDefaultServiceRole
        ```
    9. Click `Save`
6. Add the template - Restore AoC Stack
    1. Nav bar: Resources -> Templates
    2. Click: Add -> Add job template
    3. Name: `Restore AoC Stack`
    4. Project: `AoC Playbooks` or alternate name
    5. Execution Environment: `AoC Cloud EE`
    6. Playbook: `playbooks/aws_restore_stack.yml`
    7. Credentials:
        1. Select Category - `Amazon Web Services`
        2. Select your AWS Creds
    8. Variables -
        ```
        ---
        aws_foundation_stack_name: ""                            # AAP foundation stack name
        aws_restored_stack_name: ""                              # Stack name of restored AAP foundation created by playbook
        aws_region: us-east-1                                    # AWS region
        aws_backup_vault_name: ""                                # AWS backup vault name. ex - aws/efs/automatic-backup-vault
        aws_rds_db_snapshot_arn: ""                              # The ARN of the RDS snapshot to use when restoring the stack
        aws_backup_restore_point_arn: ""                         # The ARN of the EFS recovery point to use when restoring the stack
        aws_backup_iam_role_arn: ""                              # AWS backup role name. ex - arn:aws:iam::<Account-ID>:role/service-role/AWSBackupDefaultServiceRole
        aws_s3_bucket: ""                                        # AWS S3 bucket name. Used to upload cloudformation template
        ```
    9. Click `Save`
 
## Running using Ansible Navigator

To run these playbooks locally using ansible navigator, the following commands can be used as well. Be sure to set your AWS credentials via the environment variables below before running.

### Running Backup AoC Stack playbook

```bash
ansible-navigator run extension_nodes/playbooks/aws_backup_stack.yml --set-environment-variable AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -m stdout --playbook-artifact-enable false --execution-environment-image quay.io/scottharwell/cloud-ee:latest
```

### Running Remove Extension Nodes playbook
```bash
ansible-navigator run extension_nodes/playbooks/aws_restore_stack.yml --set-environment-variable AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -m stdout --playbook-artifact-enable false --execution-environment-image quay.io/scottharwell/cloud-ee:latest
```

