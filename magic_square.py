# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:16:43 2022

@author: rayyan
"""

def magic_square(n):
    
    magicSquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
    i=n//2
    j=n-1
    
    num=n*n
    count=1
    
    while(count<=num):
        if(i==-1 and j==n):
            j=n-2
            i=0
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[i][j]=count
            count+=1
            
        i=i-1
        j=j+1
        
        for i in range(n):
            for j in range(n):
             print(magicSquare[i][j],end=" ")
        print()
         
magic_square(3)
        