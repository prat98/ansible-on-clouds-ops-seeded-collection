
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

.. _ansible_collections.aap.aoc.setup_logging_monitoring_role:

.. Anchors: aliases


.. Title

aap.aoc.setup_logging_monitoring role -- This role setup the logging and monitoring.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This role is part of the `aap.aoc collection <https://galaxy.ansible.com/aap/aoc>`_ (version 0.0.1).

    To install it use: :code:`ansible-galaxy collection install aap.aoc`.

    To use it in a playbook, specify: :code:`aap.aoc.setup_logging_monitoring`.

.. contents::
   :local:
   :depth: 2


.. Entry point title

Entry point ``main`` -- This role setup the logging and monitoring.
-------------------------------------------------------------------

.. version_added


.. Deprecated


Synopsis
^^^^^^^^

.. Description

- Install monitoring tools and configure them to send data to the Google Cloud Monitoring service.

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
        <div class="ansibleOptionAnchor" id="parameter-main--components"></div>

      .. _ansible_collections.aap.aoc.setup_logging_monitoring_role__parameter-main__components:

      .. rst-class:: ansible-option-title

      **components**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--components" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      TODO\_DOC\_HERE


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--db_user"></div>

      .. _ansible_collections.aap.aoc.setup_logging_monitoring_role__parameter-main__db_user:

      .. rst-class:: ansible-option-title

      **db_user**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--db_user" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      TODO\_DOC\_HERE


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--default_collector_interval"></div>

      .. _ansible_collections.aap.aoc.setup_logging_monitoring_role__parameter-main__default_collector_interval:

      .. rst-class:: ansible-option-title

      **default_collector_interval**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--default_collector_interval" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      TODO\_DOC\_HERE


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--logging_enabled"></div>

      .. _ansible_collections.aap.aoc.setup_logging_monitoring_role__parameter-main__logging_enabled:

      .. rst-class:: ansible-option-title

      **logging_enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--logging_enabled" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      TODO\_DOC\_HERE


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-main--monitoring_enabled"></div>

      .. _ansible_collections.aap.aoc.setup_logging_monitoring_role__parameter-main__monitoring_enabled:

      .. rst-class:: ansible-option-title

      **monitoring_enabled**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-main--monitoring_enabled" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      TODO\_DOC\_HERE


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`false`
      - :ansible-option-choices-entry:`true`


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

