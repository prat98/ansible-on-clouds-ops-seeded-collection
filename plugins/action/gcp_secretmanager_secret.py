#!/usr/bin/env python
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Running on Mac: Run: `export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` as desribe in
# https://lucaberton.it/blog/why-ansible-and-python-fork-break-on-macos-high-sierra-and-how-to-solve/

# Make coding more python3-ish, this is required for contributions to Ansible
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.plugins.action import ActionBase
from ansible.config.manager import ensure_type
from ansible.module_utils.six import string_types
from ansible.errors import AnsibleActionFail, AnsibleError

try:
    # Import the Secret Manager client library.
    from google.cloud import secretmanager
except ImportError as imp_exc:
    GOOGLE_CLOUD_IMPORT_ERROR = imp_exc
else:
    GOOGLE_CLOUD_IMPORT_ERROR = None


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if GOOGLE_CLOUD_IMPORT_ERROR:
            raise AnsibleError("google.cloud must be installed to use this plugin")

        super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Options type validation
        # stings
        for s_type in ("project", "secret"):
            if s_type in self._task.args:
                value = ensure_type(self._task.args[s_type], "string")
                if value is not None and not isinstance(value, string_types):
                    raise AnsibleActionFail(
                        "%s is expected to be a string, but got %s instead"
                        % (s_type, type(value))
                    )
                self._task.args[s_type] = value

        # GCP project in which to store secrets in Secret Manager.
        project_id = self._task.args.get("project", None)

        # ID of the secret to create.
        secret_id = self._task.args.get("secret", None)

        version = self._task.args.get("version", None)
        if version is None:
            version = "latest"

        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()

        # Access the secret version.
        try:
            resource_name = "projects/%s/secrets/%s/versions/%s" % (
                project_id,
                secret_id,
                version,
            )
            # resource_name = f"projects/{project_id}/secrets/{secret_id}/versions/{version}"
            response = client.access_secret_version(request={"name": resource_name})
        except Exception as e:
            raise AnsibleActionFail(
                "secret %s with version %s not found in project %s"
                % (secret_id, version, project_id)
            )
        payload = response.payload.data.decode("UTF-8")
        ret = dict()
        ret["secret"] = payload

        return dict(ansible_facts=dict(ret))
