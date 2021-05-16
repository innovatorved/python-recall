# What is Object Introspection ?

# find information about any Object

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
        

# nump is a Class

ab = nump(2,3)

print(type(ab))

print(id(ab)) # give id of any object or anything savee in memory
# and id is alwways unique

print(dir(ab))  # return all directory information


