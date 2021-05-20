# Access Specifier
# public
# protected
# private

class Student:
    public_var = "this variable is public"
    _protected_var = "this is private var"
    __private_var = "this is private var"

    def __init__(self ,public , protected , private):
        self.public = public
        self._protected = protected
        self.__private = private

if __name__ == "__main__":
    ved = Student("Name : Ved Prakash Gupta" , "Age : 19" , "Mobile:7007868719")
    print(ved.public)        # Output :'Name : Ved Prakash Gupta'
    print(ved._protected)        # Output : 'Age : 19'
    print(ved.__private)
    # Output :
    """Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ved.__private
AttributeError: 'Student' object has no attribute '__private'"""
    
    print(ved._Student__private)        # Output : 'Mobile:7007868719'
    # private variable acces by classs define
    
