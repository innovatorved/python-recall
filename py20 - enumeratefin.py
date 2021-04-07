#enumerate function

a = ["ved" , "Prakash" , "Gupta" , "hello"]

i = 1
for item in a:
    #print(item)

    if i%2 != 0:
        print(f"item {item}")

    i+= 1

#with enumerate function
print(enumerate(a)) # Output : <enumerate object at 0x000002452601E700>
print(list(enumerate(a)))  # Output : [(0, 'ved'), (1, 'Prakash'), (2, 'Gupta'), (3, 'hello')]
for index , item in enumerate(a):
    print(f"index is {index} and value is {item}")

    if index%2 != 0:
        print(f"item {item}")

    
