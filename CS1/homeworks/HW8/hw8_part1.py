# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:49:47 2022

@author: puniaa
"""
import json
from berryfieldclass import *
from bearclass import *
from touristclass import *
#main file - part 1 
'''
f = input("Enter the json file name for the simulation => ")
print(f)
'''
f = open("bears_and_berries_1.json")
#f = open(f)
data = json.loads(f.read())
'''
print(data["berry_field"])
print(data["active_bears"])
print(data["reserve_bears"])
print(data["active_tourists"])
print(data["reserve_tourists"])

print()
bf = BerryField(data["berry_field"],data["active_bears"],data["active_tourists"])
print(bf)

print("Active Bears:")
b = Bear(data["active_bears"])
print(b)
print("Active Tourists:")
t = Tourist(data["active_tourists"])
print(t)
'''
print()
bf = BerryField(data["berry_field"],data["active_bears"],data["active_tourists"])
print(bf)
print("Active Bears:")
bearlist = []
for bear in data["active_bears"]:
    b = Bear(bear[0],bear[1],bear[2])
    bearlist.append(b)
    print(b)
print()
print("Active Tourists:")
touristlist = []
for tourist in data["active_tourists"]:
    t = Tourist(tourist[0],tourist[1])
    touristlist.append(t)
    print(t)












