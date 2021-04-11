# Instance variable & Class Variable
#-- class Variable avail in class
# -- Instance variable avail in objects
# ----- Class variable not change by any object if you try to change
        #new instance variable will be created  with same name


class Student:                                                 # max_age is class variable not overwritten by anyy object only by itself
    max_age = 9                                          # same for every Object available in class
    pass                                                    # used if any if-else , loops , def functions are blank


# copy class in variable
ved = Student()        #  ---- both Ved & abhi are different
abhi = Student()        

# --- set the value in side the class
ved.name = "Ved Prakash Gupta"
ved.mobile = "7007868719"
ved.college = "Gallgotias College of Engineering and Technology"

abhi.name = "Abhishek yadav"
abhi.mobile = "7376323134"
abhi.college = "Government Polytechnic Bahaich"

# ----------------------------------------------------

# ---- print some vallues from both objects
print(ved.name)       # Output : Ved Prakash Gupta
print(abhi.name)      # Output : Abhishek yadav
print(ved.mobile)     # Output : 7007868719
print(abhi.college)   # Output : Government Polytechnic Bahaich


# --   Access pre define variable in class from bothobjects

print(ved.max_age)  # Output : 9
print(abhi.max_age) # Output : 9

# - direct access
print(Student.max_age) #Output : 9

# -----------------------------------------------------

# print dict
print(ved.__dict__)
# Output : {'name': 'Ved Prakash Gupta', 'mobile': '7007868719',
#         'college': 'Gallgotias College of Engineering and Technology'}

print(abhi.__dict__)
# Output : {'name': 'Abhishek yadav', 'mobile': '7376323134',
#         'college': 'Government Polytechnic Bahaich'}

print(Student.__dict__)
# Output : {'__module__': '__main__', 'max_age': 9, '__dict__': <attribute '__dict__' of 'Student'
   #  objects>,'__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}

# -----------------------------------------------------------------------

# - try o change clas svariable using objct
ved.max_age = 17
print(ved.max_age)   # Output : 17 
print(Student.max_age) # Output : 9

print(ved.__dict__)

# Output :
# 'name': 'Ved Prakash Gupta', 'mobile': '7007868719',
 # 'college': 'Gallgotias College of Engineering and Technology', 'max_age': 17}
# see that there is new variable created max_age

Student.max_age = 6 # change by class 

print(Student.max_age) # Output :  6
print(ved.max_age)      # Output : 17
print(abhi.max_age)     #  Output : 6

# first check the variable in instances if ythe variable not available it checks in thwe class variables
