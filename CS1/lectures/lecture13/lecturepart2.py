# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 23:45:28 2022

@author: puniaa
"""

inputfile = input("Enter the input file name: ")
outputfile = input("enter the output file name: ")

fin = open(inputfile, "r")
fout = open(outputfile, "w")

score = list()

for line in fin:
    score.append(int(line))
    
n = len(score)

for i in range(n-1):
    for j in range(len(score) - i -1):
        if score[j] > score[j+1]:
            temp = score[j]
            score[j] = score[j+1]
            score[j+1] = temp
        
for i in range(len(score)):
    fout.write("%2d: %3\n" %(i,score[i]))

fin.close()
fout.close()
        
