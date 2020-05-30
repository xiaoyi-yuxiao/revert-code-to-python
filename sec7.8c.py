#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 22:33:25 2020

@author: huangxiaoyi
"""

import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,20,500)
val = st.norm(1,0.4).pdf(x)#very useful lib to calculate density
val2 = st.norm(1,0.6).pdf(x)
val3 = st.norm(1,1).pdf(x)
fig, ax = plt.subplots()
ax.plot(val,'g--',label='s=0.4')
ax.plot(val2,'b:',label='s=0.6')
ax.plot(val3,'r',label='s=1')
legend = ax.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')

val4 = st.norm(1,1).pdf(x)#very useful lib to calculate density
val5 = st.norm(1,1.2).pdf(x)
val6 = st.norm(1,1.6).pdf(x)
fig2, bx = plt.subplots()
bx.plot(val4,'g--',label='s=1')
bx.plot(val5,'b:',label='s=1.2')
bx.plot(val6,'r',label='s=1.6')
legend = bx.legend(loc='upper right', shadow=True)
plt.xlabel('success')
plt.ylabel('probability')
