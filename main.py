print("__Max Elements in list__")
a = int(input("Enter the Number of Elements in the List : "))

list1 = []
for x in range(0,a):
    list1.append(int(input(f"Enter the elements at {x} index : ")))

print(f"\n\nMaximum elements in list : {max(list1)}")


print("\n\n__find Element in list__")
a = int(input("Enter the Number of Elements in the List : "))

list1 = []
for x in range(0,a):
    list1.append(int(input(f"Enter the elements at {x} index : ")))

b = int(input("Enter the elememnt you want to find : "))

if b in list1:
    print(f"\nElement {b} is found @ {list1.index(b)} ")
