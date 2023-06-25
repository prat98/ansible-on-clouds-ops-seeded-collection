
.. Document meta

:orphan:

.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-default-mark
.. role:: ansible-option-default-bold

.. Anchors

.. _ansible_collections.aap.aoc.standalone_gcp_upgrade_role:

.. Anchors: aliases


.. Title

aap.aoc.standalone_gcp_upgrade role -- Performs the upgrade of the AoC GCP components to the latest version.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This role is part of the `aap.aoc collection <https://galaxy.ansible.com/aap/aoc>`_ (version 0.0.1).

    To install it use: :code:`ansible-galaxy collection install aap.aoc`.

    To use it in a playbook, specify: :code:`aap.aoc.standalone_gcp_upgrade`.

.. contents::
   :local:
   :depth: 2


.. Entry point title

Entry point ``main`` -- Performs the upgrade of the AoC GCP components to the latest version.
---------------------------------------------------------------------------------------------

.. version_added


.. Deprecated


Synopsis
^^^^^^^^

.. Description

- Performs the upgrade of the AoC GCP components to the latest version.

  Simple interface to upgrade an environment to a new VM image.

    Pending:

    #. Missing extension offer upgrade
    #. The deployment name to be used across all playbooks
    #. The authentication for fresh environments. This will remove the \`gcp\_service\_account\_credentials\_json\_path\` requirement
    #. Database backup
    #. Rollback if the upgrade fails
    #. Cleanup leftovers, like old \`Instance Group Templates\`

- Inputs example

  1. Set your deployment name and the image you want to upgrade to:

  ::

    # ./inputs/vars.yaml
    #
    # AoC GCP: Upgrade vars
    ---

    gcp\_deployment\_name: aoc-prod

    gcp\_service\_account\_credentials\_json\_path: /path/to/\<MY\_SERVICE\_ACCOUNT\>.json
    gcp\_compute\_region: "us-east1"
    gcp\_compute\_zone: "us-east1-b"

    gcp\_image\_name\_to: https://www.googleapis.com/compute/v1/projects/\<MY\_PROJECT\>/global/images/\<MY\_IMAGE\_NAME\>


  2. Run the command:

  ::

    ansible-playbook -e @inputs/vars.yaml aap.aoc.gcp\_upgrade

- \*Authors\*

  - Luiz Costa (@thenets)
  - Leena Jawale (@leena-jawale)
  - Dominique Vernier (@itdove)

.. Requirements


.. Options

Parameters
^^^^^^^^^^

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--gcp_compute_region"></div>

      .. _ansible_collections.aap.aoc.standalone_gcp_upgrade_role__parameter-main__gcp_compute_region:

      .. rst-class:: ansible-option-title

      **gcp_compute_region**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--gcp_compute_region" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      GCP compute region.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--gcp_compute_zone"></div>

      .. _ansible_collections.aap.aoc.standalone_gcp_upgrade_role__parameter-main__gcp_compute_zone:

      .. rst-class:: ansible-option-title

      **gcp_compute_zone**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--gcp_compute_zone" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      GCP compute zone.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--gcp_deployment_name"></div>

      .. _ansible_collections.aap.aoc.standalone_gcp_upgrade_role__parameter-main__gcp_deployment_name:

      .. rst-class:: ansible-option-title

      **gcp_deployment_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--gcp_deployment_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      AoC GCP deployment name


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--gcp_gcloud_bin_path"></div>

      .. _ansible_collections.aap.aoc.standalone_gcp_upgrade_role__parameter-main__gcp_gcloud_bin_path:

      .. rst-class:: ansible-option-title

      **gcp_gcloud_bin_path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--gcp_gcloud_bin_path" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      gcloud binary absolute path


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"gcloud"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--gcp_image_name_to"></div>

      .. _ansible_collections.aap.aoc.standalone_gcp_upgrade_role__parameter-main__gcp_image_name_to:

      .. rst-class:: ansible-option-title

      **gcp_image_name_to**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--gcp_image_name_to" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      AoC GCP VM image name to upgrade to. By default, the latest image will be used.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--gcp_service_account_credentials_json_path"></div>

      .. _ansible_collections.aap.aoc.standalone_gcp_upgrade_role__parameter-main__gcp_service_account_credentials_json_path:

      .. rst-class:: ansible-option-title

      **gcp_service_account_credentials_json_path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--gcp_service_account_credentials_json_path" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      GCP service account credentials json file path. https://cloud.google.com/iam/docs/creating-managing-service-account-keys


      .. raw:: html

        </div>


.. Notes


.. Seealso




.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/ansible/aap-aoc-collections/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/ansible/aap-aoc-collections" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

