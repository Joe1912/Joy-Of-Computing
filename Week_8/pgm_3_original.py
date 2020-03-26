# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:57:31 2020

@author: Joe
"""

s=list(input())
m=s
s.append(" ")
vowels="aeiou"
for i in range(len(s)-1):
    if((s[i] in vowels) and (s[i+1] in vowels)):
        m[i]=""
print("".join(m),end="")
