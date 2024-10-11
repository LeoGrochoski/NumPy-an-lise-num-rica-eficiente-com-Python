import numpy as np

data = './numpy-dados/citrus.csv'

# Dont forget to understand the range of the array (columns and rows).
# The first columns is an string columns, so is necessary to skip that.

data = np.loadtxt(data, delimiter=',', usecols=np.arange(1,6,1), skiprows=1)
print(data)