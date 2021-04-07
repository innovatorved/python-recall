# Decorators
# """

def fun1(fun):
    def fun2():
        print("I am")
        fun()
        print("Ved Prakash Gupta")
    def fun5():
        fun()
    return fun2


def fun3():
    print("Good Boy")

# fun3()

fun3 = fun1(fun3)

fun3()
# """

# easiest way to do this @fun1 before fun3 function
@fun1
def fun4():
    print("Good Boy fun4")

fun4()
