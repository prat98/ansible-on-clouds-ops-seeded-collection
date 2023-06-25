
:orphan:

.. _list_of_collection_env_vars:

Index of all Collection Environment Variables
=============================================

The following index documents all environment variables declared by plugins in collections.
Environment variables used by the ansible-core configuration are documented in :ref:`ansible_configuration_settings`.

.. envvar:: ANSIBLE_SSH_RETRIES

    Number of attempts to connect.

    Ansible retries connections only if it gets an SSH error with a return code of 255.

    Any errors with return codes other than 255 indicate an issue with program execution.

    *Used by:*
    :ref:`aap.aoc.gcp\_ssh connection plugin <ansible_collections.aap.aoc.gcp_ssh_connection>`
