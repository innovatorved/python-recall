# Super() and Overriding()\

class A:
    ab = "I am  Class A"

    def __init__(self):
        self.varb = "inside class A"
        self.ab = "Instance of A"

class B(A):
    ab = "I am Class B"
a = A()
b = B()

print(b.ab) # always program first check instance variable theen clas s variable


# super()

class hello:
    def __init__(self,name):
        self.name = name
        self.end = "Yes"

class hey(hello):
    def __init__(self , name , acc):
        super().__init__(name)
        self.acc = acc
        self.end = "No"
        
c = hello("Ved")
print(c.name , c.end)

d = hey("Prakash" , "789")
print(d.name , d.acc , d.end)
