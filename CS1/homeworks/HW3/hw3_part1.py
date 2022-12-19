# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 06:22:53 2022

@author: puniaa
"""
'''
This program takes a paragraph that the user wrote and tell us different things about it. 
For example: the average sentence length, percentage of hard words, appends hard words into a list, 
average number of syllables, two different readiability index scores. 
'''
from syllables import find_num_syllables

x = input('Enter a paragraph => ')
print(x)
word = x.split() #y
sentence = x.split('.') #z

#returns average sentence length
asl = len(word) / (len(sentence)-1)
#returns percentage of hard words
def find_phw(word):
    i = 0
    a = 0
    while i <= (len(word)-1):
        if '-' not in word[i] and not word[i].endswith('es') and not word[i].endswith('ed') and 3 <= find_num_syllables(word[i]):
            a += 1
        i += 1
    return (a / len(word))*100
#appends hard words into a list
def find_phw2(word):
    i = 0
    a = []
    while i <= (len(word)-1):
        if '-' not in word[i] and not word[i].endswith('es') and not word[i].endswith('ed') and 3 <= find_num_syllables(word[i]):
            a.append(word[i])
        i += 1
    return a
#returns computes the average number of syllables
def find_asyl(word):
    i = 0
    a = 0
    while i <= (len(word)-1):
        a += find_num_syllables(word[i])
        i += 1
    return a/len(word)
#readability index score (Gunning-Fog)
gfri = 0.4*(asl +find_phw(word))
#readability index score (Flesch Kincaid)
fkri = 206.835-1.015 * asl - 86.4 * find_asyl(word)

#print statements to print the info above
print('Here are the hard words in this paragraph:\n',find_phw2(word),sep='')
print('Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}\r'.format(asl,find_phw(word),find_asyl(word)))
print('Readability index (GFRI): {:.2f}\r'.format(gfri))
print('Readability index (FKRI): {:.2f}\r'.format(fkri))



