# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 22:31:32 2022

@author: puniaa
"""

file = input("Enter the name of the IMDB file ==> ").strip()
print(file)
count = dict()
for line in open(file,encoding = "ISO-8859-1"):
    words = line.strip().split('/')
    name = words[0].strip()
    if name in count:
        count[name] +=1
    else:
        count[name] = 1
names = sorted(count.values())
for i in count:
    if count[i] == names[len(names)-1]:
        bname = i
        numbt = count[i]
        break
count1 = names.count(1)
print("{} appears more often: {} times".format(bname,numbt))
print("{} people appear once".format(count1))