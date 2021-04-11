# Fabonachi Sequence
# find fabonachi sequene
def fab(n,a = 0 , b = 1):
  if n > 0:
    c = a+b
    print(c)
    fab(n-1,b,c)


a = int(input("How much No . of sequence you want to find :"))
fab(a)

"""
How much No . of sequence you want to find :10
1
2
3
5
8
13
21
34
55
89

"""
