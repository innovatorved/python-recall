# python3 py50-chge-to-genrator-iter.py

# iter() : function
# type of genrator
# change list or string index acces elements in genrators

string = "abcdefghijklmnopqrstuvwxyz"
num = [1,2,3,4,5,6,7,8,9,0]

# define both as genrator
string = iter(string)
num = iter(num)

# then acces the elements

print(string.__next__())
print(string.__next__())
print(string.__next__())
print(string.__next__())

print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())