# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:01:00 2022

@author: puniaa
"""
import lab05_util
restaurants = lab05_util.read_yelp('yelp.txt') 

def print_info(restaurants):
    print(restaurants[0])
    nameRes = restaurants[0]
    cuisine = restaurants[-2]
    address = restaurants[3].split("+")
    avg = sum(restaurants[-1])/len(restaurants[-1])
    print(nameRes, "(" + cuisine + ")")
    for i in range(len(address)):
        print("\t" , address[i])
    print("Average Score:",round(avg,2))

####### main code starts here
print_info(restaurants[42])
