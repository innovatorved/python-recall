import sys 

# check python version
print("Current Python Version : " + sys.version)

# pritn script name
print("\n",sys.argv)

# print copyroght information
print(f"\n\nPython Copyright : {sys.copyright}")

print(f"\n\n {sys.executable}") # give python execute path

# Built in modules python
print(f"\n\n Built in modules : {sys.builtin_module_names}")

# return all python modules avail on system
# print(f"\n\n {sys.modules}")
print(f"\n\n Print Module keys {sys.modules.keys()}")

print(f"\n\n Where Python Running : {sys.platform}")

print(f"\n\nGet Windows Enviornment : {sys.getwindowsversion()}")