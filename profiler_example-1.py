# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:35:42 2025

@author: hdavi
"""

# load numpy as np

import numpy as np

# load the user created file "calculator",  this has the functions
# we will profile

# open calculator.py and look at it in Spyder

import calculator2 as calc

#set the matrix sizes

M = 10**3
N = 10**3

# set the seed on the random number generator
# so we get repeatable results

np.random.seed(42)

# generate random matrices to work with

A = np.random.random((M,N))
B = np.random.random((M,N))

#now call hypotenause and print the first return value

print(calc.hypotenuse(A, B)[0,0])


# Question/Action

#Run the profiler

# Enter below the amound of time it takes to run each function in
# the calculator file (multiply, sqrt, add)

#multiply
#sqrt
#add


# Now go back to line 17 above and change the import statement
# to load the more efficient file calculator2 as calc

# look at calculator2
