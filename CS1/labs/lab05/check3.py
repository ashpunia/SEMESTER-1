# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:59:51 2022

@author: puniaa
"""

import lab05_util
import webbrowser

restaurants = lab05_util.read_yelp("yelp.txt")
ID = (input("ID => "))
ID = int(ID) - 1
print(ID)


def print_info(restaurants): 
    print(restaurants[0])
    nameRes = restaurants[0]
    cuisine = restaurants[-2]
    address = restaurants[3].split("+")
    if len(restaurants[-1]) >= 3 :
        avg = sum(restaurants[-1])/len(restaurants[-1])
    else: 
        Min = min(restaurants[-1])
        Max = max(restaurants[-1])
        Sum = sum(restaurants[-1]) - Min - Max
        avg = Sum/len(restaurants[-1])
        
    print(nameRes, "(" + cuisine + ")")
    for i in range(len(address)):
        print("\t" , address[i])
    print("Average Score:",round(avg,2))

    if avg >= 0 and avg < 2:
        print("The restaurant is rated bad, based on",
              len(restaurants[-1]), "reviews")
    if avg >= 2 and avg < 3:
        print("The restaurant is rated average, based on",
              len(restaurants[-1]), "reviews")
    if avg >= 3 and avg < 4:
        print("The restaurant is rated obove average, based on",
              len(restaurants[-1]), "reviews")
    if avg >= 4 and avg < 5:
        print("The restaurant is rated very good, based on",
              len(restaurants[-1]), "reviews")


if ID < 1 or ID > len(restaurants):
    print("Warning")
else:
    print_info(restaurants[ID])
# check 3

print("What would you like to do next?")
print("1. Visit the homepage")
print("2. Show on google maps")
print("3. Show directions to this restaurant")
UserInput = int(input("Your choice (1-3)? ==> "))
UserRestaurants = restaurants[ID]
if UserInput == 1:
    url = UserRestaurants[4]
    webbrowser.open(url)
elif UserInput == 2:
    webbrowser.open('http://www.google.com/maps/place/'+UserRestaurants[3])
elif UserInput == 3:
    webbrowser.open(
        'http://www.google.com/maps/dir/110 8th Street Troy NY/'+UserRestaurants[3])
