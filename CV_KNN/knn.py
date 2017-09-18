#coding:utf8
import os
import sys
import numpy as np
import cPickle as pickle

def load_CIFAR_batch(filename):

    with open(filename,'r') as f:
        dataDict = pickle.load(f)
