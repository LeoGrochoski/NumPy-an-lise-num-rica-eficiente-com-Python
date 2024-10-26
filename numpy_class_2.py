import numpy as np 
import matplotlib.pyplot as plt
from numpy_class_1 import basic_data_numpy

data_instance = basic_data_numpy()
data = data_instance.transpost_data()

def data_dates(data: np.ndarray) -> np.ndarray:
    dates = data[:,0] # : with data transpost to capture every row and 0 to capture the first column of the dates.
    dates = np.arange(1, 88)
    return dates

# def data_prices(data: np.ndarray) -> np.ndarray:
#     prices = data[:, 1:6] # to capture every column of prices, less the first that are dates.
#     return prices

def prices_by_cities(data: np.ndarray):
    Moscow = data[:,0]
    Kaliningrad = data[:,1]
    Petersburg = data[:,2]
    Krasnodar = data[:,3]
    Ekaterinburg = data[:,4]
    return Moscow, Kaliningrad, Petersburg, Krasnodar, Ekaterinburg

moscow, kaliningrad, petersburg, krasnodar, ekaterinburg = prices_by_cities(data)


dates = data_dates(data)
print(dates)
# prices = data_prices(data)
# print(prices)

plt.plot(dates, kaliningrad)
plt.xlabel("Dates")
plt.ylabel("Price")
plt.title("Prices Over Time")
plt.show()