# python3 py58-save-object-state-using-pickle.py

class Student:
    _iddd = 101
    # __id = None
    def __init__(self , name , std , idd):
        self.name = name
        self.std = std
        self.__id = idd

    def printdetails(self):
        print(f"Name is : {self.name} , Std is : {self.std} , id is : {self.__id}")
        return 0

ved = Student("Ved Prakash Gupta" , 45 , 1000123)
print(ved.printdetails())
print(ved._Student__id)

# save state by pickle
import pickle

file = "vedObj.pkl"
with open(file , "wb") as f:
    pickle.dump(ved , f)
print("State saved")

#load dump
with open(file , "rb") as f:
    vedgupta = pickle.load(f)

print(type(vedgupta))
print(vedgupta.printdetails())