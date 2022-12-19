# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 12:24:01 2022

@author: puniaa
"""

def get_words(line):
    line = line.split("|")
    line = line[1]
    line = line.replace(".","")
    line = line.replace(",","")
    line = line.replace("()","")
    line = line.replace("(","")
    line = line.replace(")","")
    line = line.replace("",'')
    line = line.lower()
    line=line.split()
    s = set()
    for word in line :
        if len(word) >=4 and word.isalpha():
            s.add(word)
    result = s 
    #print(len(result))
    return result

filename1 = input("Enter the filename: ")
print(filename1)
f = open(filename1)
line1 = f.read()
s1 = get_words(line1)

filename2 = "allclubs.txt"
f2 = open(filename2)
simlist = []
for clubs in f2: 
    s2 = get_words(clubs)
    clubs = clubs.split("|")
    #print(s1.intersection(s2))
    simlist.append((str(len(s1.intersection(s2))),clubs[0]))
simlist.sort(reverse = True)
print(simlist[0:6])

'''
print()
print("Same words:", s1.intersection(s2))
print()
print("Unique to",filename1,s1.difference(s2))
print()
print("Unique to",filename2,s2.difference(s1))
'''