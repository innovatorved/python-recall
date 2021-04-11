# Map function
# --- apply a function in whole function

num = ["7" , "8" , "9"] # change those num in int formate
num2 = list(map(int , num)) # list(map(_fun_ , _list_)) | #list used for changing map value in list
print(num2)

# Output : num2 = [7, 8, 9] | # element change in int

# ------------------------------------------------- #

# Example 2
# first change elememt in list then multiply every element of list by 3
print("\nExample 2 : first change elememt in list then multiply every element of list by 3")
num3 = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
# -- change every element in int

num4 = list(map(int , num3))

# user define fun for multiply by 3
a = (lambda b : b*4)
num5 = list(map(a,num4)) # use map
print(num5)

# Output : num5 = [4, 8, 12, 16, 20, 24, 28, 32, 36]
