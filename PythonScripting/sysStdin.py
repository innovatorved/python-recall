import sys

for line in sys.stdin:
    print(line.rstrip())
    if 'q' == line.rstrip(): 
        break
    print(f'Input : {line}') 
  
print("Exit") 