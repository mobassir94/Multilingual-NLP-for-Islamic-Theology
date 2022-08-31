# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 09:22:11 2022

@author: MOBASSIR
"""
import numpy as np


def dot_product_similarity(v1, v2):
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    return np.dot(v1, v2) / n1 / n2

def pairwise_euclidean_dists(x, y):
    dists = -2 * np.matmul(x, y.T)
    dists +=  np.sum(x**2, axis=1)[:, np.newaxis]
    dists += np.sum(y**2, axis=1)
    return  np.sqrt(dists)

