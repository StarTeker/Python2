# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:10:13 2020

@author: Batya
"""

array=[1,-3,4,-5,-2,3,-6,7,-4,5,-6,7,8,5,-4,-3,4,-5,6,-7,-8,4,3,-2,0]
for i in range(len(array)):
    if i%2!=0:
        print(array[i],end=' ')
print(sorted(array,reverse=True))
