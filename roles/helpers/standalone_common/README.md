# helpers.standalone_common

A set of helpers to be used across any AoC Standalone playbook.

## load_extra_vars

For any variable that starts with `AOC_` it will be loaded as a `fact`.

Playbook example:

```yaml
---

- hosts: localhost
  connection: local

  environment:
    AOC_foo: bar

  tasks:
    - name: "Load 'redhat.ansible_on_clouds.helpers.standalone_common' task file"
      ansible.builtin.include_role:
        name: redhat.ansible_on_clouds.helpers.standalone_common

    - name: Debug var
      ansible.builtin.debug:
        var: foo
```

You can also change the expected prefix:

```yaml
---

- hosts: localhost
  connection: local

  environment:
    MY_foo: bar

  vars:
    extra_vars_prefx: MY_

  tasks:
    - name: "Load 'redhat.ansible_on_clouds.helpers.standalone_common' task file"
      ansible.builtin.include_role:
        name: redhat.ansible_on_clouds.helpers.standalone_common

    - name: Debug var
      ansible.builtin.debug:
        var: foo
```
