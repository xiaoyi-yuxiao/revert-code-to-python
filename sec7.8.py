#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:24:33 2020

@author: huangxiaoyi
"""

import scipy.stats as st
import matplotlib.pyplot as plt
a = np.linspace(0,50,25)
val = st.lognorm(1,1).pdf(a)#very useful lib to calculate density
fig, ax = plt.subplots()
ax.plot(val,'g--',label='m=100')
legend = ax.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')

cdf = val = st.lognorm(1,1).cdf(a)##compute culmulated probability density
fig2, bx = plt.subplots()
bx.plot(cdf,'g--',label='m=100')
legend = ax.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')
