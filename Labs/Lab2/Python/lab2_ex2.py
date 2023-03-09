import numpy as np # mathematical functions and symbols each
import random # random numbers
import statistics
import math
import pandas as pd
import csv

# for our easier use, we will import square root because it is of need for our standard deviation
# in this case we will use numpy

from numpy import sqrt

# first we will load the data from our CSV file (namely 'temp-dataset.csv')
# declaring our data as a variable named data

# in this case, I used the official directory where my CSV file is located and imported
# having cloned my github repository on my docs folder

df = pd.read_csv("C:\\Users\\user\\Documents\\στοχαστικη εργαστήριο\\Labs\\Lab2\\temp-dataset.csv",
                 sep=";",
                 decimal=",",
                 index_col=0)

# declaring an array which will come from a CSV file

print(df.values)

t = df.to_numpy() # used in case of "emergency"

# for element in t:
    # print(element)

print(t)

# mean value using numpy

m = np.mean(t)

# variance value using numpy

v = np.var(t)

# standard deviation value using numpy

sdev = np.std(t)

# printing the final results all together

print("Mean value is: ", m)

print("Variance value is: ", v)

print("Standard deviation value is: ", sdev)
