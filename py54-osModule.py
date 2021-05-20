# start with Os module
# python3 py54-osModule.py


import os

# print(dir(os))
# print Courrent Workin Directory
print(os.getcwd())

# change currnt working directory
directory = "/mnt/c/Users/VED GUPTA/Desktop"
os.chdir(directory)
print(os.getcwd())

####----------------------------------------------------------------------------------
# print list of all available files
print(os.listdir())

# Check list of files in any other folder
loc = "/mnt/c/Users/VED GUPTA/Desktop/python-recall/SysModule"
print(os.listdir(loc))

directory = "/mnt/c/Users/VED GUPTA/Desktop/python-recall"
os.chdir(directory)

try :
    # make a folder in any directory
    os.mkdir("This") # for making single directory
    os.makedirs("GrandFather/Father/Son") # create multiple directory inside
    print(os.listdir(directory))
except:
    pass
# rename the file os.rename(old name of file , new Name)
# work in Current Working Directory
try : 
    os.rename("data.txt" , "dataFrame.txt")
except:
    pass

# check enviornment variable
print(os.environ.get("Path")) # None : not found

# setting enviornment Variable
os.environ["name"] = "123" 

# getting Enviorn Variables
print(os.environ.get("name"))
print(os.getenv('name'))

# join two Path
print(os.path.join("/mnt/c/Users/VED GUPTA/Desktop/" , "python-recall/SysModule/"))

# check any path that exists or not
print(os.path.exists("/mnt/c/Users/VED GUPTA/Desktop/python-recall"))
print(os.path.exists("/mnt/c/Users/VED GUPTA/Desktop/python-recall/hello/riyoo"))

# chaek any file that exists or not
print(os.path.isfile("/mnt/c/Users/VED GUPTA/Desktop/python-recall/dataFrame.txt"))