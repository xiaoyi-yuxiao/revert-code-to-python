#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:59:53 2020

@author: huangxiaoyi
"""

import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,5,1000)
F_pdf_5 = st.f(5,5).pdf(X)
F_pdf_10 = st.f(10,10).pdf(X)
F_pdf_30 = st.f(30,30).pdf(X)

fig, ax = plt.subplots()
ax.plot(X,F_pdf_5,label = 'deg=5')
ax.plot(X,F_pdf_10,label = 'deg=10')
ax.plot(X,F_pdf_30,label = 'deg=30')
legend = plt.legend(loc='upper right', shadow=True)

F_cdf_5 = st.f(5,5).cdf(X)
F_cdf_10 = st.f(10,10).cdf(X)
F_cdf_30 = st.f(30,30).cdf(X)

fig, bx = plt.subplots()
bx.plot(X,F_cdf_5,label = 'deg=5')
bx.plot(X,F_cdf_10,label = 'deg=10')
bx.plot(X,F_cdf_30,label = 'deg=30')
legend = plt.legend(loc='upper right', shadow=True)