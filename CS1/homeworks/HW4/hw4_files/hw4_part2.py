# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 01:00:11 2022

@author: puniaa
"""

import hw4_util

def compute_daily(index,abv):
    global avg 
    avg = 0
    weeks = hw4_util.part2_get_week(index)
    for state in weeks: 
        if state[0] == abv:
            pos = 0
            for num in range(2,9):
                pos = pos + state[num]
            daily_avg = pos/7
            avg = daily_avg * 100000 / state[1]
            return round(avg,1)   
    return "not found"
    
def compute_pct(index,abv):
    global avg 
    avg = 0
    weeks = hw4_util.part2_get_week(index)
    for state in weeks: 
        if state[0] == abv:
            avg_list=[]
            new_list=[]
            for a in range(2,9):
                avg_list.append(state[a])
            for b in range(2,16):
                new_list.append(state[b])
            avg = (sum(avg_list)/sum(new_list))* 100
            return round(avg,1)
    return "not found"
checker = 2
while checker == 2:
    print("...")
    index = int(input("Please enter the index for a week: "))
    print(index)
    if index < 0:
        break
    if index > 29:
        print("No data for that week")
        checker = 2
    else: 
        request = input("Request (daily, pct, quar, high): ")
        print(request)
        request = request.lower()
        if request == "daily":
            abv = input("Enter the state: ")
            print(abv)
            if compute_daily(index,abv) == "not found":
                print("State",abv,"not found")
            else:
                print("Average daily positives per 100K population:",round(avg,1))
        if request == "pct":
            abv = input("Enter the state: ")
            print(abv)
            if compute_pct(index,abv) == "not found":
                print("State",abv,"not found")
            else:
                print("Average daily positive percent:",compute_pct(index,abv))
        if request == "quar":
            List = []
            week = hw4_util.part2_get_week(index)
            for a in range(len(week)):
                temp_daily = compute_daily(index,week[a][0])
                temp_pct = compute_pct(index,week[a][0])
                if temp_daily > 10 or temp_pct > 10:
                    List.append(week[a][0])
            print("Quarantine states:")
            print(hw4_util.print_abbreviations(List))
    
        if request == "high":
            max_daily = 0 
            max_index = 0
            weeks = hw4_util.part2_get_week(index)
            for state in range(len(weeks)): 
                state_daily = compute_daily(index,weeks[state][0])
                if state_daily > max_daily:
                    max_daily = state_daily
                    max_index = state
            print("State with highest infection rate is",weeks[max_index][0])
            print("Rate is", max_daily, "per 100,000 people") 
        if request != "high" and request != "quar" and request != "daily" and request != "pct":
            print("Unrecognized request")
            
        