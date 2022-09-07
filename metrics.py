# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:22:11 2022

@author: MOBASSIR
"""
import numpy as np
from numpy import dot
from numpy.linalg import norm

#https://stackoverflow.com/questions/21030391/how-to-normalize-a-numpy-array-to-a-unit-vector

def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)
    


def dot_product_similarity(v1, v2):
    return (normalized(v1) * normalized(v2)).sum(axis=1)
    


def pairwise_euclidean_dists(x, y):
    dists = -2 * np.matmul(x, y.T)
    dists +=  np.sum(x**2, axis=1)[:, np.newaxis]
    dists += np.sum(y**2, axis=1)
    return  np.sqrt(dists)

