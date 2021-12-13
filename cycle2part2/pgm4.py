#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:59:27 2021

@author: sjcet
"""

import numpy as np
m1 = np.random.randint(20, size=(2, 2))
print(m1)
m2 = np.random.randint(20, size=(2, 2))
print(m2)
m3 = np.random.randint(20, size=(2, 2))
print(m3)
print("multiplication of the 3 matrices")
m4 = np.dot(m1,m2,m3) 
print(m4) 