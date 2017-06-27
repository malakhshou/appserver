# -*- coding: utf-8 -*-
import os
import sys

if os.environ.get('SERVER_SOFTWARE','').startswith('Dev'):
    sys.path.append('/Users/matsumotokoyo/python/out/out')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "out.settings")

#APIKEYS
consumer_api = "TLMx9b2GcPAeUBMElKY8PwJhE"
consumer_secret = "IRUF7n9Q0idV5QOzGMrDgT75LKqLK8OkscrxAUYg1dJV1NCmWp"
access_token = "876140352347840513-15aKHglha33QnmoAyiTZH3lFl9FUVMu"
access_token_secret = "uyMP91Dk2yI6aCbC2ybxQ9ycXak57WNHH3QxsT9hJtGNX"

