#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:47:18 2020

@author: huangxiaoyi
"""

import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,60,1000)
C_pdf_5 = st.chi2(5).pdf(X)
C_pdf_10 = st.chi2(10).pdf(X)
C_pdf_30 = st.chi2(30).pdf(X)

fig, ax = plt.subplots()
ax.plot(X,C_pdf_5,label = 'deg=5')
ax.plot(X,C_pdf_10,label = 'deg=10')
ax.plot(X,C_pdf_30,label = 'deg=30')
legend = plt.legend(loc='upper right', shadow=True)

T_cdf_5 = st.chi2(5).cdf(X)
T_cdf_10 = st.chi2(10).cdf(X)
T_cdf_30 = st.chi2(30).cdf(X)

fig, bx = plt.subplots()
bx.plot(X,T_cdf_5,label = 'deg=5')
bx.plot(X,T_cdf_10,label = 'deg=10')
bx.plot(X,T_cdf_30,label = 'deg=30')
legend = plt.legend(loc='upper right', shadow=True)