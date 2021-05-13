# Property decorators

class nump:
    def __init__(self , start , end):
        self.start = start
        self.end = end

    @property
    def full(self): # behave like property doesn't need to make Parentheses
        return f"{self.start}  {self.end}"

    @full.setter
    def full(self , startend):
        start = startend[0:3]
        end = startend[3:]
        self.start = start
        self.end = end

    @full.deleter
    def full(self):
        # your code here
        # code execute if anybody try to del the full
        self.start = None
        self.end = None
        print("Delete Done")
        


a = nump(1 , 100)
print(a.full) # see this we don't use parentheses if we define @property
# if we try to call with parenthesis it make TypeError

# chage start end by full
a.full = "100200"

print(a.full) # chaged by the hhelp of setter

del(a.full)
