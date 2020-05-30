#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 20:44:08 2020

@author: huangxiaoyi
"""

import numpy as np
import matplotlib.pyplot as plt

##define the calculation and ploting
def Uniformdcum(a,b,range_):
    listc = np.linspace(0,range_,500)
    listd = np.zeros([500,1])
    for i in range(len(listc)):
        if listc[i]>a and listc[i]<b:
            listd[i] = 1/(b-a)
    listd=np.cumsum(listd)
    return listc, listd#listc is the x-axis, listd is the probability

(X,data2_7) = Uniformdcum(2,7,10)
plt.plot(X,data2_7,'g--', label='2to7')
(X,data1_9) = Uniformdcum(1,9,10)
plt.plot(X,data1_9,'r:', label='1to9')
(X,data3_5) = Uniformdcum(3,5,10)
plt.plot(X,data3_5,'b--', label='3to5')
legend = plt.legend(loc='upper right', shadow=True)
plt.xlabel('x')
plt.ylabel('f(x)')
