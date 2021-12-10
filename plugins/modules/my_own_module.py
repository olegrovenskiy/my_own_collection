#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is module for Netology Devops HW-8.6

The module takes content and put it to the file

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".

version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    path:
        description: The path to file
        required: true
        type: str
    content:
        description: Content, any string data
        required: false
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name


author:
    - olegrovenskiy

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default='Some content')
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)
    
    import os.path
    check_file = os.path.exists(module.params['path'])
    if check_file == True:
       result['changed'] = False
       result['mesage'] = 'file was before'
       result['original_mesage'] = 'original'
    else:
       with open(module.params['path'], 'w') as  some_file:
         some_file.write(module.params['content'])
       result['changed'] = True
       result['mesage'] = 'file was created'
       result['original_mesage'] = 'original'

	 

# in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
