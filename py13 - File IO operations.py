# File IO operations


# ------------writing operation
file1 = open("data.txt" , "a")
file1.write("My Name is Ved Prakash Gupta\n lets try to easy\n make a work easier\n ")
file1.close()n

# -----------Read Operation
f = open("data.txt" , "r+")
data = f.read()
print(data)

f.close()
"""
Hello My Name Is Ved Prakash gupta.
lets try to easy 
make a work easier
"""


f = open("data.txt" , "r+")
#data = f.read()

for line in f:
  print(line , end = "")
f.close()

"""
Hello My Name Is Ved Prakash gupta.
lets try to easy 
make a work easier
"""
