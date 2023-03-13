# Lab 3rd
# Ornstein-Uhlenbeck process
# "my method" - no function solution

# first we import the functions which will be used for our program.

# we will use the matplotlib, pandas and numpy packages
# we will optionally import statistics package because it might be of need
# same with math package (might be optional)
# there are random numbers here but will be implemented with numpy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# optional packages which will be imported as well

import statistics
import math

# we will also import sqrt which stands for square root - it is optional

from numpy import sqrt

# declaring our variables which will be of need
# no function needed
# as meant by using the def term in Python

dt = 1 # dt represents time steps of our function
x0 = 0 # x0 represents our starting point
steps = 1000; # initially we will use 1000 steps in our code

# Ornstein-Uhlenbeck process requires extra parameters except for mean and/or standard deviation

alpha = 0.5; # oscillation parameter

# plus the Gaussian mean and standard deviation parameters

# mean valuable declaration
# will be set to 0 initially

mn = 0

# standard deviation declaration
# will be set to 0.5 initially

sd = 0.5

# we will create a result array consisting of zeros
# using numpy

ns = np.zeros(steps)

# we will initialize all of our array values to zero as their initial position
# first begin with the start value

ns[0] = x0

for t in range(1, steps):
    ns[t] = alpha * ns[t-1]*dt + sd * np.random.normal(mn,sd)
    
print(ns)    