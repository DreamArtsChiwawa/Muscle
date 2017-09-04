#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from operator import itemgetter
import numpy as np

f = open('config/config.json', 'r')
conf_data = json.load(f)

dict = {}
indents = conf_data["indents"]
for indent in indents:
    dict[indent.encode('utf-8')] = 0.0

keys = []

#Keyでソートされた値をnumpyのベクトルで返す
def getVector(jstr):
    jdict = json.loads(jstr)
    intents = jdict["intents"]
    for data in intents:
        tmp = data["intent"].encode('utf-8')
        dict[tmp] = data["score"]

    keys = sorted(dict, key=itemgetter(0))

    value = []
    for key in keys:
        #print key #for debug
        value.append(dict[key])

    return value

#(Key,Value)の形で、Keyでソートされたタプルのリストを返す
def getVectorByTuple(jstr):
    jdict = json.loads(jstr)
    intents = jdict["intents"]
    for data in intents:
        tmp = data["intent"].encode('utf-8')
        dict[tmp] = data["score"]

    keys = sorted(dict, key=itemgetter(0))

    #print keys #for debug
    tlist = []
    for key in keys:
        t = key, dict[key]
        tlist.append(t)

    return tlist
