#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:42:43 2020

@author: huangxiaoyi
"""
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
Data=yf.download("AAPL",start="2014-12-16",end="2020-4-30")
Adjclose=Data['Adj Close']
R=Adjclose.pct_change()[1:]#this is a builtin function to calculate the return

fig = plt.figure()

ax1 = fig.add_subplot(111)
(counts, bins, patch)=ax1.hist(R, bins=20) #counts is to count how many elements are there in one bin 
ax1.set_xlabel('Return')
ax1.set_ylabel('Frequency')
ax1.legend(['AAPL Returns'])
ax2 = ax1.twinx()  # this is the important function because it does not require you to use subplot to make another axis
pct_counts = counts/sum(counts)
Cum_sum = np.cumsum(pct_counts)# i used a cumsum function in np lib to calculate the cumulative summation
ax2.plot(bins[1:],Cum_sum,'r')
ax2.set_ylim([0, 1])
ax2.set_ylabel('cumpct change')

plt.show()
