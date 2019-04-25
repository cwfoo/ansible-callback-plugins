# Copyright (c) 2019, Foo Chuan Wei
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''Variant of the YAML callback plugin that show the invocation arguments.

Adapted from:
https://github.com/ansible/ansible/blob/8f5cd049d677e56648da3a6fc1c790a30d4a90f5/lib/ansible/plugins/callback/yaml.py

Differences:
  * Shows the 'invocation' field i.e. the parameters of the task.
'''

from ansible.plugins.callback.yaml import CallbackModule as CallbackModule_yaml


class CallbackModule(CallbackModule_yaml):
    '''Override for the yaml callback module.
    Show the 'invocation' field in stdout.
    '''
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'yaml_plus'

    def _dump_results(self, result, indent=None, sort_keys=True, keep_invocation=True):
        return super()._dump_results(result, indent, sort_keys, keep_invocation=True)
