# Constructor
# --- method to give value to instance

class Student:                                                 # max_age is class variable not overwritten by anyy object only by itself
    max_age = 9                                          # same for every Object available in class

    def __init__(self , name , mobile ,college):
        """this function auto run when we make the instance"""
        self.name = name
        self.mobile = mobile
        self.college = college
        
    def details(self):
        return f"Name : {self.name}\nMobile Number :{self.mobile}\nCollege : {self.college}"
    
ved = Student("Ved Prakash Gupta","7007868719" , "GCET")

print(ved.details())
print(ved.max_age , ved.name)

