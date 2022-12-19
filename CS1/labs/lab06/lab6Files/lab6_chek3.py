# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:43:12 2022

@author: puniaa
"""
import lab06_util
'''
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
'''
print(len(bd))
print(len(bd[0]))
print(bd[0][0])
print(bd[8][8])
'''
filename = input("Enter file name:")

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

def verify_board(bd):
    for i in range(len(bd)):
        for j in range(len(bd)):
            if bd[row][col] == ".":
                return False
            if okay_to_add(j,i,int(bd[i][j]))==False:
                print(i,j,bd[i][j])
                return False
    return True

bd = lab06_util.read_sudoku(filename)

while verify_board(bd) == False:
    row = int(input("Enter the value for the row: "))
    col = int(input("Enter the value for the col: "))
    numb = int(input("Enter the value for the numb: "))
#printing the entire board
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

  
      