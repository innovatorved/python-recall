# Reduce function

from functools import reduce

print(reduce.__doc__)
# reduce(function, sequence[, initial]) -> value

# Apply a function of two arguments cumulatively to the items of a sequence,
# from left to right, so as to reduce the sequence to a single value.
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
# ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
# of the sequence in the calculation, and serves as a default when the
# sequence is empty.

lis = list(range(00,20))
print(lis)
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# find sun of all item avail in list
red = reduce((lambda x , y : x+y) , lis)
print(red)
# Output : 190
