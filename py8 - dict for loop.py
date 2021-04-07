# for loop

list1 = [["Ved Gupta" , 19] , ["Harsh Gupta" , 21] , ["Ansh Gupta" ,20]]
print(list1)
dict1 = dict(list1)
print(dict1)
new = (dict1.items())
#print(new)
for x , y in new:
  print(x,y)


"""
[['Ved Gupta', 19], ['Harsh Gupta', 21], ['Ansh Gupta', 20]]
{'Ved Gupta': 19, 'Harsh Gupta': 21, 'Ansh Gupta': 20}
Ved Gupta 19
Harsh Gupta 21
Ansh Gupta 20

"""

i = 0
while (i<10):
  print(i , end = "\\")
  i = i+1

"""
0\1\2\3\4\5\6\7\8\9\

"""
