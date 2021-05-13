from sys import argv
def fun(a :str , n : int):
    if n > 0:
        n = n
        fun(a , n-1)
        print(a,n)

def main(a , n):
    # print(type(a) , type(n))
    fun(a , int(n))

main(argv[2] , argv[1])
'''
Therefore, while this ordering might seem trivial; 
it can make all the difference. 
The first case, 
where the print statement occurs before the recursive call, is called tail recursion. '''

