#!/usr/bin/env python
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
    name: gcp_secretmanager_secret
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
      service_account_credentials:
          description: The path to the service account credentionals.
          type: str
      on_missing:
          description: Action to take if the secret is missing.
          type: str
          choices:
          - "error"
          - "warn"
          - "skip"
          default: "error"
"""

EXAMPLES = """
# Retrieve a secret from a project

- name: Get secret
  hosts: localhost
  connection: local

  tasks:

  - name: Lookup secret
    ansible.builtin.debug:
      msg: "{{ lookup('redhat.ansible_on_clouds.gcp_secretmanager_secret',project='my-gcp-project',secret='my-secret-name') }}"

  - name: Lookup secret with version
    ansible.builtin.debug:
      msg: "{{ lookup('redhat.ansible_on_clouds.gcp_secretmanager_secret',project='my-gcp-project',secret='my-secret-name',version='1') }}"

"""

from ansible.module_utils.six import string_types
from ansible.errors import AnsibleActionFail, AnsibleOptionsError, AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display
import os

display = Display()

try:
    # Import the Secret Manager client library.
    from google.cloud import secretmanager
except ImportError as imp_exc:
    GOOGLE_CLOUD_IMPORT_ERROR = imp_exc
else:
    GOOGLE_CLOUD_IMPORT_ERROR = None


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        if GOOGLE_CLOUD_IMPORT_ERROR:
            raise AnsibleError("google.cloud must be installed to use this plugin")

        # First of all populate options,
        # this will already take into account env vars and ini config
        self.set_options(var_options=variables, direct=kwargs)

        # GCP project in which to store secrets in Secret Manager.
        project_id = self.get_option("project")

        # ID of the secret to create.
        secret_id = self.get_option("secret")

        version = self.get_option("version")
        if version is None:
            version = "latest"

        on_missing = self.get_option("on_missing")
        if on_missing is None:
            on_missing = "error"

        service_account_credentials = self.get_option("service_account_credentials")
        if service_account_credentials is not None:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_credentials

        # Options type validation
        ret = []
        for term in terms:
            if not isinstance(term, string_types):
                raise AnsibleOptionsError(
                    'Invalid setting identifier, "%s" is not a string, its a %s'
                    % (term, type(term))
                )

        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()

        ret = []
        # Access the secret version.
        try:
            resource_name = "projects/%s/secrets/%s/versions/%s" % (
                project_id,
                secret_id,
                version,
            )
            response = client.access_secret_version(request={"name": resource_name})
        except Exception as e:
            if on_missing == "error":
                raise AnsibleActionFail(
                    "secret %s with version %s not found in project %s"
                    % (secret_id, version, project_id)
                )
            elif on_missing == "warn":
                display.warning("projects/%s/secrets/%s/versions/%s not found" % (project_id, secret_id, version))
                return ret
            elif on_missing == "skip":
                return ret

        payload = response.payload.data.decode("UTF-8")
        ret.append(payload.strip())

        return ret
