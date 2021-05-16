# python3 py48-genrators-yield.py
"""
Iterable : __iter__() or __getitem__()
Iterator : __next__()
Iteration : 

"""

# genrators are iteraators but you can only iterate ones

def range_1_to_n(n) :
    for x in range(1 , n):
        yield x

print(range_1_to_n(10))
num = range_1_to_n(10)

print(num.__next__()) # 1
print(num.__next__()) # 2

# __iter__()
a = "Ved Prakash Gupta"
li = [1,2,3,4,5,6,7,8,9]

a = iter(a)
b = iter(li)

print(a.__next__())
print(b.__next__())

print(a.__next__())
print(b.__next__())
print(a.__next__())
print(b.__next__())