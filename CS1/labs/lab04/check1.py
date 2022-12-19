# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 16:45:42 2022

@author: puniaa
"""
'''
from PIL import Image ##must import Image first to be able to use it
im = Image.new('RGB',(512,512), 'white') # use mode 'RGB', color 'white'
im = im.resize((256,256)) # resize to the given width/height passed as a tuple
im.paste(im, (2,2)) # (x,y) coordinates of upper left corner as a tuple
im.save('image1')
im.show()
'''
from PIL import Image 
from check2_helper import make_square

image = Image.new('RGB', (512,512),'white')


im = Image.open("im.jpg")
im1 = make_square(im)
im = im1.resize((256,256))
image.paste(im,(0,0))
hk = Image.open("hk.jpg")
hk1 = make_square(hk)
hk = hk1.resize((256,256))
image.paste(hk,(0,256))
ca = Image.open("ca.jpg")
ca1 = make_square(ca)
ca = ca1.resize((256,256))
image.paste(ca,(256,0))
bw = Image.open("bw.jpg")
bw1 = make_square(bw)
bw = bw1.resize((256,256))
image.paste(bw,(256,256))
image.show()


