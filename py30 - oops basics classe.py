# OOPS concept

# --- Classes - Templates
# --- Object - Instance of the class

# ------- DRY - Do Not repeat YourSelf


class Student:
    pass             # used if any if-else , loops , def functions are blank


# copy class in variable
ved = Student()        #  ---- both Ved & abhi are different
abhi = Student()        

# --- set the value in side the class
ved.name = "Ved Prakash Gupta"
ved.mobile = "7007868719"
ved.college = "Gallgotias College"

string = "Name is : {} and Mobile Number : {}"
print(string.format(ved.name , ved.mobile))
# Name is : Ved Prakash Gupta and Mobile Number : 7007868719
# -----------------------------------------

# -- check name field in avail in abhi
try :
    print(abhi.name)
except Exception as e:
    print(f"\n{e}")
# Output : 'Student' object has no attribute 'name'
# """
# Traceback (most recent call last):
#   File "C:/Users/VED GUPTA/Desktop/basic python key/py30 - oops basics classe.py", line 29, in <module>
#     print(abhi.name)
#  AttributeError: 'Student' object has no attribute 'name'
# """

# -- add different name in abhi
abhi.name = "Abhishek Yadav"


# --- check both classe sobject name were different
print(f"\nved.name : {ved.name} and abhi.name : {abhi.name}")
