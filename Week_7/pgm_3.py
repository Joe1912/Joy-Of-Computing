# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:54:51 2020

@author: Joe
"""

N,M=map(int,input().split())
arr=[]
flag=True
for i in range(N):
    arr.append(list(map(int,input().split())))
for i in range(N):
    for j in range(M):
        if(arr[i][j]!=0 and arr[i][j]!=1):
            flag=False
            break
if(flag==True):
    print("YES",end="")
else:
    print("NO",end="")
