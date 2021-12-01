#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 11:30:06 2021

@author: sjcet
"""

import numpy as np

a = np.arange(1, 11, 1)
print("the orginal array :",a)
print("first four elements")
first_element = a[:4]
print(first_element)
print("last six elements")
first_element1 = a[5:]
print(first_element1)
print("elements from index 2 to 7")
first_element2 = a[1:7]
print(first_element2)