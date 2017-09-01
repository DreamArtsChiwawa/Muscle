# -*- coding: utf-8 -*-
import sys
import re
import os
import json
import subprocess,shlex
import datetime
import codecs
import hashlib
import codecs

data = {}
def marge(d):
	files = os.listdir(d)
	jsonfiles = []
	for f in files:
		m = re.search(".json$", f)
		if m : 
			jsonfiles.append(f)

	for f in jsonfiles:
		f = open(f, 'r')
		json_dict = json.load(f)
		if not data.has_key(json_dict[u"employee_name"]):
			data[json_dict[u"employee_name"]] = json_dict
		else:
			data[json_dict[u"employee_name"]][u"WR"].append(json_dict[u"WR"][0])

dirs = ["./"]
for d in dirs:
	marge(d)

employee_names = data.keys()
for e in employee_names:
	data[e][u"WR"] = sorted(data[e][u"WR"], key=lambda x:x[u'file_id'])

for e in employee_names:
	n = len(data[e][u"WR"])
	if n > 1:
		for i in range(n - 1):
			file_id1 = data[e][u"WR"][i][u"file_id"]
			file_id2 = data[e][u"WR"][i + 1][u"file_id"]
			month1 = file_id1 // 100000
			month2 = file_id2 // 100000
			if (month1 == month2):
				data[e][u"WR"][i][u"working_time_diff_min"] = data[e][u"WR"][i + 1][u"working_time_acc_min"] - data[e][u"WR"][i][u"working_time_acc_min"]

data2 = {}
for e in employee_names:
	n = len(data[e][u"WR"])
	if n > 1:
		data2[e] = {}
		for i in range(n):
			if not data2[e].has_key(u"WR"):
				data2[e][u"WR"] = []
			if data[e][u"WR"][i].has_key(u"working_time_diff_min"):
				data2[e][u"WR"].append(data[e][u"WR"][i])
				data2[e][u"employee_name"] = e
				data2[e][u"employee_id"] = data[e][u"employee_id"]

json.dumps(data2, ensure_ascii=False, indent=4, sort_keys=True)
