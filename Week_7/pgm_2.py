# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:49:54 2020

@author: Joe
"""

N=int(input())
arr=[]
flag=True
for i in range(N):
    arr.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if(arr[i][j]!=arr[j][i]):
            flag=False
if (flag==True):
    print("YES",end="")
else:
    print("NO",end="")