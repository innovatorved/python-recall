# Break an Continue

i = 0
while (True):
  print(i , end = "\\")
  if (i == 45):
    print("\nWhile loop were breaked at 45")
    break
  i = i+1

print("exit()")

"""
0\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25\26\27\28\29\30\31\32\33\34\35\36\37\38\39\40\41\42\43\44\45\
While loop were breaked at 45
exit()
"""

while (True):
  num = int(input("Enter Any Number :"))
  if num<=100:
    continue
  else:
    break

print("Loop exit()")

"""
Enter Any Number :45
Enter Any Number :56
Enter Any Number :55
Enter Any Number :55
Enter Any Number :100
Enter Any Number :101
Loop exit()
"""
