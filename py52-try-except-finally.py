# python3 py52-try-except-finally.py

a = "abcd"
try : 
    print(a)

except SyntaxError as s:
    print(f"There is an Syntax Error {s}")

except Exception as E:
    # // the block execute when try block make an Error
    print(f"Exceptio is : {E}")
    # we also write one or more except block

else :
    print("This only Run when \"except\" block not run")

finally :
    print("This block of code is aleways execute if any of one try or exception execute") 

