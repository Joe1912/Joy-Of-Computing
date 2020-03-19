# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:21:43 2020

@author: Joe
"""

size=int(input())
arr=[]
for i in range(size):
    
    arr.append(list(map(int,input().split())))
 
for i in range(size):
    for j in range(size):
        if(j<=i):
            print(arr[i][j],end=" ")
        elif(j==size-1):
            print(0)
        else:
          	print(0,end=" ")
   