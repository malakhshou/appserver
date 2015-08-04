#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
import sys
import urllib
import urllib2
import json
import logging

logger = logging.getLogger('django_site')

def index(request):
    return render_to_response('chat/index.html',
        context_instance=RequestContext(request))

def send(request):
    url = 'https://slack.com/api/channels.list?token='
    #token = 'xoxp-3164932209-7076174822-7198818065-9bf53a'
    try:
        token = request.POST['hoge']
    except (KeyError, hoge.DoesNotExist):
        return render_to_response('chat/send.html',
            context_instance=RequestContext(request))
    else:
        response = urllib.urlopen(url+token)
    data = json.loads(response.read())
    for attr in data.get('channels'):
        print("id:" + attr.get('id') + " name:" + attr.get('name'))

    return render_to_response('chat/send.html',{'hogeson': data},
        context_instance=RequestContext(request))

def post(request):
    application_number = request.POST['application_number']
    application_title = request.POST['application_title']
    applicant = request.POST['applicant']
    amount = request.POST['amount']
    application_content = request.POST['application_content']

    data = {
        'username':'WF通知' + application_number.encode(),
        'color':'good',
        'icon_url':'http://pbs.twimg.com/profile_images/3564728072/dd32151fac474f98a20fa5887a81e7ee_normal.jpeg',
        'pretext':'<http://www.google.com|申請番号' + application_number.encode() + '>の承認依頼がありました。',
        'title':application_title,
        'itle_link': 'http://flickr.com/bobby/',
        'text':application_content,
        'fields':[
            {
                'title':'申請者',
                'value':applicant,
                'short':'true'
            },
            {
                'title':'金額',
                'value':amount,
                'short':'true'
            },
            {
                'title':'承認',
                'value':'<http://www.google.com|click>',
                'short':'true'
            },
            {
                'title':'却下',
                'value':'<http://www.google.com|click> ',
                'short':'true'
            },
        ]
        }
    req = urllib2.Request('https://hooks.slack.com/services/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')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    return HttpResponseRedirect(reverse('chat.views.index'))

def out(request):
    print("hoge")
    data = {
        'username':'outgoing通知',
        'color':'good',
        'icon_url':'http://pbs.twimg.com/profile_images/3564728072/dd32151fac474f98a20fa5887a81e7ee_normal.jpeg',
        'pretext':'通知があったよ',
        'text':'ほげほげ',
        }
    req = urllib2.Request('https://hooks.slack.com/services/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')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    return
