#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:59:18 2020

@author: huangxiaoyi
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dice_prob = np.ones(6)/6.0 #calculate the probability
s_0 = pd.Series([1,2,3,4,5,6],name='number')
s_1 = pd.Series(dice_prob, name='probability')
s_2 = pd.Series(np.cumsum(dice_prob), name='cdf')# use data frame to calculate cdf
prob = pd.concat([s_0,s_1, s_2], axis=1)# concacnate the data to pandas data frame
print (prob)
plt.figure()
plt.subplot(221)
plt.xticks([1,2,3,4,5,6])# set the length of x_axis
plt.plot(np.linspace(1,6,6),dice_prob,'-')
plt.legend(['PDF'])
plt.subplot(222)
plt.xticks([1,2,3,4,5,6])
plt.plot(np.linspace(1,6,6),np.cumsum(dice_prob),'-')
plt.legend(['CDF'])