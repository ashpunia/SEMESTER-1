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
    for i in range(len(password)): 
        if password[i].isupper():
            upper = upper +1 
        if password[i].islower():
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
            score4=1        
    return score4 

def puntuation2(password): 
    score7 = 0 
    for char in password: 
       if char == "%" or char == "^" or char == "&" or char == "*":
           score7=1
    return score7

def nylicense(password):
    score5 = 0
    if len(password) == 7:
        if password[0].isalpha() == True:
            if password[1].isalpha() == True:
                if password[2].isalpha() == True:
                    if password[3].isdigit() == True:
                        if password[4].isdigit() == True:
                            if password[5].isdigit() == True:
                                if password[6].isdigit() == True:
                                     score5 = score5 - 2
    return score5
            

def common_password(password):
    score6 = 0
    password = password.lower()
    for ele in hw4_util.part1_get_top(): 
        if ele == password: 
            score6 = score6 -3
    return score6
        

UserPassword = input("Enter a password => ")
print(UserPassword)

if find_lengthstrength(UserPassword) > 0: 
    print("Length: +"+str(find_lengthstrength(UserPassword)))
if case(UserPassword) > 0:
    print("Cases: +"+str(case(UserPassword)))
if digits(UserPassword) >0:
    print("Digits: +"+str(digits(UserPassword)))
if puntuation(UserPassword) > 0:
    print("!@#$: +" +str(puntuation(UserPassword)))
if puntuation2(UserPassword) > 0:
    print("%^&*: +" +str(puntuation2(UserPassword)))
if nylicense(UserPassword) < 0:
    print("License: "+str(nylicense(UserPassword)))
if common_password(UserPassword) < 0:
    print("Common: "+str(common_password(UserPassword)))


score = find_lengthstrength(UserPassword)+case(UserPassword)+digits(UserPassword)+puntuation(UserPassword)+nylicense(UserPassword)+common_password(UserPassword)+puntuation2(UserPassword)
print("Combined score:",score)

if score <= 0: 
    print("Password is rejected")
if score == 1 or score == 2: 
    print("Password is poor")
if score == 3 or score == 4: 
    print("Password is fair")
if score == 5 or score == 6: 
    print("Password is good")
if score >= 7:
    print("Password is excellent")


            


    
    
        