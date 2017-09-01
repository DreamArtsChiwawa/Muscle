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

def json_write(path, data):
    with codecs.open(path,'w','utf-8') as f:
        dump = json.dumps(data,ensure_ascii=False)
        f.write(dump)

argv = sys.argv
argc = len(argv)

filename = argv[1]

command = './AR.sh ' + filename
devnull = open('/dev/null', 'w')
proc = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=devnull)
AR_ = proc.stdout.read()
AR_ = AR_.split('\n')
AR = []
for a in AR_:
	if a == "":
		continue
	AR.append(a)
if (len(AR) == 0): quit()

name = ""
date = ""
time = ""
month = ""

file_data = codecs.open(filename, "r", "utf-8")

lastmonth = 0
for line in file_data:
    line = line.replace('\n','')
    name_match = re.match(ur"From:\s*(.*?)\s*<", line)
    date_match = re.match(ur"Date:\s*(.*)\s*$", line)
    time_match = re.match(ur"^[\s　]*([0-9]+年)?([0-9]+月)(.*?)([0-9]+時間[0-9]+分)", line)

    if name_match:
    	name = name_match.group(1)
    if date_match:
    	date = date_match.group(1)
    if time_match:
    	month = time_match.group(2)
    	month = int(month.replace(u"月", u""))
    	if lastmonth < month:
    		lastmonth = month
    		time = time_match.group(4)

if name == u"":
	quit()
if date == u"":
	quit()
if time == u"":
	quit()
if lastmonth == 0:
	quit()


hm_match = re.match(ur"^([0-9]+)時間([0-9]+)分", time)

time_min = 0
if hm_match:
	time_min = int(hm_match.group(1)) * 60 + int(hm_match.group(2))

name = name.encode("utf-8")
date = date.encode("utf-8")
time = time.encode("utf-8")
file_id = int(filename.split(".")[0]) + lastmonth * 100000 

ret = {
	"employee_id":hashlib.md5(name).hexdigest(), 
	"employee_name": name, 
	"WR":
		[
			{
				"file_name": filename, 
				"file_id": file_id,
				"path": os.path.abspath(os.path.dirname(__file__)), 
				"date": date, 
				"working_month": lastmonth,
				"working_time_acc": time, 
				"working_time_acc_min": time_min,
				"AR": AR
			}
		]
	
}
print json.dumps(ret, ensure_ascii=False, indent=4, sort_keys=True)

