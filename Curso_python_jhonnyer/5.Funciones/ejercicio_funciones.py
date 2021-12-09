#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:45:58 2021

@author: root
"""

def relacion(a,b):
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))
