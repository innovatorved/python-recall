# Static Methods
# -- used in class whaen no self or class argument passed in class

class Solution:
    a = 7
    def __init__(self , a : int , b : int):
        self.a = a
        self.b = b

    def add(self):
        print(f"{self.a + self.b}")

    @classmethod
    def show(cls):
        print(cls.a)

    # staticmetheod
    @staticmethod
    def reverse(a):
        # print(self.a) : make error because no seelf argument is passed
        for x in range(len(a)-1,-1,-1):
            print(a[x])

if __name__ == "__main__":
    new = Solution(10,56)
    new.add() # 66

    print(new.a) # 10
    new.a = 22
    print(new.a) # 22
    
    print(new.add()) # 78

    print(new.show()) # 7 show cls value

    # static metheod no self or class argument passed
    print(new.reverse("74100258963.qwertyuiopasdfghjklzxcvbnm"))

    # we also use Static Metheod from Class
    print(Solution.reverse("qwertyuiopasdfghbnm"))
# 
