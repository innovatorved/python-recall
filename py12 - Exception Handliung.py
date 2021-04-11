# Exception Handling


c = input("#enter a number : ")
d = input("Enter Second Number : ")

try :
  c = int(c)
  d = int(d)
except Exception as e :
  print(e)



"""
#enter a number : p
Enter Second Number : l
invalid literal for int() with base 10: 'p'
"""
