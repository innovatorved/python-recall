# example of multilevel Inheriance
class dad:
    mind = "slow"
    basketball = 3 

class Son(dad):
    mind = "moderate"
    hockey = 5

class Grandson(Son):
    mind = "fast"
    hockey = 7
    def mindpow():
        return mind

if __name__ == "__main__":
    john = dad()
    rohan = Son()
    jolly = Grandson()

    print(rohan.__dict__)
    print(rohan.mind)
    print(jolly.mindpow())
    # print(rohan.basketball)

