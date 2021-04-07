# List
Name = [ "Ved Gupta" ," Ramesh Prasad" , "Anand Kumar" "Shrish Guptas" , "Rishi sharma" ]
Age = [20,56,89,12,45]

print(type(Name),type(Age))

# Age.sort()
print(Age)

print(sum(Age))
print(min(Age))
print(max(Age))
print(len(Age))

Age.reverse()
print(Age)

Age.sort()
print(Age)

new = sorted(Age)
print(new)


"""
<class 'list'> <class 'list'>
[20, 56, 89, 12, 45]
222
12
89
5
[45, 12, 89, 56, 20]
[12, 20, 45, 56, 89]
[12, 20, 45, 56, 89]
"""

print(Age)
new = Name.copy()
print(new)
print(new.count("Ved Gupta"))
new.clear()
print(new)

"""
[12, 20, 45, 56, 89]
['Ved Gupta', ' Ramesh Prasad', 'Anand KumarShrish Guptas', 'Rishi sharma']
1
[]
"""
