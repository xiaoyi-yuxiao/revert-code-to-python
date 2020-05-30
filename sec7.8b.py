#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:30:05 2020

@author: huangxiaoyi
"""
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
a = np.linspace(0,50,25)
val = st.lognorm(1,1).pdf(a)#very useful lib to calculate density
val2 = st.lognorm(2,1).pdf(a)
val3 = st.lognorm(3,1).pdf(a)
fig, ax = plt.subplots()
ax.plot(val,'g--',label='m=1')
ax.plot(val2,'b:',label='m=2')
ax.plot(val3,'r',label='m=3')
legend = ax.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')

cdf = st.lognorm(1,1).cdf(a)##compute culmulated probability density
cdf2 = st.lognorm(2,1).cdf(a)
cdf3 = st.lognorm(3,1).cdf(a)
fig2, bx = plt.subplots()
bx.plot(cdf,'g--',label='m=1')
bx.plot(cdf2,'b:',label='m=2')
bx.plot(cdf3,'r',label='m=3')
legend = bx.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')
