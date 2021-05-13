#python3 d2-indirect-recursion.py

def function1(str1 , n):
    if n>0:
        print(str1 , n)
        function2(str1 , n-1)
        

def function2(str1 , n):
    if n>0:
        print(str1 , n)
        function1(str1 , n-2)
        

def main(str1 , n):
    function1(str1 , n)

main("ved"  , 5)