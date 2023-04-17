# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:48:50 2022

@author: rayya
"""

estimates=[10,9,8,7,6,5,4,3,2,1,0]
estimates.sort()

tv=int(0.1*len(estimates))
estimates=estimates[tv:]

for i in range(len(estimates)):
    print(estimates[i])

print(" ")

estimates=estimates[:len(estimates)-tv]
for i in range(len(estimates)):
    print(estimates[i])

