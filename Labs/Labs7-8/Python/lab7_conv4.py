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

# Basic triangular pulse function
def tri_p(t):
     return (1 - abs(t)) * (abs(t) < 1)

# Sign function
def sign_function(t):
    return 1 * (t >= 0) - 1 * (t < 0)

# define and calculate each pulse

t = np.linspace(-10, 10, 1000)

# triangular pulse
trig = tri_p(t)

# sign function
sgn = sign_function(t)

# calculate each plot for each function

# first begin with Triangular Pulse plot

plt.plot(t, trig, label='Triangular Pulse')
plt.legend()
plt.show()

# Sign Pulse plot

plt.plot(t, sgn, label='Sign Pulse')
plt.legend()
plt.show()

# convolution between triangle pulse and sign function
s7 = trig
s8 = sgn
conv4 = np.convolve(s7, s8, mode='same')
#conv4 /= len(s8) # Normalization

plt.plot(t, conv4, label='Convolution Triangular - Sign')
plt.legend()

# Final Plots for signals 7 and 8

plt.plot(np.abs(2/(len(s7))*np.fft.rfft(s7)))
plt.show()

plt.plot(np.abs((2/len(s8))*np.fft.rfft(s8)))
plt.show()

# for convolution 4

plt.plot(np.abs(2/(len(conv4))*np.fft.rfft(conv4)))