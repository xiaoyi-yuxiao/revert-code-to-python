#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:19:25 2020

@author: huangxiaoyi
"""

import numpy as np
import pandas as pd
import operator as op
from functools import reduce
import matplotlib.pyplot as plt
##define the function of n choose k
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom
##define the calculation
def calculate_pdf (N, h, n, x):
    return ncr(h, x)*ncr(N-h,n-x)/ncr(N,n)

def hypergeometric(N,h,n):
    probability = np.zeros((n+1,1))##set the dataframe for probability
    for i in range(n+1):
        probability[i] = calculate_pdf(N, h, n, i)
    return probability

prob = pd.DataFrame(hypergeometric(10,4,6))
prob.columns = ['probability']
print(prob)


