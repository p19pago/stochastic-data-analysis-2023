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

# Sign function
def sign_function(t):
    return 1 * (t >= 0) - 1 * (t < 0)

# define and calculate each pulse

t = np.linspace(-10, 10, 1000)

# rectangular pulse
sq = rect_p(t)

# sign function
sgn = sign_function(t)

# Square Pulse plot

plt.plot(t, sq, label='Square Pulse')
plt.legend()
plt.show()

# Sign Pulse plot

plt.plot(t, sgn, label='Sign Pulse')
plt.legend()
plt.show()

# convolution between square pulse and sign function
s5 = sq
s6 = sgn
conv3 = np.convolve(s5, s6, mode='same')
#conv3 /= len(s6) # Normalization

plt.plot(t, conv3, label='Convolution Square - Sign')
plt.legend()

# Final Plots
# for signals 5 and 6

plt.plot(np.abs(2/(len(s5))*np.fft.rfft(s5)))
plt.show()

plt.plot(np.abs((2/len(s6))*np.fft.rfft(s6)))
plt.show()

# for convolution 3

plt.plot(np.abs(2/(len(conv3))*np.fft.rfft(conv3)))