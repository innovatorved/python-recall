# python3 py53Coroutines.py

# 3 if program are time taking to run like training a ml model
# then we try to build sytem that executr some program and save the state if interpruted 
# and again start from same state

# we develop this concept by using tiem module for better understand

# import time

def model():
    """20 secound time consuming task"""
    """
    Coroutines basically use :
    -- When once a lengthy process is necessary and once the proess in completed we use benifits from process
    and executed some code
    in a single user define function
    """
    import time
    time.sleep(2)

    while True :
        text = (yield) # every time value accepted by yield because the while loop continous running and upper code exected oonce
        print(text)

def model2():
    import time
    time.sleep(2)
    text = (yield)
    return(text)
        

if __name__ == "__main__":
    model = model()  # object making

    next(model)
    model.send("hello")
    model.send("hello wert")

    # when all work in done so we close all resource by
    model.close()