# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:59:41 2020

@author: Joe
"""

def is_prime(ar):
    if(ar==1):
        return False
    for i in range(2,ar):
        if(ar%i==0):
            return False
    return True


def is_semi_prime(br):
    for i in range(2,br):
        if(br%i==0):
            j=br//i
            if(is_prime(i) and is_prime(j) and i!=j):
                return True
    return False
                
            
N=int(input())
for i in range(2,N+1):
    if(is_semi_prime(i) and is_semi_prime(N-i)):
        print("Yes",end="")
        exit()
print("No",end="")