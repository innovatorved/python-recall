# lambda functions
# -- lambda used for short user define function

# Program for add two num
add = (lambda x,y : x+y)
print(add(2,4))

# check no is greater than 45
z = (lambda elem : elem>45)
print(z(0) , z(10) , z(55)) # False False True

# check number is even or odd
check = (lambda x : x%2==0) 
print(check(24)) # True
