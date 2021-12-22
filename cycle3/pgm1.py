#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:48:53 2021

@author: sjcet
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2001,2002,2003,2004,2005,2006,2007])
y = np.array([24000,22500,19700,17500,14500,10000,5800])

plt.plot(x, y ,'-.',color='r',marker='*',ms='20',mec='g',mfc='g')
plt.title("Value Depreciation " ,loc='left')
plt.xlabel("Year")
plt.ylabel("Car Value")

plt.show()

