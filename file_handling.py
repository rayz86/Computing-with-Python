# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:09:40 2022

@author: rayya
"""

with open("file1.txt","r+") as myfile:
    print (myfile.read())
    myfile.write("i am fine")
myfile.close()