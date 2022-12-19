# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:50:25 2022

@author: puniaa
"""


from PIL import Image 

wp = Image.new('RGB', (1060,360),'black')

#ca image
ca = Image.open("ca.jpg")
width = ca.width
height = ca.height
ratio = width/height
ca = ca.resize((int(256*ratio),256))
wp.paste(ca,(31,20))
#hk image 
hk = Image.open("hk.jpg")
width = hk.width
height = hk.height
ratio = width/height
hk = hk.resize((int(256*ratio),256))
wp.paste(hk,(int(31+ca.size[0]+10),60))
#bw image 
th = Image.open("4.jpg")
width = th.width
height = th.height
ratio = width/height
th = th.resize((int(256*ratio),256))
wp.paste(th,(int(31+ca.size[0]+10+hk.size[0]+10),20))
#cf image 
cf = Image.open("bw.jpg")
width = cf.width
height = cf.height
ratio = width/height
cf = cf.resize((int(256*ratio),256))
wp.paste(cf,(int(31+ca.size[0]+10+hk.size[0]+10+th.size[0]+10),60))
#im image 
im = Image.open("im.jpg")
width = im.width
height = im.height
ratio = width/height
im = im.resize((int(256*ratio),256))
wp.paste(im,(int(31+ca.size[0]+10+hk.size[0]+10+th.size[0]+10+cf.size[0]+10),20))
#hw image

hw = Image.open("hw.jpg")
width = hw.width
height = hw.height
ratio = width/height
hw = hw.resize((int(256*ratio),256))
wp.paste(hw,(int(31+ca.size[0]+10+hk.size[0]+10+th.size[0]+10+cf.size[0]+10+im.size[0]+10),60))

wp.show()
