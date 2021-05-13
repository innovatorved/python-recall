# Dunder Metheod
# all operators : https://www.cmi.ac.in/~madhavan/courses/prog2-2015/docs/python-3.4.2-docs-html/library/operator.html

class Student :
    def __init__(self , fname , lname , Age):
        self.fname = fname
        self.lname = lname
        self.age = Age

    def __add__(self , other):   # dunder metheod use when you perform addition
        return self.age + other.age

    def __repr__(self): # use if you print class
        return ("This is a Class Object")

    def __truediv__(self , other): # if we divide 2 Object
        return self.age / other.age

    def __str__(self):
        return ("This is a Class Object and str function")

if __name__ == "__main__":
    a = Student("Ved Prakash " , "Gupta" , 19)
    b = Student("Shyam" , "kahka" , 25)

    print(a+b)
    print(a/b)
    
    print(a)  # execute str if str is not present it executes repr
    print(str(a)) # we also execute str by str(object_name)

    # we want exectu repr
    print(repr(a))

"""
Operation 	Syntax 	Function
Addition 	a + b 	add(a, b)
Concatenation 	seq1 + seq2 	concat(seq1, seq2)
Containment Test 	obj in seq 	contains(seq, obj)
Division 	a / b 	truediv(a, b)
Division 	a // b 	floordiv(a, b)
Bitwise And 	a & b 	and_(a, b)
Bitwise Exclusive Or 	a ^ b 	xor(a, b)
Bitwise Inversion 	~ a 	invert(a)
Bitwise Or 	a | b 	or_(a, b)
Exponentiation 	a ** b 	pow(a, b)
Identity 	a is b 	is_(a, b)
Identity 	a is not b 	is_not(a, b)
Indexed Assignment 	obj[k] = v 	setitem(obj, k, v)
Indexed Deletion 	del obj[k] 	delitem(obj, k)
Indexing 	obj[k] 	getitem(obj, k)
Left Shift 	a << b 	lshift(a, b)
Modulo 	a % b 	mod(a, b)
Multiplication 	a * b 	mul(a, b)
Negation (Arithmetic) 	- a 	neg(a)
Negation (Logical) 	not a 	not_(a)
Positive 	+ a 	pos(a)
Right Shift 	a >> b 	rshift(a, b)
Slice Assignment 	seq[i:j] = values 	setitem(seq, slice(i, j), values)
Slice Deletion 	del seq[i:j] 	delitem(seq, slice(i, j))
Slicing 	seq[i:j] 	getitem(seq, slice(i, j))
String Formatting 	s % obj 	mod(s, obj)
Subtraction 	a - b 	sub(a, b)
Truth Test 	obj 	truth(obj)
Ordering 	a < b 	lt(a, b)
Ordering 	a <= b 	le(a, b)
Equality 	a == b 	eq(a, b)
Difference 	a != b 	ne(a, b)
Ordering 	a >= b 	ge(a, b)
Ordering 	a > b 	gt(a, b)
"""
    
