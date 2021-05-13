# python3 problem2.py

def permutations(string):
    if string == "":
        return [""]
    l =[]
    for x in string:
        sub = permutations(string.replace(x , "" ,1))
        for y in sub :
            l.append(x+y)
            print("x+sub" , x+y)
    return l

print(permutations("abc"))
