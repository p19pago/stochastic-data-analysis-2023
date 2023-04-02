# Lab 5th
# "my method" 4 of 4 - solution with values input from a CSV file
# without input or for-loops (random numbers)
# using the random module in Python to generate random values

# first we import the functions which will be used for our program.

# we will use the numpy and math packages (math is optional as well)
# we will also import the pandas package because it might be of need (in case of a CSV solution)
# there are random numbers here as declared in tables of our choice
# (we will import the random package too just in case)
# (no dataset from a CSV file)

import numpy as np
import pandas as pd
import math
import random
import csv

# we will also import sqrt which stands for square root - it is optional

from numpy import sqrt

# we will also import the data from the CSV file we created ('method4_dataset.csv')
# declaring our data in two variables

# one variable for the data of the x array
# and one for the data of the y array

# in this case, I used the official directory where my CSV file is located and imported
# having cloned my github repository on my docs folder

# dataframe for the x array

df_x = pd.read_csv("method4-dataset.csv",
                   sep=",",
                   decimal=",",
                   index_col=1,
                   )

# declaring an array of our choice which will come from a CSV file
# will consist of different values
# no input from user or empty list creation
# only from a CSV file

# array values declaration
# used a CSV file to assign each value

x = df_x.to_numpy()

print('Display all values of x array: \n', x)

# dataframe for the y array

df_y = pd.read_csv("method4-dataset.csv",
                   sep=",",
                   decimal=",",
                   index_col=0,
                   )

# declaring an array of our choice which will come from a CSV file
# will consist of different values
# no input from user or empty list creation
# only from a CSV file

# array values declaration
# used a CSV file to assign each value

y = df_y.to_numpy()

print('Display all values of y array: \n', y)

# array size declaration

n = 10

# values for x array
# mean value using numpy

mx = np.mean(x)

print("Mean value is: ", mx)

# variance value using numpy

vx = np.var(x)

print('Variance value is: ', vx)

# statistics value using numpy

sdev_x = np.std(x)

print("Standard deviation value for x is: ", sdev_x)

# values for y array
# mean value using numpy

my = np.mean(y)

print("Mean value is: ", my)

# variance value using numpy

vy = np.var(y)

print('Variance value is: ', vy)

# statistics value using numpy

sdev_y = np.std(y)

print("Standard deviation value for x is: ", sdev_y)

# both arrays
# covariance using numpy

# x.T and y.T are used to avoid warnings on array size
# in both cases

cov_xy = np.cov(x.T,y.T)

print("Covariance value is: ", cov_xy)

# Pearson correlation coefficient using numpy

pearson_xy = np.corrcoef(x.T,y.T)

print("Pearson correlation coefficient value is: ", pearson_xy)
