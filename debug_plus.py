# Copyright (c) 2019, Foo Chuan Wei
# Copyright (c) 2017, Ansible
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

'''Variant of the debug callback plugin that shows the invocation arguments.

Adapted from:
https://github.com/ansible/ansible/blob/d2438b6b6b9dbb5f0f320fbe9e6e30b102006c1d/lib/ansible/plugins/callback/debug.py

Differences:
  * Shows the 'invocation' field i.e. the parameters of the task.
'''

import json
from ansible.plugins.callback.default import CallbackModule as CallbackModule_default


class CallbackModule(CallbackModule_default):
    '''Override for the default callback module.
    Show invocation information.
    '''
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'debug_plus'

    def _dump_results(self, result):
        # Enable JSON identation
        result['_ansible_verbose_always'] = True

        save = {}
        # Reference for common return values:
        # https://docs.ansible.com/ansible/2.7/reference_appendices/common_return_values.html
        for key in ['stdout',
                    'stdout_lines',
                    'stderr',
                    'stderr_lines',
                    'msg',
                    'invocation']:
            if key in result:
                save[key] = result.pop(key)

        output = CallbackModule_default._dump_results(self, result)

        # Exclude stdout_lines, stderr_lines in output.
        for key in ['stdout', 'stderr', 'msg']:
            if key in save and save[key]:
                output += '\n\n%s:\n\n%s\n' % (key.upper(), save[key])

        # Deal with 'invocation'.
        if 'invocation' in save and save['invocation']:
            invocation = json.dumps(save['invocation'], indent=4)  # Pretty printed json.
            output += '\n\n%s:\n\n%s\n' % ('INVOCATION', invocation)

        for key, value in save.items():
            result[key] = value

        return output
