# Lab 3rd - Wiener process
# "my method" - solution with function and plot

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
# function needed
# as meant by using the def term in Python

def Wiener(dt = 1, x0 = 0, steps = 1000, mn = 0, sd = 1):

    # all our variables have been initialized at the beginning of the function
    # (see above)
    
    '''
    meant by:
        dt represents time steps of our function
        x0 represents our starting point
        steps represent the number of steps - initially we will use 1000 steps in our code
        mn represents Gaussian mean (or mean) and will be set to 0 initially
        sd represents Gaussian standard deviation
    '''
    
    # we will create a result array consisting of zeros
    # using numpy
    
    ns = np.zeros(steps)
    
    # we will initialize all of our array values to zero as their initial position
    # first begin with the start value
    
    ns[0] = x0
    
    # we will declare the mean or standard deviation variables manually
    # in order for them to be calculated using a built-in function in numpy
    
    # for-loop
    
    for t in range(1, steps):
        #         X(t+dt)=X(t)+sqrt(dt)*npr.randn(Nt)
        ns[t] = ns[t-1] + np.random.normal(mn, sd)*dt
    
    return ns

x = Wiener()

plt.figure(figsize=(20,9))

# first try using the plot
plt.plot(Wiener())

# second try using the plot

plt.plot(Wiener())

# third try using the plot

plt.plot(Wiener())

# and so on
# use it for as many times you want!

# update using the final plot

final = []

for i in range(10):
    
    y = []
    for j in range(10):
        
        x = Wiener()
        y.append(x[-1])
    final.append(np.mean(y))

# final plot functions

plt.figure(figsize=(20,9))
plt.plot(final)

# histogram is optional    
