#!/usr/bin/python
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Running on Mac: Run: `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` as desribe in
# https://lucaberton.it/blog/why-ansible-and-python-fork-break-on-macos-high-sierra-and-how-to-solve/

# Make coding more python3-ish, this is required for contributions to Ansible
from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "status": ["preview"],
    "supported_by": "community",
    "metadata_version": "2.14.1",
}

DOCUMENTATION = """
    module: gcp_secretmanager_secret
    short_description: retrieve a secret
    description:
        - This actions retrieve the last version value of secret
    author: Dominique Vernier. (@itdove)
    version_added: 2.3.0
    options:
      project:
          description: GCP project id
          type: str
          required: true
      secret:
          description: The secret name
          type: str
          required: true
      version:
          description: The secret version
          type: str
"""

EXAMPLES = """
# Retrieve a secret from a project

- name: Get secret
  hosts: localhost
  connection: local

  tasks:

  - name: Get secret
    redhat.ansible_on_clouds.gcp_secretmanager_secret:
      project: 'gc-ansible-cloud'
      secret: 'dvernier1-aap-admn'
    register: 'r'

  - name: Display results
    ansible.builtin.debug:
      msg: |
        "{{ r }}"

  - name: Get secret with version
    redhat.ansible_on_clouds.gcp_secretmanager_secret:
      project: 'gc-ansible-cloud'
      secret: 'dvernier1-aap-admn'
      version: '1'
    register: 'r'

  - name: Display results
    ansible.builtin.debug:
      msg: |
        "{{ r }}"
"""
