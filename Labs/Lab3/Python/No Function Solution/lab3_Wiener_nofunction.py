# Lab 3rd - Wiener process
# "my method" - no function or plot

# first we import the functions which will be used for our program.

# we will use the matplotlib, pandas and numpy packages
# we will optionally import statistics package because it might be of need
# same with math package (might be optional)
# there are no random numbers here

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

# mean valuable declaration
# will be set to 0 initially

mn = 0

# standard deviation declaration
# will be set to 1 initially

sd = 1

# we will create a result array consisting of zeros
# using numpy

ns = np.zeros(steps)

# we will initialize all of our array values to zero as their initial position
# first begin with the start value

ns[0] = x0

# for-loop

for t in range(1, steps):
    #         X(t+dt)=X(t)+sqrt(dt)*npr.randn(Nt)
    ns[t] = ns[t-1] + np.random.normal(mn, sd)*dt
    
print (ns)    
