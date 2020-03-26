# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:33:21 2020

@author: Joe
"""

s=input()
s=s.lower()
d={}
for i in s:
    if (i.isalpha()):
        d[i]="Present"
if(len(d.keys())==26):
    print("YES",end="")
else:
    print("NO",end="")
