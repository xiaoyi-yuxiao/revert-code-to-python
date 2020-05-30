#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:06:55 2020

@author: huangxiaoyi
"""

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,4,1000)
E_pdf_1 = np.exp(-1*X)
E_pdf_2 = 2*np.exp(-2*X)
E_pdf_3 = 3*np.exp(-3*X)

fig, ax = plt.subplots()
ax.plot(X,E_pdf_1,label = 'deg=1')
ax.plot(X,E_pdf_2,label = 'deg=2')
ax.plot(X,E_pdf_3,label = 'deg=3')
legend = plt.legend(loc='upper right', shadow=True)

E_cdf_1 = 1-np.exp(-1*X)
E_cdf_2 = 1-np.exp(-2*X)
E_cdf_3 = 1-np.exp(-3*X)

fig, bx = plt.subplots()
bx.plot(X,E_cdf_1,label = 'deg=1')
bx.plot(X,E_cdf_2,label = 'deg=2')
bx.plot(X,E_cdf_3,label = 'deg=3')
legend = plt.legend(loc='upper right', shadow=True)