# -*- coding: utf-8 -*-
import os
import sys

if os.environ.get('SERVER_SOFTWARE','').startswith('Dev'):
    sys.path.append('/Users/matsumotokoyo/python/out/out')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "out.settings")

#APIKEYS
# changed all API keys to XXXX as security team was behind me to delete them. 

consumer_api = "XXXXXX"
consumer_secret = "XXXXXX"
access_token = "XXXXXX"
access_token_secret = "XXXXXX"

slack_api_token = "XXXXXX
shodan_api = "XXXXXX"
