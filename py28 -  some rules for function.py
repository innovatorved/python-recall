# user Define fuunction

# Rule 1 : -- we can put a fuuncion to another variable
def fun1():
    print("Ved Gupta")

fun2 = fun1

# -- & and if we delete  first function 2nd function is exist
del fun1

fun2()
# Output : Ved Gupta

# --------------------------------------------------------------------

# Rule 2 : We can return a function from another function

add = (lambda a,b : a+b)
sub = (lambda a,b : a-b)

def returnFun(num):
    if num>0:
        return add
    elif num<0:
        return sub

print(returnFun(-1)(7,3))  # Output : 4
print(returnFun(4)(17,56))  # Output : 73

# --------------------------------------------------------------------

# Rule 3 : We can also give function as an argument

def execute(funct):
    funct("My Name is Ved Gupta")

execute(print) # Output :My Name is Ved Gupta

# ---- one more example
def exe(fun):
    return fun([1,2,3,4,5,6])


print(exe(sum))
# Output : 21



# --------------------------------------------------------------------
