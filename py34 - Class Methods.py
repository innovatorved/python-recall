class Student:                                                
    max_age = 9                                          
    def __init__(self , name , mobile ,college):
        """this function auto run when we make the instance"""
        self.name = name
        self.mobile = mobile
        self.college = college

    @classmethod
    def change_age(cls , newage):
        cls.max_age = newage

    @classmethod
    def create(cls , string):
        strlist = string.split("-")
        return cls(strlist[0] , strlist[1] , strlist[2]) # direct metheod is return cls(*string.split("-")) and cls(strlist[0] , strlist[1] , strlist[2])
        
    def details(self):
        return f"Name : {self.name}\nMobile Number :{self.mobile}\nCollege : {self.college}"
    
ved = Student("Ved Prakash Gupta","7007868719" , "GCET")
abhi = Student("Abhii" , "7376323134" , "GPB")

# print(ved.details())
# print(abhi.details())

# if we try to change class variable by instanc then new instance variable were created
# --- then we can access class by class metheod
# classmetheod same as Decoratoers

# -- if we change using class metheod
ved.change_age(55)

print(Student.max_age)
# Output : 55

# class metheod as constructor

sudh = Student.create("Sudhanshu-7234999568-GPB")

print(Student.__dict__)
print(sudh.details())

