# Lab 5th
# "my method" 1 of 4 - solution with tables input from user

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
# input from user

# empty list creation

x = []

# array size declaration

n = 10

# a message used to prompt the user to enter their desired values

print("Enter values: ")

# for-loop
for i in range(0, n):
    val1 = float(input())
    x.append(val1)

# empty list creation

y = []

# a message used to prompt the user to enter their desired values

print("Enter values: ")

# another for-loop used for our second array

# for-loop
for i in range(0, n):
    val2 = float(input())
    y.append(val2)
    
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