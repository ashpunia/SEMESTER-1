# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:44:05 2022

@author: puniaa
"""


bd = [[ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6']]

'''
print(len(bd)) = 9
print(len(bd[0])) = 9
print(bd[0][0]) = 1
print(bd[8][8]) = 6
'''


for row in range(len(bd)):
    if row % 3 ==0:
        print("-"*25)
    for col in range(len(bd)):     
        #print(bd[row]) 
        if col % 3 == 0:
            print("|", end = " ")
        print(bd[row][col], end = " ")        
    print("|")
print("-"*25)


# bd[row][r]) == the entire row

def okay_to_add(numb,row,col):   
   for r in range(len(bd)):
       for c in range(len(bd)):
           if bd[col][c] == numb:
               return False
           elif bd[row][r] == numb:
               return False
           

   R = row - (row % 3)
   C = col - (col % 3)
   for nrow in range(R,R+3):
      for ncol in range(C, C+3): 
          if( bd[nrow][ncol]) == numb:
            return False
    
   return True
 
 

row = int(input("Enter a row: "))
col = int(input("Enter a column: "))
numb = input("What number would you like to input? ")

print(okay_to_add(numb,row,col))

if okay_to_add == True: 
    bd[row][col] == numb
    
    
    
    