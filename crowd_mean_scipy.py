# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:03:09 2022

@author: rayya
"""
from statistics import mean
estimates=[10,9,8,7,6,5,4,3,2,1,0]
estimates.sort()

tv=int(0.1*len(estimates))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]

print (mean(estimates))

#or use this

from scipy import stats

estimates=[10,9,8,7,6,5,4,3,2,1,0]
estimates.sort()
m=stats.trim_mean(estimates,0.1)
print(m)