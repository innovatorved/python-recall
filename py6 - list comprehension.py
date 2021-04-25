# some list comprehension
# ------ make new list from previous list by apply algo in one line


prev = [1,2,3,4,5,6,7]

new = [x for x in prev ] # apply loop in single line
print(new)

# Output : [1, 2, 3, 4, 5, 6, 7]


new2 = [x for x in prev if x%2==0]
print(new2)

# Output : [2, 4, 6]

new3 = ["abc" , "def" , "ghi" , "jklm" ,"nop"]

new4 = [len(x) for x in new3]
print(new4)
# Output : [3, 3, 3, 4, 3]

new5 = [x.upper() for x in new3]
print(new5)
# Output : ['ABC', 'DEF', 'GHI', 'JKLM', 'NOP']

new6 = [x if len(x)==3 else "NULL" for x in new3]
print(new6)
