import numpy as np 


# Import the doc .csv and print
data = np.loadtxt('./numpy-dados/apples_ts.csv', delimiter=',', usecols=np.arange(1,88,1))

# Show the quantity of dimensions of the array
qty_array = data.ndim
print(f"The number of info that our data is varying is {qty_array}")

# Show the quantity of elements in the array
qty_items = data.size
print(f"The number of items in our array is {qty_items}")

# Check the number of elements in each dimension

qty_dimensions = data.shape
print(f"The number of dimensions of our array is {qty_dimensions}")

# Better view of the data with transposition
print(data.T)