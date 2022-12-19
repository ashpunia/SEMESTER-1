# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:36:02 2022

@author: puniaa
"""
line = []
for numb in range(0,9):
    line.append(numb)
print(line)
    
for i in range(0, 9):
    for j in range(0, 9):
        if j == 2 or j == 5:
            print('{},{}'.format(i, j), end = '  ')
        else:
            print('{},{}'.format(i, j), end = ' ')
    if i == 2 or i == 5:
        print('\n')
    else:
        print()


row = input("Enter a row: ")

for j in range(0,9): 
        print('{},{}'.format(row, j), end = ' ')

col = input("Enter a column: ")
for i in range(0,9):
        print('{},{}'.format(i, col), end = ' ')


print("\n")
for i in range(0, 3):
    for j in range(0, 3):
        print('{},{}'.format(i, j), end = ' ')
    if i == 2:
        print("\n")
    else:
        print()