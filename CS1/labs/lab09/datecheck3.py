# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:23:24 2022

@author: puniaa
"""

from datepart2 import Date
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

datelist = []
def birthday():
    f = open("birthdays.txt")
    line = f.read()
    line = line.split("\n")
    line.pop(-1)
    datelist = []
    for l in line:
        olist = l.split(" ")
        d = Date(olist[0],olist[1],olist[2])
        datelist.append(d)
    return datelist
List = birthday()
print(max(List))
print(min(List))
monthlist = []
for i in List:
    #print(i)
    monthlist.append(i.month)
#print(monthlist)

frequency = {}
for item in monthlist:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
#print(frequency)

List1 = []
for key in frequency:
    value = frequency[key]
    List1.append(value) 
    Max1 = max(List1)
for i in frequency: 
    if frequency[i] == Max1:
        i = int(i)
        print(month_names[i])
        
        
    


    
    


