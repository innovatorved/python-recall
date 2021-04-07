# Self & __init__() constructors

class Student:                                                 # max_age is class variable not overwritten by anyy object only by itself
    max_age = 9                                          # same for every Object available in class
    # pass
    def details(self):
        return f"Name : {self.name}\nMobile Number :{self.mobile}\nCollege : {self.college}"
    

ved = Student()        #  ---- both Ved & abhi are different
abhi = Student()

# --- set the value in side the class
ved.name = "Ved Prakash Gupta"
ved.mobile = "7007868719"
ved.college = "Gallgotias College of Engineering and Technology"

abhi.name = "Abhishek yadav"
abhi.mobile = "7376323134"
abhi.college = "Government Polytechnic Bahaich"

# ---------------------------------------------------- #

print(ved.details())
print(abhi.details())

