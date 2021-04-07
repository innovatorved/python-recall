# filter funcion
# -- used o filter the value from list

# any user define function
check = (lambda x : x>0)

# filter positive value from list
lis = [-1,4,5,8,7,-8,-9,0,-6,-5,2,4,-5]

fil = filter(check , lis)
print(fil)
# Output : <filter object at 0x000001EC1037B610>

# change filter into list
fil = list(fil)
print(fil)
# Output : [4, 5, 8, 7, 2, 4]
