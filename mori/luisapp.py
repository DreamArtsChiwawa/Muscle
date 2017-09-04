#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urlparse
import requests

#defurl = 'http://zipcloud.ibsnet.co.jp/api/search?' #for debug
defurl = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/ab882d01-22cd-4256-a26b-f367824e1363?subscription-key=b6dc1c4790354d64bf5ec2cadbf242ed&timezoneOffset=0&verbose=true&q='


def getAppJsonByUrl(url):
    response = requests.get(url)
    html = response.text
    return html

def getAppJsonByParam(param):
    url = defurl+param
    response = requests.get(url)
    html = response.text
    return html
