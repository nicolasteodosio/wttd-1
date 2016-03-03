# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line

from eventex.settings import ROOT_DIR


default_args = []
user_args = sys.argv[1:]

args = user_args + default_args
manage_py = ROOT_DIR + 'manage.py'
commands = [manage_py, 'test', 'core', 'subscriptions']
commands.extend(args)

if __name__ == '__main__':
    old_settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'eventex.settings'
    execute_from_command_line(commands)
    os.environ['DJANGO_SETTINGS_MODULE'] = old_settings_module or ''