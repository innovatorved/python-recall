# python3 py49-genrators-ex1.py

n = 10

def fib(a=0 , b = 1):
    for x in range(n):
        yield (a+b)
        a , b = b , b+a
        

a = fib(0,1)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())