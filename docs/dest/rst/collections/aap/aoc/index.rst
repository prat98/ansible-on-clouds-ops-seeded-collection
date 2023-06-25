


.. _plugins_in_aap.aoc:

Aap.Aoc
=======

Collection version 0.0.1

.. contents::
   :local:
   :depth: 1

Description
-----------

Miscellaneous playbooks for configuration and maintenance of Ansible Automation Platform deployments

**Author:**

* Ansible Automation Platform team

**Supported ansible-core versions:**

* 2.11 or newer

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/ansible/aap-aoc-collections/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/ansible/aap-aoc-collections" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>



.. toctree::
    :maxdepth: 1


Plugin Index
------------

These are the plugins in the aap.aoc collection:


Modules
~~~~~~~

* :ref:`aws_deployment_info module <ansible_collections.aap.aoc.aws_deployment_info_module>` -- Returns the AoC AWS deployment information.

.. toctree::
    :maxdepth: 1
    :hidden:

    aws_deployment_info_module


Connection Plugins
~~~~~~~~~~~~~~~~~~

* :ref:`gcp_ssh connection <ansible_collections.aap.aoc.gcp_ssh_connection>` -- connect via gcloud compute ssh/scp client binary

.. toctree::
    :maxdepth: 1
    :hidden:

    gcp_ssh_connection


Filter Plugins
~~~~~~~~~~~~~~

* :ref:`filter_keys_from_dict filter <ansible_collections.aap.aoc.filter_keys_from_dict_filter>` -- 
* :ref:`remove_keys_from_dict filter <ansible_collections.aap.aoc.remove_keys_from_dict_filter>` -- 

.. toctree::
    :maxdepth: 1
    :hidden:

    filter_keys_from_dict_filter
    remove_keys_from_dict_filter


Role Index
----------

These are the roles in the aap.aoc collection:

* :ref:`setup_logging_monitoring role <ansible_collections.aap.aoc.setup_logging_monitoring_role>` -- This role setup the logging and monitoring.
* :ref:`standalone_aws_deployment_inventory role <ansible_collections.aap.aoc.standalone_aws_deployment_inventory_role>` -- This role generates the inventory for aws.
* :ref:`standalone_aws_upgrade role <ansible_collections.aap.aoc.standalone_aws_upgrade_role>` -- Performs the upgrade of the AoC AWS components to the latest version.
* :ref:`standalone_gcp_deployment_inventory role <ansible_collections.aap.aoc.standalone_gcp_deployment_inventory_role>` -- This role generates the inventory for gcp.
* :ref:`standalone_gcp_upgrade role <ansible_collections.aap.aoc.standalone_gcp_upgrade_role>` -- Performs the upgrade of the AoC GCP components to the latest version.

.. toctree::
    :maxdepth: 1
    :hidden:

    setup_logging_monitoring_role
    standalone_aws_deployment_inventory_role
    standalone_aws_upgrade_role
    standalone_gcp_deployment_inventory_role
    standalone_gcp_upgrade_role


.. seealso::

    List of :ref:`collections <list_of_collections>` with docs hosted here.
