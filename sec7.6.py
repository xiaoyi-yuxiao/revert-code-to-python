#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:07:23 2020

@author: huangxiaoyi
"""


import scipy.stats as st
import matplotlib.pyplot as plt

val = st.norm(100,30).pdf(range(500))#very useful lib to calculate density
val2 = st.norm(200,30).pdf(range(500))
val3 = st.norm(300,30).pdf(range(500))
fig, ax = plt.subplots()
ax.plot(val,'g--',label='m=100')
ax.plot(val2,'b:',label='m=200')
ax.plot(val3,'r',label='m=200')
legend = ax.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')

cdf = val.cumsum()##compute culmulated probability density
cdf2 = val2.cumsum()
cdf3 = val3.cumsum()
fig2, bx = plt.subplots()
bx.plot(cdf,'g--',label='m=100')
bx.plot(cdf2,'b:',label='m=200')
bx.plot(cdf3,'r',label='m=300')
legend = ax.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')