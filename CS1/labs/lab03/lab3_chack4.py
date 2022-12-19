# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:43:26 2022

@author: puniaa
"""

bpop = int(input("Number of bunnies: "))
print(bpop)
fpop = int(input("Number of foxes: "))
print(fpop)


def next_pop(bpop, fpop):
    bpop_next = int((10*bpop)/(1+0.1*bpop) - 0.05*bpop*fpop)
    bpop_next = max(bpop_next,0)
    fpop_next = int(0.4 * fpop + 0.02 * fpop * bpop)
    fpop_next = max(fpop_next,0)
    return bpop_next,fpop_next
'''
print("Year 1:",bpop,fpop)
print("Year 2:",*next_pop(bpop,fpop))
bpop, fpop  = next_pop(bpop,fpop)
print("Year 3:",*next_pop(bpop,fpop))
bpop, fpop  = next_pop(bpop,fpop)
print("Year 4:",*next_pop(bpop,fpop))
bpop, fpop  = next_pop(bpop,fpop)
print("Year 5:",*next_pop(bpop,fpop))
'''
i = 1
print("Year 1:",bpop,fpop)
while i < 5:
    bpop_new, fpop_new = next_pop(bpop,fpop)
    bpop,fpop = bpop_new, fpop_new
    i += 1
    print("Year", i, bpop, fpop)