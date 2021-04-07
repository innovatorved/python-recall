# Recursion

result = 1
def fac(n):
  """
    find factorioal of a Number
    #paramete required 
    n
  """
  if n>0 :
    global result
    result = result * n
    #print(result)
    fac(n-1)
  return result

n = fac(5)
print(n)
