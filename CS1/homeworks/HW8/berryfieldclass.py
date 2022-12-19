# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 20:10:48 2022

@author: puniaa
"""

#BerryField Class

class BerryField(object):
    def __init__(self,berryfield,bears,tourist):
        self.berryfield = berryfield
        self.bears = bears
        self.tourist = tourist
        
    #printing out stats and the grid
    def __str__(self):  
        string = ""
        count = 0
        for r in range(len(self.berryfield)):
            for c in range(len(self.berryfield[r])):
                count += self.berryfield[r][c] 
        
        string += "Field has {} berries.\n".format(count)
                
        for r in range(len(self.berryfield)):
            for c in range(len(self.berryfield[r])):
                Bear = False
                Tourist = False
                for b in self.bears:
                   if b[0] == r and b[1] == c:
                       Bear = True
                for t in self.tourist:
                    if t[0] == r and t[1] == c:
                        Tourist = True
                if Bear and Tourist:
                    string += "{:>4}".format("X")
                elif Bear:
                    string += "{:>4}".format("B")
                elif Tourist:
                    string += "{:>4}".format("T")
                else:
                    string += "{:>4}".format(self.berryfield[r][c])
            string += "\n"
        return string
    #growing berries based on conditions
    def grow_berries(self):
        for r in range(len(self.berryfield)):
            for c in range(len(self.berryfield[r])):
                if 0 < self.berryfield[r][c] < 10:
                    self.berryfield[r][c] += 1
     #spreasing the berries  
    def spread(self):
        for r in range(len(self.berryfield)):
            for c in range(len(self.berryfield[r])):
                if self.berryfield[r][c] == 0:
                    if r-1 >= 0 :
                        if c-1 >= 0 and self.berryfield[r-1][c-1] == 10:
                            self.berryfield[r][c] = 1
                        elif self.berryfield[r-1][c] == 10:
                            self.berryfield[r][c] = 1
                        elif c+1 < len(self.berryfield) and self.berryfield[r-1][c+1] == 10:
                            self.berryfield[r][c] = 1
                    elif c -1 >= 0 and self.berryfield[r][c-1] == 10:
                        self.berryfield[r][c] = 1
                    elif c +1 < len(self.berryfield) and self.berryfield[r][c+1] == 10:
                        self.berryfield[r][c] = 1   
                    elif r+1 < len(self.berryfield):
                        if c-1 >= 0 and self.berryfield[r+1][c-1] == 10:
                            self.berryfield[r][c] = 1
                        elif self.berryfield[r+1][c] == 10:
                            self.berryfield[r][c] = 1
                        elif c+1 < len(self.berryfield) and self.berryfield[r+1][c+1] == 10:
                            self.berryfield[r][c] = 1
                            
        def move(self):
            bear_count = 0
            nobear_count = 0
            for t in self.tourist:
                tourist_position = (t[0],t[1])
                for b in self.bears:
                    bear_position = (b[0],b[1])
                    if ((t[1]-t[0])**2 + (b[1]-b[0])**2)**0.5 >= 4:
                        bear_count +=1
                    else:
                        nobear_count +=1
                    if bear_count == 3:
                        t.remove(self.tourist)
            
                    

        

     
     