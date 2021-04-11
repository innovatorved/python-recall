# Single inheritance module

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

if __name__ == "__main__":
    ved = Student("Ved Prakash Gupta","7007868719" , "GCET")
    abhi = Student("Abhii" , "7376323134" , "GPB")
