def solve(x):
    if x == "":
        return [""]
    list1 = []
    for y in x:
        new = solve(x.replace(y ,"", 1))
        for z in new:
            list1.append(y+z)
    return list1

print(solve("abc"))