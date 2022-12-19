# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:38:01 2022

@author: puniaa
"""


def get_words(filename):
    f = open(filename)
    line = f.read()
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
    print(len(result))
    return result
filename1 = input("Enter the filename: ")
print(filename1)
s1 = get_words(filename1)
filename2 = input("Enter the filename: ")
print(filename2)
s2 = get_words(filename2)
print()
print("Same words:", s1.intersection(s2))
print()
print("Unique to",filename1,s1.difference(s2))
print()
print("Unique to",filename2,s2.difference(s1))