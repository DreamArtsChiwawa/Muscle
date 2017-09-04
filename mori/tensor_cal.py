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

# Create the model
x = tf.placeholder(tf.float32, [None, input_vector_size])
W = tf.Variable(tf.zeros([input_vector_size, output_vector_size]))
#b = tf.Variable(tf.zeros([1]))
y = tf.matmul(x, W)

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, output_vector_size])

def train(test_data):
    # The raw formulation of cross-entropy,
    #
    #   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
    #                                 reduction_indices=[1]))
    #
    # can be numerically unstable.
    #
    # So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
    # outputs of 'y', and then average across the batch.
    #loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
    loss = tf.reduce_mean(tf.abs(y-y_))
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    #sess.run(tf.initialize_all_variables())
    # Train
    rangenum = 10000
    par_str = '%'
    for data in range(rangenum):
        past_loss = 0
        if(data % 100) == 0:
            loss_val = sess.run(loss,feed_dict={x:test_data["x_data"], y_:test_data["y_data"]})
            #print('Loss Value :',loss_val)
            par = int(data/rangenum*100)
            sys.stdout.write("\rLoss Value :%lf,%3d%s   " % (loss_val, par, par_str))
            sys.stdout.flush()
            if past_loss == loss_val:
                break
            past_loss = loss_val
        sess.run(train_step, feed_dict={x:test_data["x_data"], y_:test_data["y_data"]})

    sys.stdout.write("\rLoss Value :%lf,100%s   " % (loss_val, par_str))
    sys.stdout.flush()
    saver = tf.train.Saver();
    saved_file = saver.save(sess, savedFileName)
    print("")
    print("Saved file: " + saved_file)

    results = sess.run(W)
    return results

def predict(vec):
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess, savedFileName)

    results = sess.run(y, feed_dict={x: [vec]})
    return results
