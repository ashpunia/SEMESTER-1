# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 11:52:30 2022

@author: puniaa
"""

import hw5_util
#getting the nrbs
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

#getting steepest path
def steepest_path(start, max_step,grid):
    curr_pos = start
    path = [start]
    while True:
        nrbs = get_nrbs(curr_pos[0],curr_pos[1], numbr, numbc)
        qualified_nrbs = []
        for i in  nrbs: 
            if int(grid[i[0]][i[1]]) - int(grid[curr_pos[0]][curr_pos[1]]) <= int(max_step):
                if grid[i[0]][i[1]] > grid[curr_pos[0]][curr_pos[1]]:
                    qualified_nrbs.append(i)
                        
        max_neigh = (-1,-1)
        max_val = 0
        for n in qualified_nrbs:
            if grid[n[0]][n[1]] > max_val:
                max_val = grid[n[0]][n[1]]
                max_neigh = n
        if max_neigh == (-1,-1):
            return path
        else:
            path.append(max_neigh)
            curr_pos = max_neigh
# getting gradual    
def gradual_path(start, max_step,grid):
    curr_pos = start
    path = [start]
    while True:
        nrbs = get_nrbs(curr_pos[0],curr_pos[1], numbr, numbc)
        qualified_nrbs = []
        for i in  nrbs: 
            if int(grid[i[0]][i[1]]) - int(grid[curr_pos[0]][curr_pos[1]]) <= int(max_step):
                if grid[i[0]][i[1]] > grid[curr_pos[0]][curr_pos[1]]:
                    qualified_nrbs.append(i)
                        
        max_neigh = (-1,-1)
        max_val = global_max + 1
        for n in qualified_nrbs:
            if grid[n[0]][n[1]] < max_val:
                max_val = grid[n[0]][n[1]]
                max_neigh = n
        if max_neigh == (-1,-1):
            return path
        else:
            path.append(max_neigh)
            curr_pos = max_neigh
        

if __name__ == "__main__":
    #print statements
    gindex = int(input("Enter a grid index less than or equal to 3 (0 to end): "))
    print(gindex)
    max_step = input("Enter the maximum step height: ")
    print(max_step)
    print_ask = input("Should the path grid be printed (Y or N): ")
    print(print_ask)
    grid = hw5_util.get_grid(gindex)
    numbc = len(grid[0])
    numbr = len(grid)
    if print_ask == "y" or print_ask == "Y":
        print("Grid has {} rows and {} columns".format(numbr,numbc))
    startloc =  hw5_util.get_start_locations(gindex)

    ##global max##
    row = 0 
    col = 0 
    global_max = 0
    for i in range(len(grid)):
        for x in range(len(grid[0])):
            if global_max < grid[i][x]:
                row = i 
                col = x
                global_max = grid[i][x]
    print("global max: ({0}, {1}) {2}".format(row,col,global_max))
     ##end global max## 
     #grid
    cgrid = []
    for i in range(len(grid)):
        cgrid.append([])
        for j in range(len(grid[i])):
            cgrid[i].append(0)
            
    #printing thw paths and the max/kind of paths        
    for start in startloc:
        cgrid[start[0]][start[1]] +=1
        steep = steepest_path(start, max_step,grid)
        if grid[steep[-1][0]][steep[-1][1]] == global_max:
            #print("===")
            print("===\nsteepest path")
            print(steep)
            print("global maximum")
            print("...")
            
        else:
            print("===")
            print(steep)
            print("no maximum")
            print("...")
        
        gradual = gradual_path(start, max_step, grid)
        print("most gradual path")
        print(gradual)
        print("...")
        # calculate the local maximum of the final location gradual[-1]
        # get the nrbs of gradual[]
        
        '''
        for i in range(len(path)):
            print(path[i], end = " ")
            if i % 4 and i != 0:
                print()
        print()
        '''    
            
   
print('==\nPath Grid')
for r in cgrid:
    for i in r:
        if i == 0: 
            print(" .", end = "" )
        else: 
            print(" "+ str(i), end = "")
    print()