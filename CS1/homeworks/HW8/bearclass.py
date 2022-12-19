# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 22:24:45 2022

@author: puniaa
"""

#Bear Class

#Bear Class
class Bear(object):
    def __init__(self,row,col,direction):
        self.row = row
        self.col = col
        self.direction = direction
        self.asleep = 0 #how many turns does it have to be asleep for 
        self.berries = 0 #berries eaten in this turn 

        
        
        '''
        N = (row, col - 1)
       S = position = (row, col + 1)
       E = position = (row + 1, col)
       W = position = (row - 1, col)
       NE = position = (row + 1, col - 1)
       NW = position = (row - 1, col - 1)
       SE = position = (row + 1, col + 1)
       SW = position = (row - 1, col + 1)
       '''
        
    def __str__(self):
        string = ""
        string += "Bear at ({},{}) moving {}".format(self.row,self.col,self.direction) 
        return string 
    #moving the bear or at least it's trying its best
    def move(self,bf,tlist):
        # if the bear is sleeping
        if self.asleep > 0:
            self.asleep -= 1
        
        # bear is not sleeping
        elif self.asleep == 0:
        
            position = (self.row,self.col)
            direction = self.direction
            
            berry_eaten = 0
            found = False
            while berry_eaten < 30:
                if (self.row < 0) or (self.row >= 10) or (self.col < 0) or (self.col >= 10):
                    break
                for t in tlist:
                    if position == t.position():
                        # code when the current location of the bear is a tourist
                        self.asleep = 2  
                        found = True
                        break
                if found:
                    break
                #we wanna move and eat the berries
                if berry_eaten < 30:
                    bf.berryfield[position[0]][position[1]] = 0 
                
                    # move to the next position
                    if self.direction == "N":
                        position = (self.row, self.col - 1)  
                    if self.direction == "S":
                        position = (self.row, self.col + 1)
                    if self.direction == "E":
                        position = (self.row + 1, self.col)
                    if self.direction == "W":
                        position = (self.row - 1, self.col)
                    if self.direction == "NE":
                        position = (self.row + 1, self.col - 1)
                    if self.direction == "NW":
                        position = (self.row - 1, self.col - 1)
                    if self.direction == "SE":
                        position = (self.row + 1,self. col + 1)
                    if self.direction == "SW":
                        position = (self.row - 1, self.col + 1)
                    
                # current location of bear is not a tourist
                berries = bf.berryfield[position[0]][position[1]]
                berry_eaten += berries
                break
                if berry_eaten >= 30:
                    extra = berry_eaten - 30
                    bf.berryfield[position[0]][position[1]] = extra
                    break
       
        
        
        