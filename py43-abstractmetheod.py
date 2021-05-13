# Abstract Base Class
# basicall ABCMeta and abstractmetheod used in aprogram that defines that :
# if we define any function abstractmetheod then it is necessay to make for all inheriitance classses


# from abc import ABCMeta , abstractmethod

# if we use python 3.4 or greater then we alse use only ABC



# if we inhariate any class bu ABC metaclass
# then they force there inheritance or children class that
# any funcction is compulsory

from abc import ABC , abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def printevery(self):
        return 0


class rectangle(Shape):
    def __init__(self):
        self.val = 45
        
    #def printevery(self , every):
     #   return f"entered : {every}"
a = Shape() # we dont make from abstract basee class
