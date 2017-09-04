#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import numpy as np
from operator import itemgetter
import testdata
import tensor_cal
import tensor_multi
import luis2vec
import luisapp
import arjson

import sys

def main_json():
    #f = open('data/test_json.json', 'r')
    #data = luis2vec.getVectorByTuple(f)
    #data = luisapp.getAppJosnByUrl('http://zipcloud.ibsnet.co.jp/api/search?zipcode=4680045')
    #j = luisapp.getAppJsonByParam('これはテストデータですよ')
    #data = luis2vec.getVectorByTuple(j)
    #data = arjson.getTeacherDataList()
    namelist = [u"中村 卓磨",u"仲村 常司",u"佐藤 憲司",u"佐藤 英喜",u"佐藤　隆之",u"加藤 健太",u"吉野 友則",u"大表 正人",u"平川 昌和",u"本多 俊之",u"竹林 賢哉",u"比嘉 真人",u"沼田 歩実",]
    for name in namelist:
        ardata = arjson.getArDataList(name)
        sys.stderr.write("%s\n" % name)
        worktime = 0;
        arlist = []
        for tupleList in ardata:
            worktime = tupleList[1]
            arlist = tupleList[0]
            vec = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],dtype=float)
            for ar in arlist:
                #print ar
                jsondata = luisapp.getAppJsonByParam(ar)
                tmp_vec = luis2vec.getVector(jsondata)
                tmp_np_vec = np.array(tmp_vec, dtype=float)
                vec = vec + tmp_np_vec
            sys.stdout.write("%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%d\n" % (vec[0],vec[1],vec[2],vec[3],vec[4],vec[5],vec[6],vec[7],vec[8],vec[9],vec[10],worktime))
            sys.stderr.write("%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%lf,%d\n" % (vec[0],vec[1],vec[2],vec[3],vec[4],vec[5],vec[6],vec[7],vec[8],vec[9],vec[10],worktime))
        #print vec
        #print worktime

    #ar = ardata[0][0][0]
    #print ar
    #jsondata = luisapp.getAppJsonByParam(ar)
    #data = luis2vec.getVectorByTuple(jsondata)
    #for l in data:
        #sys.stdout.write("%s: %lf\n" % (l[0],l[1]))

def main_tensor():
    #1,1,1,1,1,0,0,0,0,0,38 0
    #1,1,1,1,0,1,0,0,0,0,44 1
    #1,1,1,0,1,1,0,0,0,0,41 2
    #1,1,0,1,1,1,0,0,0,0,48 3
    #1,0,1,1,1,1,0,0,0,0,43 4
    #0,1,1,1,1,1,0,0,0,0,41 5
    #1,1,1,1,0,0,1,0,0,0,35 6
    #1,1,1,0,1,0,1,0,0,0,32 7
    #1,1,0,1,1,0,1,0,0,0,39 8
    #1,0,1,1,1,0,1,0,0,0,34 9

    #1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2
    #1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8
    #1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25
    #1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12
    #1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23
    #0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5
    #1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1
    #1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16
    #1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3
    #1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14

    test_data = testdata.getTestData('data/teacher_data2.csv')
    print test_data['x_data']
    vec0 = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#38
    vec1 = np.array([1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#44
    vec2 = np.array([1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#41
    vec3 = np.array([1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#48
    vec4 = np.array([1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#43
    vec5 = np.array([0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#41
    vec6 = np.array([1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#35
    vec7 = np.array([1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#32
    vec8 = np.array([1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#39
    vec9 = np.array([1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#34

    #test_data = testdata.getTestData('data/test_data.csv')
    #vec0 = np.array([1,1,1,1,1,0,0,0,0,0])#38
    #vec1 = np.array([1,1,1,1,0,1,0,0,0,0])#44
    #vec2 = np.array([1,1,1,0,1,1,0,0,0,0])#41
    #vec3 = np.array([1,1,0,1,1,1,0,0,0,0])#48
    #vec4 = np.array([1,0,1,1,1,1,0,0,0,0])#43
    #vec5 = np.array([0,1,1,1,1,1,0,0,0,0])#41
    #vec6 = np.array([1,1,1,1,0,0,1,0,0,0])#35
    #vec7 = np.array([1,1,1,0,1,0,1,0,0,0])#32
    #vec8 = np.array([1,1,0,1,1,0,1,0,0,0])#39
    #vec9 = np.array([1,0,1,1,1,0,1,0,0,0])#34
    results = 'no-training'
    #results = tensor_cal.train(test_data)
    #results = tensor_cal.predict(vec1)

    #0.016497,0.054612,0.044671,0.035999,0.050665,0.052243,0.035503,0.034979,0.039986,0.760705,0.023540,2952
    vec_test = np.array([0.015105,0.075117,0.103089,0.052672,0.052740,0.040462,0.077495,0.042361,0.049867,0.035592,0.047026])
    #vec_test = np.array([1,1,1,1,1,1,1,1,1,1,1], dtype=float)
    #results = tensor_multi.train(test_data)
    results = tensor_multi.predict(vec_test)
    print results




    #print test_data['x_data']
    #print test_data['y_data'].shape
    #print type(test_data['x_data'][0][0])

if __name__ == '__main__':
    main_tensor()
    #main_json()
