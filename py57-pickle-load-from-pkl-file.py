# python3 py57-pickle-load-from-pkl-file.py

import pickle


# load object by help of pickle
file = "mycar.pkl"

with open (file , "rb") as f:
    cars = pickle.load(f)

print(type(cars))
print(cars)