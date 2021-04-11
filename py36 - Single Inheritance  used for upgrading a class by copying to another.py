# Single Inheritance
# -- used to update any class by copying to another Class

from py36_singleinheritance_module import Student

class Programmer(Student):
    # Student Class copied to Programmer Class
    def print_prog(self):
        return f"Programmer details is Name : {self.name}\nMobile Number :{self.mobile}\nCollege : {self.college}"


ved = Student("Ved Prakash Gupta","7007868719" , "GCET")
abhi = Student("Abhii" , "7376323134" , "GPB")

anchal = Programmer("Anchal","741258963","GPB")
ajay = Programmer("Ajay Sharma" , "741258894" , "NSTL")

    
print(ajay.details())  # use Student class functions
print(ajay.print_prog()) # use Programmer class functions


# user Super() to add more inputs in __init__functions
class new_advance(Programmer):
    # class contaoin all the feeature of Student Class and Programmer class
    # --- lets add gender in this class

    def __init__(self , name , mobile , college , gender):
        # super() - call the Supper class or input classs for add inputs
        super().__init__(name , mobile , college)
        # then add geender
        self.gender = gender

    # print all avail info in new_advance class
    def print_details(self):
        return f"New_Advanced class variable is Name : {self.name}\nMobile Number :{self.mobile}\nCollege : {self.college} \nGenger : {self.gender}"


print("\n\n")
print("#####"*10)
print("new_advance class")

sudh = new_advance("Suddhanshi Srivastava" , "7954123" , "snathak vidyalaye" , "Male")

print(f"use Student class functions : {sudh.details()}\n")  # use Student class functions
print(f"use Programmer class functions : {sudh.print_prog()}\n") # use Programmer class functions
print(f"use new_advance class functions : {sudh.print_details()}")
