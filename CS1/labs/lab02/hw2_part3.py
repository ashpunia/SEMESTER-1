# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:32:59 2022

@author: puniaa
"""

x = input("Enter a sentence ==>")
print(x)
def number_happy(x):
    y= x.lower()
    count = y.count("laugh")
    count1 = y.count("happiness")
    count2 = y.count("love")
    count3 = y.count("excellent")
    count4 = y.count("good")
    count5 = y.count("smile")
    allcount = count+count1+count2+count3+count4+count5
    return allcount

def number_sad(x):
    y = x.lower()
    count = y.count("bad")
    count1 = y.count("sad")
    count2 = y.count("horrible")
    count3 = y.count("terrible")
    count4 = y.count("problem")
    count5 = y.count("hate")
    allcount = count+count1+count2+count3+count4+count5
    return allcount

numbplus = number_happy(x)
numbminus = number_sad(x)

print("+"*numbplus,"-"*numbminus)

if numbplus > numbminus:
    print("This is a happy sentence")
elif numbminus > numbplus:
     print("This is a sad sentence")
else: 
    print("This is a neutral sentence")


