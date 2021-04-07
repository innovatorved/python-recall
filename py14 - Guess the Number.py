# Guess the Number
 num = 25
 g = 5
print("__You Entered in Guess the Number Game__")
print("You have only 5 number of Guessses\n")
while (1):
    a = int(input("\nEnter the Number : "))
    if (a<num) :
      g-=1
      print("Wrong!\nthis number is small")
      print(g,"Guess left")

    elif (a>num):
      g-=1
      print("Wrong!\nthis number is Bigger")
      print(g,"Guess left")

    elif a == num :
      print("Your Number is Correct")
      break

    if g == 0 :
      print("No Guss lest\n")
      print("__Game Over__")
      break


"""
__You Entered in Guess the Number Game__
You have only 5 number of Guessses


Enter the Number : 5
Wrong!
this number is small
4 Guess left

Enter the Number : 9
Wrong!
this number is small
3 Guess left

Enter the Number : 27
Wrong!
this number is Bigger
2 Guess left

Enter the Number : 22
Wrong!
this number is small
1 Guess left

Enter the Number : 44
Wrong!
this number is Bigger
0 Guess left
No Guss lest

__Game Over__
"""
