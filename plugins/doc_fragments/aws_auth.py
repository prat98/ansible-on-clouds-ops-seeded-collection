# -*- coding: utf-8 -*-

# Copyright: (c) 2023, Red Hat | Ansible
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Options for authenticating with the API.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
options:
  aws_access_key:
    description: AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID environment variable is used.
    type: str
  aws_secret_key:
    description: AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY environment variable is used.
    type: str
notes:
  - "For the authentication method, it's preferable to use the C(Ansible variables) instead of C(environment variables) to avoid exposing the credentials."
"""
