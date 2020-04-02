# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 21:56:54 2020

@author: Joe
Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.

"""
N=input()
if(len(N)>=2):    
    print(N[0:2]+N[len(N)-2:],end="")
else:
    print("",end="")