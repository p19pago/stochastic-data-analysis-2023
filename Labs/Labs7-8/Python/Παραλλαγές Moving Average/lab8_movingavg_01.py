# Lab 7th & 8th - Moving Average
# Solution using plot and functions

# first we import the functions which will be used for our program.
# we will use the numpy and matplotlib packages

import numpy as np
import matplotlib.pyplot as plt

# also we will use the math and statistics packages "just in case"

import math
import statistics

# we will declare a time series of random data assigned in an array
# first an empty list

timeseries = []

# then declare the array size

n = 10

# a message used to prompt the user to enter their desired values

print("Enter values: ")

# for-loop

for i in range(0, n):
    ts = int(input())
    timeseries.append(ts)
    

def MovingAverage(timeseries,lag=3):
    '''
        Calculates The Simple Moving Average (SMA) of a timeseries with a certain lag.
        timeseries: The timeseries data to impliment the Simple Moving Average (SMA).
        lag: The lag to use for the Simple Moving Average (SMA).
    '''
    ma = np.empty(len(timeseries))
    ma[:] = np.nan
    for i in range(lag,len(timeseries) - lag):
        ma[i] = np.mean(timeseries[i-lag//2:i+lag//2+1])
    return ma

mavg = MovingAverage(timeseries)

plt.plot(timeseries)
plt.plot(mavg)
