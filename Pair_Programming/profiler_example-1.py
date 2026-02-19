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
calc.multiply(A, B)
"""The total time is 116.97 ms to run multipy function"""
#sqrt
calc.sqrt(A)
"""The total time is 136.78 ms to run the square function"""
#add
calc.add(A, B)
"""The total time is 117.34 ms to run the add function"""


# Now go back to line 17 above and change the import statement
# to load the more efficient file calculator2 as calc

# look at calculator2
#multiply
calc.multiply(A, B)
"""The total time is 116.39 ms to run the multiply function"""
#sqrt
calc.sqrt(A)
"""The total time is 137.05 ms to run the square function"""
#add
calc.add(A, B)
"""The total time is 165.79 microseconds to run the add function"""

"""The add function improved dramatically, 
dropping from milliseconds to microseconds due to optimized implementation"""
