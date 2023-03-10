# Python code for Random Walk in One Dimension of the X, Y Axis.
# My method as described in my repo from 2022: p19pago/probability-2022
# Lab 7 out of total 10 we did in class, as taken place on Tuesday April 12th 2022

# solution without decimals

# Code
# Import functions as to be used during the code
# Functions that will be used: random (for random numbers), numpy (for mathematical functions/symbols) and matplotlib to implement the final chart and position of the walker.
# Initialization

import random # random numbers
import numpy as np # mathematical functions and symbols each
import matplotlib.pyplot as plt # diagram/graph plotting package

# we first import the three (3) basic libraries as described in the comments on the first 8 lines of the code
# either way we should have imported the "time" library, but it does not count in our method because it measures the number of seconds since January 1st 1970.
# but we will use arrays to declare our final points and positions (using np)

# let's get to the main point of the code and what it actually needs.
# variable declaration

# in Python you cannot declare a variable without assigning its value, so we are going to use values for each variable
# variables that will be of use on our method are:

# generic variables

#       x (a random variable)
#       rw (an array determining the amount of walks in one dimension)

x = 0 # x must be initialized to 0
rw = np.zeros(1000) # a 1 dimensional array consisting of zeros at the beginning. It determines the amount of walks in one dimension.

# other variables
# first walkers

#       p1 (position for the first walker as it is moving across the axis)
#       s1 (registered position for the first walker as shown in the chart)

p1 = 0 # position for the first walker must be initialized to 0
s1 = [0] # registered position for the first walker, also must be initialized to 0

# no heads or tails will be of need in this example

# IMPORTANT: before we move into the main part of the code, we should alter the values of the array so instead of zeros it should be integers from 0 to 1000

rw = np.arange(0, 1000)

# main part of the code

# using a for-loop to determine time points and positions as the walker moves around.

for i in range (1, 10): # first we begin with 10 rolls

    x = random.randint(0,9)
    print("Random number result is: ", x)

    # two simple if-structures to determine if the walker should move up or down

    # if-structure if x is greater than 5
    
    if (x>5):
        p1 = x + 1
        s1.append (rw[p1])
        
    # if-structure if x is smaller than 5
     
    if (x<5):
        p1 = x - 1
        s1.append (rw[p1])
    
print("Registered position for the first walker is: ", s1) 
print ("Final position for the first walker is:", p1)

# plotting down the graph of the random walk in 1 dimension
# using pyplot

plt.plot(s1)
plt.show()
