# F String

a = "Ved Gupta"
b = "My Name is %s"%a
print(b)
"""
My Name is Ved Gupta
"""

# --------------------------------------
c= " My Name is %s"
print(c%a)
"""
 My Name is Ved Gupta
"""

# ----------------------------------------
d = "ved"
e = "Gupta"
f = "My Self {} {}"
g =  f.format(d,e)
print(g)
"""
My Self ved Gupta
"""

# -----------------------------------------
print(f"my name is {d} {e}")
"""
my name is ved Gupta
"""

# ------------------------------------------
