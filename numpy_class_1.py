import numpy as np 
import csv

class basic_data_numpy:
    def __init__(self: csv):
        # Import the doc .csv and print
        self.data = np.loadtxt('./numpy-dados/apples_ts.csv', delimiter=',', usecols=np.arange(1,88,1)) 

    def qty_dimension_array(self):
        # Show the quantity of dimensions of the array
        qty_array = self.data.ndim
        print(f"The number of info that our data is varying is {qty_array}")

    def qty_items_array(self):
        # Show the quantity of elements in the array
        qty_items = self.data.size
        print(f"The number of items in our array is {qty_items}")

    def check_dimensions_array(self):
        # Check the number of elements in each dimension
        qty_dimensions = self.data.shape
        print(f"The number of dimensions of our array is {qty_dimensions}")

    def transpost_data(self):
        # Better view of the data with transposition
        print(self.data.T)

def main():
    data_instance = basic_data_numpy()

    data_instance.qty_dimension_array()
    data_instance.qty_items_array()
    data_instance.check_dimensions_array()
    data_instance.transpost_data()


if __name__ == "__main__":
    main()


