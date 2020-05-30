#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 20:24:11 2020

@author: huangxiaoyi
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##define the calculation
def calculate_pdf (lambda_, k):
    return pow(np.e,-1*lambda_)*pow(lambda_,k)/math.factorial(k)

probability = np.zeros((21,4))##set the dataframe for probability
lambd = [4,6,8,10]
for i in range(4):
    for j in range(21):
        probability[j,i] = calculate_pdf(lambd[i],j)

prob = pd.DataFrame(probability)
prob.columns = ['m=4', 'm=6','m=8','m=10']

fig, ax = plt.subplots()
ax.plot(prob['m=4'],'g--', label='m=4')
ax.plot(prob['m=6'],'r:', label='m=6')
ax.plot(prob['m=8'],'b', label='m=8')
ax.plot(prob['m=10'],'b--', label='m=10')

legend = ax.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')

########
cdf = prob.cumsum()##compute culmulated probability density
print(cdf)

fig2, bx = plt.subplots()
bx.plot(cdf['m=4'],'g--', label='m=4')
bx.plot(cdf['m=6'],'r:', label='m=6')
bx.plot(cdf['m=8'],'b', label='m=8')
bx.plot(cdf['m=10'],'b--', label='m=10')

legend = bx.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')