# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:06:19 2022

@author: rayyan
"""

import random
year=random.randint(1993,2022)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("given year is a leap year")
else:
    print("given year is not a leap year")
    
