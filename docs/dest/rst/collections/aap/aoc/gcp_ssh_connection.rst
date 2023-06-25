
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-default-mark
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.aap.aoc.gcp_ssh_connection:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

aap.aoc.gcp_ssh connection -- connect via gcloud compute ssh/scp client binary
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This connection plugin is part of the `aap.aoc collection <https://galaxy.ansible.com/aap/aoc>`_ (version 0.0.1).

    To install it, use: :code:`ansible-galaxy collection install aap.aoc`.

    To use it in a playbook, specify: :code:`aap.aoc.gcp_ssh`.

.. version_added


.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This connection plugin allows ansible to communicate to the target machines via normal gcloud compute ssh/scp command line.


.. Aliases


.. Requirements






.. Options

Parameters
----------


.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-compute_scp_flags"></div>

      .. _ansible_collections.aap.aoc.gcp_ssh_connection__parameter-compute_scp_flags:

      .. rst-class:: ansible-option-title

      **compute_scp_flags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-compute_scp_flags" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      flags to pass to the gcloud compute scp command-line


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"--tunnel-through-iap --quiet"`

      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Variable: ansible\_gcp\_compute\_ssh\_flags


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-compute_ssh_args"></div>

      .. _ansible_collections.aap.aoc.gcp_ssh_connection__parameter-compute_ssh_args:

      .. rst-class:: ansible-option-title

      **compute_ssh_args**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-compute_ssh_args" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      arguments to pass to the underlying ssh command


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Variable: ansible\_gcp\_compute\_ssh\_args


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-compute_ssh_flags"></div>

      .. _ansible_collections.aap.aoc.gcp_ssh_connection__parameter-compute_ssh_flags:

      .. rst-class:: ansible-option-title

      **compute_ssh_flags**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-compute_ssh_flags" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      flags to pass to the gcloud compute ssh command-line


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"--tunnel-through-iap --no-user-output-enabled --quiet"`

      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Variable: ansible\_gcp\_compute\_ssh\_flags


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-host"></div>

      .. _ansible_collections.aap.aoc.gcp_ssh_connection__parameter-host:

      .. rst-class:: ansible-option-title

      **host**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-host" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      instance name to connect to.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"inventory\_hostname"`

      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Variable: inventory\_hostname

      - Variable: ansible\_host

      - Variable: ansible\_ssh\_host

      - Variable: delegated\_vars['ansible\_host']

      - Variable: delegated\_vars['ansible\_ssh\_host']


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-reconnection_retries"></div>

      .. _ansible_collections.aap.aoc.gcp_ssh_connection__parameter-reconnection_retries:

      .. rst-class:: ansible-option-title

      **reconnection_retries**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-reconnection_retries" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Number of attempts to connect.

      Ansible retries connections only if it gets an SSH error with a return code of 255.

      Any errors with return codes other than 255 indicate an issue with program execution.


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`3`

      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - INI entries:

        .. code-block::

          [connection]
          retries = 3



        .. code-block::

          [ssh_connection]
          retries = 3


      - Environment variable: :envvar:`ANSIBLE\_SSH\_RETRIES`

      - Variable: ansible\_ssh\_retries


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-zone"></div>

      .. _ansible_collections.aap.aoc.gcp_ssh_connection__parameter-zone:

      .. rst-class:: ansible-option-title

      **zone**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-zone" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      the zone where the instance reside


      .. rst-class:: ansible-option-line

      :ansible-option-configuration:`Configuration:`

      - Variable: ansible\_gcp\_zone


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    # Making use of Dynamic Inventory Plugin
    # =======================================
    # google.cloud.gcp_compute (Dynamic Inventory - Linux)
    # This will return the name of hosts
    # plugin: "google.cloud.gcp_compute"
    # auth_kind: "application"
    # hostnames:
    #  - name
    # compose can be use to set the plugin vars

    - name: Get hostname and user
      hosts: all
      connection: aap.aoc.gcp_ssh

      vars:
        ansible_gcp_compute_ssh_flags: "--tunnel-through-iap --no-user-output-enabled --quiet"
        ansible_gcp_zone: "us-east1-b"
        ansible_gcp_compute_scp_flags: "--tunnel-through-iap --quiet"

      tasks:
        - name: Get hostname
          ansible.builtin.command:
            cmd: "hostname"
          register: hostname

        - name: Show hostname
          ansible.builtin.debug:
            msg:
            - "hostname: {{ hostname.stdout_lines }}"




.. Facts


.. Return values


..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Dominique Vernier (@dominiquevernier)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/ansible/aap-aoc-collections/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/ansible/aap-aoc-collections" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

