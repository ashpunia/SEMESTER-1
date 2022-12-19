# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:38:51 2022

@author: puniaa
"""

hd = int(input("Enter Dale's height: "))
print(hd)
he = int(input("Enter Erin's height: "))
print(he)
hs = int(input("Enter Sam's height: "))
print(hs)

if (hd >= he):
    if (hd >= hs):
        if (he >= hs):
            print("Dale")
            print("Erin")
            print("Sam")
        else: 
            print("Dale")
            print("Sam")
            print("Erin")
    elif (he >= hs):
        print("Erin")
        print("Sam")   
        print("Dale")
    else: 
        print("Sam")
        print("Dale")
        print("Erin")
elif (hd >= hs):
    if(he >= hs):
        print("Erin")
        print("Dale")
        print("Sam") 
    else: 
        print("Sam")
        print("Erin")
        print("Dale")
elif (he >= hs): 
    print("Erin")
    print("Sam")
    print("Dale")
else: 
    print("Sam")
    print("Erin")
    print("Dale")
        