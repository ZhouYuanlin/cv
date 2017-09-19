#coding:utf8
import os
import sys
import numpy as np
import cPickle as pickle

def load_CIFAR_batch(filename):

    with open(filename,'r') as f:
        dataDict = pickle.load(f)
        X = dataDict['data']
        Y = dataDict['labels']
        X = X.reshape(10000,3,32,32).transpose(0,2,3,1).astype("float")
        Y = np.array(Y)
        return  X,Y
def load_CIFAR10(ROOT):
    xs=[]
    ys=[]