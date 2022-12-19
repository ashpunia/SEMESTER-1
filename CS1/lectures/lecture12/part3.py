# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:28:25 2022

@author: puniaa
"""

def find_min(lists):
    lists = sum(lists,[])
    min = lists[0]
    for e in lists: 
        if e < min: 
            min = e
    return min

if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )