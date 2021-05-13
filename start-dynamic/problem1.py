#python3 problem1.py
"""
str = "abacada"
char = 'a'

def countChar(str, char):
  '''
  you can call helper function as countChar_(str[1:], char)
  '''
  return -1
  
# Output: countChar("abacada", 'a') = 4
  """
i = 0
def countChar(string , char ):
    global i
    if len(string) != 0:
        if string[0] == char:
            i = i + 1
        countChar(string[1:] , char)
    return f"countchar('{string}' , '{char}') = {i}"
    
print(countChar("abacada", 'a'))
