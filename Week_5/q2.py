# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:34:28 2020

@author: Joe
"""
arr=list(map(int,input().split()))
count=0
brr=sorted(arr)
for i in range(len(arr)):
    if(arr[i]==brr[count]):
        count=count+1
print(len(arr)-count,end="")