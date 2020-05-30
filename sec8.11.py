#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:03:17 2020

@author: huangxiaoyi
"""

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import anderson

N=1000

def PsudoRand(mu,sigma,N,size,number_of_sample):
    psudo = np.random.lognormal(mu,sigma,N)#generate a thousand unidform random number from uniform distribution
    choice = np.random.choice(psudo, (size,number_of_sample))#choose 5 number from Rsudo without replacement
    return choice

def Plot(sample,num):
    fig, ax = plt.subplots()
    ax.hist(np.mean(sample,axis=0),bins = 20)
    plt.xlabel('mean')
    plt.ylabel('frequency')
    plt.title('histogram of C%s'%(num))
    
Sample_1 = PsudoRand(1,1,N,5,300)
Plot(Sample_1,10)

test = np.mean(Sample_1,axis=0)
qqplot(test, line='s')
print('MLE: mean=%.3f stdv=%.3f' % (np.mean(test), np.std(test)))
result = anderson(test)
print(result)