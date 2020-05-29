#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 13:34:12 2020

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
def calculate_pdf (n, k, p):
    return ncr(n, k)*pow(p,k)*pow((1-p),n-k)

probability = np.zeros((11,3))##set the dataframe for probability
p = [0.25,0.5,0.75]
for i in range(3):
    for j in range(11):
        probability[j,i] = calculate_pdf(10,j,p[i])

prob = pd.DataFrame(probability)
prob.columns = ['25 percent', '50 percent','75 percent']
print(prob)


fig, ax = plt.subplots()
ax.plot(prob['25 percent'],'g--', label='25 percent')
ax.plot(prob['50 percent'],'r:', label='75 percent')
ax.plot(prob['75 percent'],'b', label='75 percent')

legend = ax.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')

########
cdf = prob.cumsum()##compute culmulated probability density
print(cdf)

fig2, bx = plt.subplots()
bx.plot(cdf['25 percent'],'g--', label='25 percent')
bx.plot(cdf['50 percent'],'r:', label='75 percent')
bx.plot(cdf['75 percent'],'b', label='75 percent')

legend = bx.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')