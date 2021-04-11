# escape sequence Character

print("\\n ved gupta")
# --\n ved gupta


print("C:\\none\Gupta")
# --C:\none\Gupta


print("\"VedGupta\"")
# --"VedGupta"

# ---------------------------------------

# \'	Single Quote
print("it\'s not a glass of Water")

# \\	Backslash
print("Insert backslash \\ in")

# \n	New Line
print("New\nLine")

# \r	Carriage Return	
print("Hello i a\rved")

# \t	Tab
print("Ved\tPrakash\tGupta")

# \b	Backspace
print("hello \bWorld")

# \f	Form Feed

# \ooo	Octal value
# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

# \xhh	Hex value
# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
txt = "\x33"
print(txt) 

'''
it's not a glass of Water
Insert backslash \ in
New
Line
ved
Ved	Prakash	Gupta
helloWorld
Hello
3
'''
