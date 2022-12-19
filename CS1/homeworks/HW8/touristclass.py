# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 22:24:46 2022

@author: puniaa
"""

#Tourist Class
class Tourist(object):
    
    def __init__(self,row,col):
        self.row = row
        self.col = col
#printing the conditions
    def __str__(self):
        string = "Tourist at ({},{}), 0 turns without seeing a bear.".format(self.row,self.col)
        return string
    #returning position
    def position(self):
        position = (self.row,self.col)
        return position