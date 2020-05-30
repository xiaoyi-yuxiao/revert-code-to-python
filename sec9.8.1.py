#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:24:37 2020

@author: huangxiaoyi
"""

import numpy as np
import matplotlib.pyplot as plt

N=1000

def PsudoRand(beta,N,size,number_of_sample):
    psudo = np.random.exponential(1/beta,N)#generate a thousand unidform random number from uniform distribution
    choice = np.random.choice(psudo, (size,number_of_sample))#choose 5 number from Rsudo without replacement
    return choice

def Plot(sample,num):
    fig, ax = plt.subplots()
    ax.hist(np.mean(sample,axis=0),bins = 20)
    plt.xlabel('mean')
    plt.ylabel('frequency')
    plt.title('histogram of C%s'%(num))
    
Sample_1 = PsudoRand(1,N,5,300)
Plot(Sample_1,10)

Sample_2 = PsudoRand(1,N,10,300)
Plot(Sample_2,15)

Sample_3 = PsudoRand(1,N,30,300)
Plot(Sample_3,35)

Sample_2 = PsudoRand(1,N,50,300)
Plot(Sample_2,55)

