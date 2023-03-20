# Lab 4th - White Noise Process
# "my method" - solution with function and plot

# first we import the functions which will be used for our program.

# we will use the numpy and matplotlib packages
# we will also import the statistics package because it might be of need
# same thing with math package which is built-in Python module (and optional as well)
# there are no random numbers here

import numpy as np
import matplotlib.pyplot as plt

# optional packages which will be imported as well

import math
import statistics

# we will also import sqrt from numpy function which stands for square root
# and might be optional

# declaring our function first
# as meant by using the def term in Python
# and variables-parameters inside of it

def whitenoise(x0 = 0, steps = 1000, mn = 0, sd = 1, a = 1):
    
    # all our variables have been initialized at the beginning of the function
    # (see above)
    
    '''
    meant by:
        x0 represents our starting point
        steps represent the number of steps - initially we will use 1000 steps in our code
        mn represents Gaussian mean (or mean) and will be set to 0 initially
        sd represents Gaussian standard deviation
        a represents amplification parameter
    '''
    
    # we will create a result array consisting of zeros
    # using numpy
    
    ns = np.zeros(steps)
    
    # we will also initialize all of our array values to zero as their initial position
    # first begin with the start value
    
    ns[0] = x0
    
    # for-loop
    
    for t in range(1, steps):
        ns[t] = a * np.random.normal(mn, sd)
    
    # return time series
    return ns

# we will not declare or calculate mean, standard deviation or variance
# first we will use and define our plot

# first define figure size

plt.figure(figsize=(20,9))

# then use a title for our plot
plt.title('White Noise')

# second define and display the plots for each process
# no starting point (x0) or amplification parameter used for the first plot we're trying out

plt.plot(whitenoise(), label='No starting point or amplification parameter used')

# then experiment with amplification parameters of our choice

# the upcoming plots are assigned for a starting point of our choice
# we can add whatever value we like

# experiment for a=1 (amplification parameter set to 1)

plt.plot(whitenoise(a=1.), label='a=1')

# experiment for a=2 (amplification parameter set to 2)

plt.plot(whitenoise(a=2.), label='a=2')

# experiment for a=0.5 (amplification parameter set to 0.5)

plt.plot(whitenoise(a=0.5), label='a=0.5')

# then display the final plot and what is used for each parameter

# update with orbits

final = []

for i in range(10):
    
    y=[]
    
    for j in range(10):
        
        x = whitenoise()
        y.append(x[-1])
        
    final.append(np.mean(y))
    
plt.legend()