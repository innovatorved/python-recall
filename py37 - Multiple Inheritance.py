# Multiple inheritance

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


class player:
    def __init__(self , play_name , interest):
        self.play_name = play_name
        self.interest = interest

    def print_details(self):
        print(f"Name :{self.play_name}\n Interest :{self.interest}")
        return "Successfuly Printed"

# derive new class by 2 previous class called Multiple Inheritance
class upgrade_class(Student , player):
    pass

class class_upgrade(player, Student):
    pass

try : 
    b = upgrade_class()
except Exception as E:
    print(E)

# Output : __init__() missing 3 required positional arguments: 'name', 'mobile', and 'college'

# -- this because in upgrade_class 2 classes passes like argument concept of Multiple Inheritance
# -- first position class __init__() function react as the th __init__ function of m__main___ function
try : 
    b = class_upgrade()
except Exception as E:
    print(E)

# Output : __init__() missing 2 required positional arguments: 'play_name' and 'interest'


# we use function of bothhh classes in muk=ltiple inheritance
upgrade_class("HELLO","7854123690","GPB")
