#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:27:44 2020

@author: huangxiaoyi
"""

import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-5,5,100)
T_pdf_4 = st.t(4).pdf(X)
T_pdf = st.t(1).pdf(X)
Norm = st.norm(0,1).pdf(X)

fig, ax = plt.subplots()
ax.plot(X,T_pdf,label = 'deg=1')
ax.plot(X,T_pdf_4,label = 'deg=4')
ax.plot(X,Norm,label = 'Normal')
legend = plt.legend(loc='upper right', shadow=True)

T_cdf_4 = st.t(4).cdf(X)
T_cdf = st.t(1).cdf(X)
Normc = st.norm(0,1).cdf(X)

fig, bx = plt.subplots()
bx.plot(X,T_cdf,label = 'deg=1')
bx.plot(X,T_cdf_4,label = 'deg=4')
bx.plot(X,Normc,label = 'Normal')
legend = plt.legend(loc='upper right', shadow=True)