# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 02:14:58 2022

@author: puniaa
"""


def add(m,n):
    print(m,n)
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1
    
print(add(5,3))

def mult(m,n):
    print(m,n)
    if m == 1:
        return n
    return add(n,mult(m-1,n))
    if n == 0:
        return 0
    
print(mult(8,3))

def power(x,n):
    print(x,n)
    if n == 0:
        return 1
    return mult(x, power(x,n-1))

#print(power(6,3)) 
print(power(6,4))
