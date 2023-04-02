# Lab 5th
# "my method" 2 of 4 - solution with tables assigned from user
# without input or for-loops (random numbers)

# first we import the functions which will be used for our program.

# we will use the numpy, statistics and math packages (math is optional as well)
# we will also import the pandas package because it might be of need (in case of a CSV solution)
# there are random numbers here as declared in tables of our choice
# (we will import the random package too just in case)
# (no dataset from a CSV file)

import numpy as np
import pandas as pd
import statistics
import math
import random

# we will also import sqrt which stands for square root - it is optional

from numpy import sqrt

# declaring an array of our choice
# will consist of different values
# no input from user or empty list creation
# just values assigned without input

# array values declaration
# used random numbers to generate our values

x = np.array([80, 13, 59, 38, 88, 6, 43, 44, 71, 22])

# array size declaration

n = 10

# no input from user or empty list creation
# just values assigned without input

# array values declaration
# used random numbers to generate our values

y = np.array([16, 8, 30, 4, 25, 70, 40, 3, 64, -1])
    
# once we are done with our values we will calculate our variance first
# variance using statistics

var = statistics.variance(x)

print("Variance value is: ", var)

# covariance using statistics

cov = np.cov(y)
print("Covariance value is: ", cov)

# Pearson correlation coefficient using numpy

r = np.corrcoef(x,y)
print("Pearson correlation coefficient is: ", r)
