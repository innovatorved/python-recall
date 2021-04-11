#Dictionary

# Start With Dictionary
dic = { 1 : { "Name" : "Ved Gupta" , "Age" : 18 , "Gender" : "Male" } , 2 : { "Name" : "Harsh" , "Age" : 25 , "Gender" : "Male"  } , 3 : { "Name" : "Ansh" , "Age" : 22 , "Gender" : "Male"  }}

print(dic.keys())
print(dic)
print(dic[1])

newdic = dic.copy()
# print(newdic)
# newdic.clear()
print(dic[1].keys())


"""
dict_keys([1, 2, 3])
{1: {'Name': 'Ved Gupta', 'Age': 18, 'Gender': 'Male'}, 2: {'Name': 'Harsh', 'Age': 25, 'Gender': 'Male'}, 3: {'Name': 'Ansh', 'Age': 22, 'Gender': 'Male'}}
{'Name': 'Ved Gupta', 'Age': 18, 'Gender': 'Male'}
dict_keys(['Name', 'Age', 'Gender'])
"""

# Add value on dic
dic[0] = "Hello I am  Ved"
print(dic)
del dic[0]
 
print(dic)

"""
{1: {'Name': 'Ved Gupta', 'Age': 18, 'Gender': 'Male'}, 2: {'Name': 'Harsh', 'Age': 25, 'Gender': 'Male'}, 3: {'Name': 'Ansh', 'Age': 22, 'Gender': 'Male'}, 0: 'Hello I am  Ved'}
{1: {'Name': 'Ved Gupta', 'Age': 18, 'Gender': 'Male'}, 2: {'Name': 'Harsh', 'Age': 25, 'Gender': 'Male'}, 3: {'Name': 'Ansh', 'Age': 22, 'Gender': 'Male'}}
"""

dic.values()

"""
dict_values([{'Name': 'Ved Gupta', 'Age': 18, 'Gender': 'Male'}, {'Name': 'Harsh', 'Age': 25, 'Gender': 'Male'}, {'Name': 'Ansh', 'Age': 22, 'Gender': 'Male'}])
"""

dic.keys()
dic.popitem()

"""
(3, {'Age': 22, 'Gender': 'Male', 'Name': 'Ansh'})
"""
