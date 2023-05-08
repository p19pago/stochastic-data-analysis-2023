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

# we will define each pulse function separately
# one by one

# Basic rectangular pulse function
def rect_p(t):
    return 1 * (abs(t) < 2)

# Basic triangular pulse function
def tri_p(t):
     return (1 - abs(t)) * (abs(t) < 1)

# Sign function
def sign_function(t):
    return 1 * (t >= 0) - 1 * (t < 0)

# Unit step function
def unit_step(t):
    return 1 * (t >= 0)

# Exponential function
def exp_function(t):
    return np.exp(-1 * t) * (t >= 0)

# define and calculate each pulse

t = np.linspace(-10, 10, 1000)

# rectangular pulse
sq = rect_p(t)

# triangular pulse
trig = tri_p(t)

# sign function
sgn = sign_function(t)

# unit step function
y = unit_step(t)

# exponential function
ex = exp_function(t)

# print each value - optional

# print (sq)

# print (trig)

# print (sgn)

# print (y)

# print (ex)

# calculate each plot for each function

# first begin with Triangular Pulse plot

plt.plot(t, trig, label='Triangular Pulse')
plt.legend()
plt.show()

# Square Pulse plot

plt.plot(t, sq, label='Square Pulse')
plt.legend()
plt.show()

# Sign Pulse plot

plt.plot(t, sgn, label='Sign Pulse')
plt.legend()
plt.show()

# Unit Step Function plot

plt.plot(t, y, label='Unit Step Function')
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

# convolution between triangular pulse and square pulse

s3 = sq
s4 = trig
conv2 = np.convolve (s3, s4, mode='same')
conv2 /= len(s4) # Normalization

# convolution plot

plt.plot(t, conv2, label='Convolution Square - Triangular')
plt.legend()

# convolution between square pulse and sign function
s5 = sq
s6 = sgn
conv3 = np.convolve(s5, s6, mode='same')
#conv3 /= len(s6) # Normalization

plt.plot(t, conv3, label='Convolution Square - Sign')
plt.legend()

# convolution between triangle pulse and sign function
s7 = trig
s8 = sgn
conv4 = np.convolve(s7, s8, mode='same')
#conv4 /= len(s8) # Normalization

plt.plot(t, conv4, label='Convolution Triangular - Sign')
plt.legend()

# convolution between exponential function and sign function

s9 = ex
s10 = sgn
conv5 = np.convolve(s9, s10, mode='same')
conv5 /= len(s10) # Normalization

plt.plot(t, conv5, label='Convolution Exponential - Sign')
plt.legend()

# Final Plots
# for each signal

# signals 1 and 2

plt.plot(np.abs(2/(len(s1))*np.fft.rfft(s1)))
plt.show()

plt.plot(np.abs((2/len(s2))*np.fft.rfft(s2)))
plt.show()

# signals 3 and 4

plt.plot(np.abs(2/(len(s3))*np.fft.rfft(s3)))
plt.show()

plt.plot(np.abs((2/len(s4))*np.fft.rfft(s4)))
plt.show()

# signals 5 and 6

plt.plot(np.abs(2/(len(s5))*np.fft.rfft(s5)))
plt.show()

plt.plot(np.abs((2/len(s6))*np.fft.rfft(s6)))
plt.show()

# signals 3 and 4

plt.plot(np.abs(2/(len(s7))*np.fft.rfft(s7)))
plt.show()

plt.plot(np.abs((2/len(s8))*np.fft.rfft(s8)))
plt.show()

# signals 3 and 4

plt.plot(np.abs(2/(len(s9))*np.fft.rfft(s9)))
plt.show()

plt.plot(np.abs((2/len(s10))*np.fft.rfft(s10)))
plt.show()

# for each convolution

plt.plot(np.abs(2/(len(conv1))*np.fft.rfft(conv1)))

plt.plot(np.abs(2/(len(conv2))*np.fft.rfft(conv2)))

plt.plot(np.abs(2/(len(conv3))*np.fft.rfft(conv3)))

plt.plot(np.abs(2/(len(conv4))*np.fft.rfft(conv4)))

plt.plot(np.abs(2/(len(conv5))*np.fft.rfft(conv5)))