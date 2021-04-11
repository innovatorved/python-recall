# exercise printing stars

n = int(input("Enter A Number to Print in th form of Stars : "))
var1 = int(input("Press 1 or 0 : "))
var2 = bool(var1)

print(type(var2) , var2)

if var2 == True :
  for x in range (1,n+1):
    print("\n")
    for y in range(1, x+1):
      print(n , end = " ")

elif var2 == False :
  for x in range (n , 0 , -1):
    print("\n")
    for y in range(x , 0 , -1):
      print(n , end = " ")
