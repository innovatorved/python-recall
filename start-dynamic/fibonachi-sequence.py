# python3 fibonachi-sequence.py

def fib_seq(n ,a=0,b=1):
    if n != 0:
        print(a+b)
        fib_seq(n-1 ,b,a+b)

fib_seq(5)