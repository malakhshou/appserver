# -*- coding: utf-8 -*-
import os
import sys

if os.environ.get('SERVER_SOFTWARE','').startswith('Dev'):
    sys.path.append('/Users/matsumotokoyo/python/out/out')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "out.settings")
