# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 22:14:54 2020

@author: Joe
"""

N=int(input())
a=[]
inp=map(int,input().split())
for i in inp:
    a.append(i)
k=int(input())
b=sorted(a)
for i in range(len(b)):
    if(b[i]==a[k-1]):
        print(i+1,end="")
        break;
