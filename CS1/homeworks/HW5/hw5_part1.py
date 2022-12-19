# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:58:36 2022

@author: puniaa
"""

import hw5_util

#getting neighbors
def get_nrbs(r,c, numbr, numbc):
    n1 = (r-1,c) 
    n2 = (r,c-1)
    n3 = (r,c+1)
    n4 = (r+1,c)
    nrbs = [n1,n2,n3,n4]
    delete = []
    for i in nrbs: 
        if i[0] >= numbr or i[1] >= numbc or i[0] < 0 or i[1] <0:
            delete.append(i)
    for i in delete: 
        nrbs.remove(i)
    return nrbs

#checking if the path is valid
def is_valid(path): 
    i = 0
    while i < len(path)-1:
        nrbs = get_nrbs(path[i][0],path[i][1],numbr,numbc) 
        j = 0
        while j < len(nrbs):
            if nrbs[j][0] == path[i+1][0] and nrbs[j][1] == path[i+1][1]:
                break
            j+=1
            if j == len(nrbs):
                return False
        i+=1
    return True

if __name__ == "__main__":
    n = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
    print(n)
    choice = input("Should the grid be printed (Y or N): ")
    print(choice)
    if choice.lower() == "y":
        print("Grid", n)
        for lists in hw5_util.get_grid(n):
               for List in lists:
                   print("{:4d}".format(List),end = "")
                   numbc = len(lists)
               print()
    #getting my numbr and numbc
    for lists in hw5_util.get_grid(n):
        numbc = len(lists)
    numbr = len(hw5_util.get_grid(n))
    
    print("Grid has {} rows and {} columns".format(numbr,numbc))
    startloc =  hw5_util.get_start_locations(n)
    #printing neighbors
    for start in startloc:
       nrbs = (get_nrbs(start[0],start[1],numbr,numbc))
       print("Neighbors of " + str(start) + ":", end="")
       for x in nrbs:
           print(" " + str(x), end="")
       print()
    
    path = hw5_util.get_path(n) 
    
    #printing valid paths
    if is_valid(path) == True:
        print("Valid path")
        
        i=0
        down= 0
        up = 0
        while i < len(path)-1:
            diff = hw5_util.get_grid(n)[path[i+1][0]][path[i+1][1]] - hw5_util.get_grid(n)[path[i][0]][path[i][1]]
            
            if diff < 0:
                down = abs(diff) + down
            if diff > 0:
                up = diff + up
            i+=1
    
        print("Downward",down)
        print("Upward",up)
    
    elif is_valid(path) == False:
        print("Path: invalid step from (2, 4) to (3, 3)")



