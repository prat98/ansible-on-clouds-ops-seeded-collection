
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

.. _ansible_collections.aap.aoc.aws_deployment_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

aap.aoc.aws_deployment_info module -- Returns the AoC AWS deployment information.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `aap.aoc collection <https://galaxy.ansible.com/aap/aoc>`_ (version 0.0.1).

    To install it, use: :code:`ansible-galaxy collection install aap.aoc`.

    To use it in a playbook, specify: :code:`aap.aoc.aws_deployment_info`.

.. version_added

.. rst-class:: ansible-version-added

New in aap.aoc 0.0.1

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Returns the AoC AWS deployment information. It includes data from the AWS CloudFormation stack outputs and the load balancer components.


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
        <div class="ansibleOptionAnchor" id="parameter-foundation_stack_name"></div>

      .. _ansible_collections.aap.aoc.aws_deployment_info_module__parameter-foundation_stack_name:

      .. rst-class:: ansible-option-title

      **foundation_stack_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-foundation_stack_name" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The name of the foundation stack deployment.


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    # Pass in a message
    - name: Test with a message
      aap.aoc.aws_deployment_info:
        foundation_stack_name: my_deployment




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-foundation_stack_name"></div>

      .. _ansible_collections.aap.aoc.aws_deployment_info_module__return-foundation_stack_name:

      .. rst-class:: ansible-option-title

      **foundation_stack_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-foundation_stack_name" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The foundation stack deployment name.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"my\_deployment"`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-health_check"></div>

      .. _ansible_collections.aap.aoc.aws_deployment_info_module__return-health_check:

      .. rst-class:: ansible-option-title

      **health_check**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-health_check" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The AWS load balancer health check.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`{"automation-controller": "HTTP:80/health", "automation-hub": "HTTP:80/health"}`


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-stack_outputs"></div>

      .. _ansible_collections.aap.aoc.aws_deployment_info_module__return-stack_outputs:

      .. rst-class:: ansible-option-title

      **stack_outputs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-stack_outputs" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The AWS CloudFormation stack outputs. The key is the CloudFormation 'output.ExportName'.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-status"></div>

      .. _ansible_collections.aap.aoc.aws_deployment_info_module__return-status:

      .. rst-class:: ansible-option-title

      **status**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-status" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The AWS CloudFormation health check status. [healthy, unhealthy]


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` always

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` :ansible-rv-sample-value:`"healthy"`


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Luiz Costa (@thenets)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/ansible/aap-aoc-collections/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/ansible/aap-aoc-collections" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

