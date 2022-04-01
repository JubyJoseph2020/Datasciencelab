#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:07:48 2022

@author: sjcet
"""

import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,1,2,3],[6,4,3,2]])
print("array elements")
print(a)
print("excluding first row")
print(a[1:4])
print("3rd and 4th element of 1st row")
print(a[0,2:4])