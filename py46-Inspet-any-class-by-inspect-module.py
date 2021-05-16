# inspect module
# inspect any Class by inspect Module

class nump:
    def __init__(self , start , end):
        self.start = start
        self.end = end

    @property
    def full(self):
        return f"{self.start}  {self.end}"

    @full.setter
    def full(self , startend):
        start = startend[0:3]
        end = startend[3:]
        self.start = start
        self.end = end

    @full.deleter
    def full(self):
        self.start = None
        self.end = None
        print("Delete Done")


# lets inspect
import inspect
import pprint

pprint.pprint(inspect.getmembers(nump))
