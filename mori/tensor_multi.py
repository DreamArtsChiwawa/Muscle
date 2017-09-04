#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

import json
import tensorflow as tf
import numpy as np

#==============confif==============
f = open('config/config.json', 'r')
conf_data = json.load(f)

input_vector_size = conf_data['input_vector_size']
output_vector_size = conf_data['output_vector_size']
savedFileName = conf_data['save_file_path']

f.close()
#===================================

# Variables
x = tf.placeholder("float", [None, input_vector_size])

w3 = tf.Variable(tf.truncated_normal([input_vector_size, 6]))
b3 = tf.Variable(tf.zeros([6]))
hidden3 = tf.nn.tanh(tf.matmul(x,w3) + b3)

#w2 = tf.Variable(tf.truncated_normal([8, 5]))
#b2 = tf.Variable(tf.zeros([5]))
#hidden2 = tf.nn.tanh(tf.matmul(hidden3,w2) + b2)

#w1 = tf.Variable(tf.truncated_normal([5,2]))
#b1 = tf.Variable(tf.zeros([2]))
#hidden1 = tf.nn.tanh(tf.matmul(hidden2,w1) + b1)

w0 = tf.Variable(tf.truncated_normal([input_vector_size,1]))
#b0 = tf.Variable(tf.zeros([1]))

#y = tf.matmul(hidden1, w0) + b0
#y = tf.matmul(hidden3, w0) + b0
y = tf.matmul(x, w0)


y_ = tf.placeholder("float", [None, output_vector_size])


def train(test_data):# the loss and accuracy
    #loss = tf.reduce_sum(tf.abs(y-y_))
    loss = tf.losses.huber_loss(y_,y,delta=30)
    #train_step = tf.train.GradientDescentOptimizer(0.000001).minimize(loss)
    train_step = tf.train.AdamOptimizer().minimize(loss)
    #correct_prediction = tf.equal(tf.argmax(y_hypo,1), tf.argmax(y_,1))
    #accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    #sess.run(tf.initialize_all_variables())
    # Train
    rangenum = 100000
    par_str = '%'
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("training...")

    min_num = 9999.999
    for data in range(rangenum):
        past_loss = 0
        if(data % 100) == 0:
            loss_val = sess.run(loss,feed_dict={x:test_data["x_data"], y_:test_data["y_data"]})
            if loss_val < min_num:
                min_num = loss_val
            #print('Loss Value :',loss_val)
            par = int(data/rangenum*100)
            sys.stdout.write("\r[Loss Value :%lf][Min :%lf]%3d%s   " % (loss_val, min_num, par, par_str))
            sys.stdout.flush()
            #print(loss_val)
            if past_loss == loss_val:
                break
            past_loss = loss_val
        sess.run(train_step, feed_dict={x:test_data["x_data"], y_:test_data["y_data"]})

    sys.stdout.write("\r[Loss Value :%lf][Min :%lf]100%s   " % (loss_val, min_num,par_str))
    sys.stdout.flush()
    saver = tf.train.Saver();
    saved_file = saver.save(sess, savedFileName)
    print("")
    print("Saved file: " + saved_file)

    results = sess.run(w0)
    return results

def predict(vec):
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess, savedFileName)

    results = sess.run(y, feed_dict={x: [vec]})
    return results
