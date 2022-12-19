# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:11:08 2022

@author: puniaa
"""
co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]
    
x = input("Enter the fraction: ")
print(x)
x = float(x)

for a in range(len(co2_levels)):
    co2_levels[a] = co2_levels[a]*(1+x)
    
print('First: {:.2f}'.format(co2_levels[0]))
print('Last: {:.2f}'.format(co2_levels[-1]))
    
