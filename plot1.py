# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:23:48 2022

@author: rayya
"""
import statistics
import matplotlib.pyplot as plt
estimates=[10,9,8,7,6,5,4,3,2,1,0]
y=[]

estimates.sort()
tv=int(0.1*(len(estimates)))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
for i in range(len(estimates)):
    y.append(5)
plt.plot(estimates,y,'r--')
plt.plot([statistics.mean(estimates)],[5],'ro')
#plt.plot([statistics.median(estimates)],[5],'bs')
plt.plot([4],[5],'bs')
plt.plot([6],[5],'g^')

