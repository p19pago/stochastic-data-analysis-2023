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

# Basic triangular pulse function
def tri_p(t):
     return (1 - abs(t)) * (abs(t) < 1)
 
# define and calculate each pulse

t = np.linspace(-10, 10, 1000)

# rectangular pulse
sq = rect_p(t)

# triangular pulse
trig = tri_p(t)

# first begin with Triangular Pulse plot

plt.plot(t, trig, label='Triangular Pulse')
plt.legend()
plt.show()

# Square Pulse plot

plt.plot(t, sq, label='Square Pulse')
plt.legend()
plt.show()

# convolution between triangular pulse and square pulse

s3 = sq
s4 = trig
conv2 = np.convolve (s3, s4, mode='same')
conv2 /= len(s4) # Normalization

# convolution plot

plt.plot(t, conv2, label='Convolution Square - Triangular')
plt.legend()

# Final Plots for signals 3 and 4

plt.plot(np.abs(2/(len(s3))*np.fft.rfft(s3)))
plt.show()

plt.plot(np.abs((2/len(s4))*np.fft.rfft(s4)))
plt.show()

# for convolution 2

plt.plot(np.abs(2/(len(conv2))*np.fft.rfft(conv2)))