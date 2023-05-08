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

# Basic rectangular pulse function
def rect_p(t):
    return 1 * (abs(t) < 2)

# Exponential function
def exp_function(t):
    return np.exp(-1 * t) * (t >= 0)

# define and calculate each pulse

t = np.linspace(-10, 10, 1000)

# rectangular pulse
sq = rect_p(t)

# exponential function
ex = exp_function(t)

# calculate each plot for each function

# Square Pulse plot

plt.plot(t, sq, label='Square Pulse')
plt.legend()
plt.show()

# Exponential Function plot

plt.plot(t, ex, label='Exponential Function')
plt.legend()
plt.show()

# convolution
# trying all together
# convolution between square pulse and exponential

s1 = sq
s2 = ex
conv1 = np.convolve(s1, s2, mode='same')
conv1 /= len(s2) # Normalization

# convolution plot

plt.plot(t, conv1, label='Convolution Square - Exponential')
plt.legend()

# Final Plots
# for signals 1 and 2

plt.plot(np.abs(2/(len(s1))*np.fft.rfft(s1)))
plt.show()

plt.plot(np.abs((2/len(s2))*np.fft.rfft(s2)))
plt.show()

# for convolution 1

plt.plot(np.abs(2/(len(conv1))*np.fft.rfft(conv1)))