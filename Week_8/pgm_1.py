# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:56:36 2020

@author: Joe
"""

s=input().split()
d={}
for i in s:
    d[i]="This character is present"
for i in d.keys():
    print(i,end=" ")
