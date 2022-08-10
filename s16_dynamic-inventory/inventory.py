#!/usr/bin/env python3

import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json


inventory_example = {
            'all': {
                'hosts': ['node-1'],
                'vars': {
                    'ansible_host': '192.168.50.11',
                    'ansible_ssh_user': 'vagrant',
                    'ansible_ssh_private_key_file':
                        '~/.vagrant.d/insecure_private_key',
                }
            },
            '_meta': {
                'hostvars': {
                    'node-1': {
                        'host_specific_var': 'test'
                    }
                }
            }
        }

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('--list', action = 'store_true')
parser.add_argument('--host', action = 'store')
args = parser.parse_args()

inventory = {'_meta': {'hostvars': {}}}
# --list
if args.list:
    inventory = inventory_example
# --host


print(json.dumps(inventory))
