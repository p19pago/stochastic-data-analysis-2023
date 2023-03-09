import numpy as np # mathematical functions and symbols each
import random # random numbers
import math
import statistics
import pandas as pd

# declaring an array of 12 values in total
# for each month of the year
# this 12 values represent the temperature of a region (hometown)
# that way we will use the numpy library to implement our array

# t stands for the temperature data for a certain region
# in this case we have chosen the temperature data for the city of Ioannina, located in Epirus
# where I come from

t = np.array([4.7, 6.0, 8.8, 12.5, 17.6, 22.0, 25.0, 24.6, 19.9, 14.9, 9.8, 5.9])

print("Print the temperature values held for each month: ")

print(t)

# mean value using statistics library

mean = statistics.mean(t)

print("Mean value is: ", mean)

# variance value using statistics library

var = statistics.variance(t)

print("Variance value is: ", var)

# standard deviation using statistics library

stdv = statistics.stdev(t, mean)

print("Standard deviation value is: ", stdv)
