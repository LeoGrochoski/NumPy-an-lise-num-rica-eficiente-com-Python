import numpy as np
import csv

path = './numpy-dados/citrus.csv'

# Dont forget to understand the range of the array (columns and rows).
# The first columns is an string columns, so is necessary to skip that.

def load_data(file: csv):
    data = np.loadtxt(file, delimiter=',', usecols=np.arange(1,6,1), skiprows=1)
    print(data)

def main():
    load_data(path)

if __name__ == "__main__":
    main()
