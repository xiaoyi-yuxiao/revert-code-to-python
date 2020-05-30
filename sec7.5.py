#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:43:02 2020

@author: huangxiaoyi
"""

import scipy.stats as st
import matplotlib.pyplot as plt

val = st.norm(15,5).pdf(range(40))#very useful lib to calculate density
fig, ax = plt.subplots()
ax.plot(val,'g--')

plt.xlabel('success')
plt.ylabel('probability')

cdf = val.cumsum()##compute culmulated probability density

fig2, bx = plt.subplots()
bx.plot(cdf,'g--')
plt.xlabel('success')
plt.ylabel('probability')