
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

.. _ansible_collections.aap.aoc.standalone_aws_upgrade_role:

.. Anchors: aliases


.. Title

aap.aoc.standalone_aws_upgrade role -- Performs the upgrade of the AoC AWS components to the latest version.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This role is part of the `aap.aoc collection <https://galaxy.ansible.com/aap/aoc>`_ (version 0.0.1).

    To install it use: :code:`ansible-galaxy collection install aap.aoc`.

    To use it in a playbook, specify: :code:`aap.aoc.standalone_aws_upgrade`.

.. contents::
   :local:
   :depth: 2


.. Entry point title

Entry point ``main`` -- Performs the upgrade of the AoC AWS components to the latest version.
---------------------------------------------------------------------------------------------

.. version_added


.. Deprecated


Synopsis
^^^^^^^^

.. Description

- Performs the upgrade of the AoC AWS components to the latest version.

  Simple interface to upgrade an environment to a new VM image.

- Authors:

  - Luiz Costa (@thenets)


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
        <div class="ansibleOptionAnchor" id="parameter-main--aws_foundation_stack_name"></div>

      .. _ansible_collections.aap.aoc.standalone_aws_upgrade_role__parameter-main__aws_foundation_stack_name:

      .. rst-class:: ansible-option-title

      **aws_foundation_stack_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--aws_foundation_stack_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      AoC AWS foundation stack name


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--aws_s3_bucket_name"></div>

      .. _ansible_collections.aap.aoc.standalone_aws_upgrade_role__parameter-main__aws_s3_bucket_name:

      .. rst-class:: ansible-option-title

      **aws_s3_bucket_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--aws_s3_bucket_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      AoC AWS S3 bucket name. It will be used to store the AoC AWS foundation stack template.


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

