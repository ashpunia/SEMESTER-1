# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:18:48 2022

@author: puniaa

Description of overall program
"""

'''
Import Statements
'''

import math

'''
Function Definitions
'''

def find_volume_sphere(radius):
    return (4*math.pi*radius**3)/3

def find_volume_cube(side):
    return (side)**3

'''
Main Body
'''
 
radius = (input ("Enter the gum ball radius (in.) => ".strip("\r")))
print (radius)
radius = float(radius)
weekly_sales = int(input("Enter the weekly sales => ".strip("\r")))
print (weekly_sales)
print("")
def calc_gumball(weekly_sales):
    return 1.25*weekly_sales
totalgumball = calc_gumball(weekly_sales)
dimensiongumball = math.ceil(totalgumball**(1/3))
def calc_side(gumball, radius):
    return math.ceil(gumball)*radius*2
side = calc_side (dimensiongumball, radius)
def calc_gumbfit(dim, radius):
    return dim/2*radius
volcube = find_volume_cube(side)
volgb = find_volume_sphere(radius)
volallgb = math.ceil(totalgumball)*volgb
def wasted_space(volcube, volgb):
    return volcube - (volgb)
extragb = int(dimensiongumball**3 - calc_gumball(weekly_sales))
wastedspacews = volcube - (volgb*math.ceil(calc_gumball(weekly_sales)))
wastedspacegbfit = volcube - (volgb*(dimensiongumball**3))
print("The machine needs to hold".strip("\r"), math.ceil (dimensiongumball), "gum balls along each edge.".strip("\r"))
print("Total edge length is {:.2f} inches.".strip("\r").format(side))
print("Target sales were ".strip("\r")+ str(math.ceil(totalgumball))+", but the machine will hold".strip("\r"), extragb,
"extra gum balls.".strip("\r"))
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,".strip("\r").format(wastedspacews))
print("or {:.2f} cubic inches if you fill up the machine.".strip("\r").format(wastedspacegbfit))

