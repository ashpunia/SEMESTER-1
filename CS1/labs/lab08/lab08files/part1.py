# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:33:34 2022

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

filename = input("Enter the filename: ")
print(filename)
print(get_words(filename))
    