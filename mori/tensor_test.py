#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys

import tensorflow as tf
import numpy as np

FLAGS = None


def done(test_data):
    #print(test_data["x_data"])
    #print(test_data["y_data"])

  # Create the model
    x = tf.placeholder(tf.float32, [None, 10])
    W = tf.Variable(tf.zeros([10, 1]))
    #b = tf.Variable(tf.zeros([1]))
    y = tf.matmul(x, W)

    # Define loss and optimizer
    y_ = tf.placeholder(tf.float32, [None, 1])

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
    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    #sess.run(tf.initialize_all_variables())
    # Train
    for data in range(10000):
        if(data % 1000) == 999:
            loss_val = sess.run(loss,feed_dict={x:test_data["x_data"], y_:test_data["y_data"]})
            print('Loss Value :',loss_val)
        sess.run(train_step, feed_dict={x:test_data["x_data"], y_:test_data["y_data"]})

    results = sess.run(W)
    return results
