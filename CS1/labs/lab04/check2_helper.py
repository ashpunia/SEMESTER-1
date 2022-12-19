# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:50:26 2022

@author: puniaa
"""

from PIL import Image 


def make_square(image): 
    width = image.width
    height = image.height
    cropped_image = image.crop((0,0,min(width,height),min(width,height)))
    return cropped_image
    
image = Image.open("im.jpg")
imsquare = make_square(image)
imsquare.show()  

