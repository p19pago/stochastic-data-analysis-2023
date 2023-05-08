# Lab 7th & 8th - Convolution
# Solution using plot and functions

# first we import the functions which will be used for our program.

# we will use the numpy and matplotlib packages
# additionally we will use the scipy package which will be used to import the signal

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# we will initialize the figure size for our final plot(s)
plt.rcParams["figure.figsize"] = (20,8)

# also we will use the math and statistics packages "just in case"

import math
import statistics

# Sign function
def sign_function(t):
    return 1 * (t >= 0) - 1 * (t < 0)

# Exponential function
def exp_function(t):
    return np.exp(-1 * t) * (t >= 0)

# define and calculate each pulse

t = np.linspace(-10, 10, 1000)

# sign function
sgn = sign_function(t)

# exponential function
ex = exp_function(t)

# Sign Pulse plot

plt.plot(t, sgn, label='Sign Pulse')
plt.legend()
plt.show()

# Exponential Function plot

plt.plot(t, ex, label='Exponential Function')
plt.legend()
plt.show()

# convolution between exponential function and sign function

s9 = ex
s10 = sgn
conv5 = np.convolve(s9, s10, mode='same')
conv5 /= len(s10) # Normalization

plt.plot(t, conv5, label='Convolution Exponential - Sign')
plt.legend()

# Final Plots for signals 9 and 10

plt.plot(np.abs(2/(len(s9))*np.fft.rfft(s9)))
plt.show()

plt.plot(np.abs((2/len(s10))*np.fft.rfft(s10)))
plt.show()

# for convolution 5

plt.plot(np.abs(2/(len(conv5))*np.fft.rfft(conv5)))