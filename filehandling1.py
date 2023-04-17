# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:43:07 2022

@author: rayya
"""
import random

def evolve(x):
    ind=random.randint(0,len(x)-1)
    p=random.randint(1,100)
    print(p)
    
    if(p==1):
        if(x[ind]=='0'):
            x[ind]=='1'
        else:
            x[ind]=='0'
            
with open("file2.txt") as myfile:
    x=myfile.read()
    x=list(x)
for i in range(0,10000): #10000 is the size of file(bytes)
    evolve(x)
print(x)