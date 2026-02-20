# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 10:59:28 2025

@author: SheetsH
"""

import numpy as np

import evelyn_summer as summer

#set the matrix sizes

M = 10**7


# set the seed on the random number generator
# so we get repeatable results

np.random.seed(42)

# generate random matrices to work with

A = np.random.random((M))

x=summer.sum(A)

print(x)