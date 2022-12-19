# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:56:07 2022

@author: puniaa
"""
import hw4_util

def find_lengthstrength(password):
    score1 = 0
    if len(password) == 7 or len(password) == 6:
        score1 = score1 + 1 
    if len(password) >= 8 and len(password) <= 10:
        score1 = score1 + 2
    if len(password) > 10: 
        score1 = score1 + 3
    return score1

def case(password):
    score2 = 0
    upper = 0 
    lower = 0
    for letter in password: 
        if letter.isupper():
            upper = upper +1 
        if letter.islower():
            lower = lower+1
    
    if upper >= 2 and lower >= 2:
        score2  = score2 +2
    elif (upper == 1 and lower >= 1) or (upper >= 1 and lower == 1):
        score2 = score2 +1
    return score2

def digits(password): 
    score3 = 0
    digit = 0 
    for char in password: 
        if char.isdigit():
            digit = digit + 1
    if digit >= 2: 
        score3 +=2
    if digit == 1:
        score3 +=1
    return score3

def puntuation(password):
    score4 = 0
    for char in password: 
        if char == "!" or char == "@" or char == "#" or char == "$":
            score4 +=1
        if char == "%" or char == "^" or char == "&" or char == "*":
            score4 +=1
    return score4 

def nylicense(password):
    pass
def common_password(password):
    pass 

UserPassword = input("What's you password: ")
print(find_lengthstrength(UserPassword))
print(case(UserPassword))
print(digits(UserPassword))
print(puntuation(UserPassword))
print(hw4_util.part1_get_top())

score = find_lengthstrength(UserPassword)+case(UserPassword)+digits(UserPassword)+puntuation(UserPassword)
print(score)



            


    
    
        