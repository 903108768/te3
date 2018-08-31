# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:18:15 2018

@author: Administrator
"""
def fob(n):
    if n==1 or n==2:
        return 1
    elif n>2:
        return fob(n-1)+fob(n-2)
for n in range(30):
    print(fob(n),sep="##",end="")