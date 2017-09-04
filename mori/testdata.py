#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import numpy as np
import json

f = open('config/config.json', 'r')
conf_data = json.load(f)
input_vector_size = conf_data['input_vector_size']
f.close()

dict = {}

def getTestData(data_path):
    x_array = []
    y_array = []
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        isFirstTime = True
        a = 0
        b = 0;
        for row in reader:
            x_array.append(map(float,row[:input_vector_size]))
            y_array.append(map(float,row[input_vector_size:]))
        x = np.array(x_array)
        y = np.array(y_array)

    dict = {"x_data":x.astype(np.float32), "y_data":y.astype(np.float32)}
    return dict
