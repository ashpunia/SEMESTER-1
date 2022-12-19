# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:34:05 2022

@author: puniaa
"""
'''
This program computes a population balance between Bears, Berries and Tourists. 
'''
import math
#this function will compute new number of tourists and make sure that it doesn't reach less than 0
def num_tourists(bear):
    if bear >= 4 and bear <= 15:
        if bear<=10:
            tourists=bear*10000
        elif bear>10:
            tourists=100000+(bear-10)*20000
    else:
        tourists=0
    return max(0, tourists)

#this function will compute the next population 
def find_next(new_bears, new_berries, new_tour):
    bears_next = new_berries/(50*(new_bears+1)) + new_bears*0.60 - (math.log(1+new_tour,10)*0.1)
    berries_next = (new_berries*1.5) - (new_bears+1)*(new_berries/14) - (math.log(1+new_tour,10)*0.05)
    return max(0, int(bears_next)), max(0, float(berries_next)), max(0, int(new_tour))

#user inputs the numbers of bears and size of berry area
bears = input("Number of bears => ")
print(bears)
bears = int(bears)
berries = input("Size of berry area => ")
print(berries)
berries= float(berries)
print("Year      Bears     Berry     Tourists")

#lists to append to in th while loop
Lbears=[]
Lberry=[]
Ltourist=[]

#appends all the information in a list
i = 1
while i <= 10:
    tourists = num_tourists(bears)
    print(str(i) + ' '*(10-len(str(i))) + str(bears) + ' '*(10-len(str(bears))) +"{:.1f}".format(berries) + ' '*(10-len(str(round(berries, 1)))) + str(tourists) + ' '*(10-len(str(tourists))))
    Lbears.append(bears)
    Lberry.append(berries)
    Ltourist.append(tourists)
    bears, berries, tourists = find_next(bears, berries, tourists)
    i += 1


#print statements for max and min
print()
print("Min:", " "*4, min(Lbears), " "*(8-len(str(min(Lbears)))), "{:.1f}".format(round(min(Lberry),1)), " "*(8-len(str(round(round(min(Lberry),1),1)))), min(Ltourist), " "*(8-len(str(min(Ltourist)))))
print("Max:", " "*4, max(Lbears), " "*(8-len(str(max(Lbears)))), "{:.1f}".format(round(max(Lberry),1)), " "*(8-len(str(round(round(max(Lberry),1),1)))), max(Ltourist), " "*(8-len(str(max(Ltourist)))))