# Ansible Callback Plugins
Custom [`stdout_callback` plugins](https://docs.ansible.com/ansible/2.7/plugins/callback.html#plugin-list) that make the output of `ansible-playbook` include complete invocation information. Complete invocation information is useful for tracking down mistakes in tasks.

The official `stdout_callback` plugins do not include complete invocation information in the output of `ansible-playbook`. To illustrate, suppose we have this task:

```
- name: Create directory
  file:
    path: /home/user/my-files/
    state: directory
    owner: user
    group: user
```

Using the official `yaml` plugin (set using `stdout_callback = yaml` in `ansible.cfg`), and running the task using the verbose option (i.e. `ansible-playbook -v ...`) results in:

```
TASK [Create directory] ***********************************
ok: [10.0.0.1] => changed=false
  gid: 33
  group: user
  mode: '0755'
  owner: user
  path: /home/user/my-files/
  size: 4096
  state: directory
  uid: 33
```

In contrast, using the custom `yaml_plus` plugin (provided in this repository) results in:

```
TASK [Create directory] ***********************************
ok: [10.0.0.1] => changed=false
  gid: 33
  group: user
  invocation:
    module_args:
      _diff_peek: null
      _original_basename: null
      access_time: null
      access_time_format: '%Y%m%d%H%M.%S'
      attributes: null
      backup: null
      content: null
      delimiter: null
      directory_mode: null
      follow: true
      force: false
      group: user
      mode: null
      modification_time: null
      modification_time_format: '%Y%m%d%H%M.%S'
      owner: user
      path: /home/user/my-files/
      recurse: false
      regexp: null
      remote_src: null
      selevel: null
      serole: null
      setype: null
      seuser: null
      src: null
      state: directory
      unsafe_writes: null
  mode: '0755'
  owner: user
  path: /home/user/my-files/
  size: 4096
  state: directory
  uid: 33
```

Notice that the complete invocation information is shown.

## Usage
Two custom plugins are provided in this repository:
* `debug_plus` (analogous to the official `debug` plugin)
* `yaml_plus` (analogous to the official `yaml` plugin)

To use a custom plugin provided by this repository:
* Create a directory named `callback_plugins` in the same directory as the `ansible.cfg` file of your project.
* Place the plugin file (e.g. `debug_plus.py`) into the `callback_plugins` directory.
* Open `ansible.cfg`, and set `stdout_callback` to the plugin you wish to use (e.g. `stdout_callback = debug_plus`).
* Note: to be able to see invocation information, run playbooks using the verbose option (i.e. `ansible-playbook -v ...`).

## Ansible version information
The plugins have been used on ansible-playbook 2.7.6 with python 3.6.7. The plugins might be able to function properly on other versions of Ansible, but this cannot be guaranteed.

## License
This project is distributed under the GNU General Public License version 3 (see LICENSE).
