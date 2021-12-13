#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:43:18 2021

@author: sjcet
"""

import numpy as np
A = np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])
b=np.array([[3],
             [5],
             [-2]])
inv=np.linalg.inv(A)
x=np.linalg.solve(inv,b)
print(x)

