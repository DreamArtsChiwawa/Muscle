#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

WRlist = []
teacherDataList = []

def getTeacherDataList():
    with open('data/database.json','r') as f:
        jsondata = json.load(f)
        jlist = jsondata.values()
        for l in jlist:
            for ll in l['WR']:
                WRlist.append(ll)

    for l in WRlist:
        teacherDataList.append((l["AR"], l["working_time_diff_min"]))
    return teacherDataList

#ARのリストとそれにかかる時間のリスト
def getArDataList(employee_name):
    with open('data/database.json','r') as f:
        jsondata = json.load(f)
        WRlist = jsondata[employee_name]["WR"]
        ret = []
        for wr in WRlist:
            tmp = (wr["AR"], wr["working_time_diff_min"])
            ret.append(tmp)
        return ret
