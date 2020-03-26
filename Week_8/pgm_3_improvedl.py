# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:24:00 2020

@author: Joe
"""
s=input()
vowels="aeiou"
print(s[0],end="")
for i in range(1,len(s)):
    if(s[i] in vowels and s[i-1] in vowels):
        continue
    else:
        print(s[i],end="")
