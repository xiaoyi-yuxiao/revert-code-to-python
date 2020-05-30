#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 20:44:08 2020

@author: huangxiaoyi
"""

import numpy as np
import matplotlib.pyplot as plt

##define the calculation
def Uniformd(a,b,range_):
    listc = np.linspace(0,range_,500)
    listd = np.zeros([500,1])
    for i in range(len(listc)):
        if listc[i]>a and listc[i]<b:
            listd[i] = 1/(b-a)
    plt.plot(listc,listd)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    

Uniformd(2,7,10)
