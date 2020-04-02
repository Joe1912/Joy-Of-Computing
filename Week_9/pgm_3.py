# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:00:45 2020

@author: Joe
Given a square matrix with n rows and n columns, you have to write a program 
to rotate this matrix such that each element is shifted by one place in a clockwise manner.
"""

def Print_Matrix(ar):
    for i in range(len(ar)):
        for j in range(len(ar)-1):
            print(ar[i][j],end=" ")
        print(ar[i][len(ar)-1],end="")
        print("")
    


def Rotate_Matrix(ar):
    
    top=0
    bottom=len(ar)-1    
    left=0
    right=len(ar)-1
    
    while left<right and top<bottom:
        previous=ar[top+1][left]
        
        #top row rotation
        for i in range(left,right+1):
            current=ar[top][i]
            ar[top][i]=previous
            previous=current
        
        top+=1
        
        #right coloumn
        for i in range(top,bottom+1):
            current=ar[i][right]
            ar[i][right]=previous
            previous=current
        right-=1
        
        #bottom coloumn
        
        for i in range(right,left-1,-1):
            current=ar[bottom][i]
            ar[bottom][i]=previous
            previous=current
        bottom-=1
        
        #left coloumn
        for i in range(bottom,top-1,-1):
            current=ar[i][left]
            ar[i][left]=previous
            previous=current
        left+=1
    Print_Matrix(ar)        
        
N=int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
    
Rotate_Matrix(arr)