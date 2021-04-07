# *argus & **kwargs

def checkArgus(a,*argus):
    print("A is : ",a)
    print("input list ",*argus)


def checkkwargs(a,**kwargs):
    print("A is : ",a)
    print("input dict is ",**kwargs)
    
# *argus - used for sending whole list in user define function
# **kwags - used for sending whole dict in user define function


# container = [1,2,1,9,8,7,5,2]

# print(container)
if __name__ == "__main__":
    checkArgus(0,1,2,1,9,8,7,5,2)
    checkArgus(0,7,8,9)

    dictt = {"hello":"world" , 1:2 , "a":"b"}
    checkkwargs(1,dictt)
    
