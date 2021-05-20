# python3 py56-pickleModuledump.py

import pickle

cars = ["Audi" , "BMW" , "Maruti Suzuki" , "Rollas Royals" , "Bolt"]

# store object by help of pickle
file = "mycar.pkl"
# pickling a list we can pickle any object
#"""
with open (file , "wb") as f:
    pickle.dump(cars , f)#"""