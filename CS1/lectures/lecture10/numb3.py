# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 12:35:21 2022

@author: puniaa
"""

co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
    
total = 0 
for levels in co2_levels:
    total = total + levels
    average = total/len(co2_levels)

print("Average: {:.2f}".format(average))


count = 0 
for levels in co2_levels:
    if levels > average:
            count+=1
            
print("Num above average:", count)
    
    
    