# String functions

# ----------------Check String have any Space or not
# check string have any space or not
mystr = "my name is ved prakash Gupta Developer at Next Innovation"
print(mystr.isalnum())
# --False

# in this string there has no space
mystr2 = "mynameisvedprakashGuptaDeveloperatNextInnovation"
print(mystr2.isalnum())
# --True

# ------------------Check the String end And start Values

# check the string end
print(mystr.endswith("Next Innovation"))
# --True


# check the string start value
print(mystr.startswith("my name"))
# --True


# ---------------------Count any Single Character in String
# count any Character in String
# ---------- program to count how much times "n" in a string
print(mystr.count("n"))
# Capital or small both letters are different in count
# --4


# ---------------------Capitalise the first Character in String
# Capital the first lettter
mystr3 = "my name is ved prakash Gupta Developer at Next Innovation . heloo EveryOne"
print(mystr3.capitalize())
# Note : It only Convert first Character of String in Capital letter and Change all Other character in small letter
# --My name is ved prakash gupta developer at next innovation . heloo everyone


# -------------------------find any word or string On a String
# find any String on a String
mystr4 = "my name is ved prakash Gupta Developer at Next Innovation . heloo EveryOne my name is ved"
print(mystr4.find("ved"))
# it returs the starting position of String
# if there are multiple string u want to find then it only returns first on.


# ------------------------Change String to Upper and Lower Case
# Change in to upper case
print(mystr4.upper())

# Change String into Lower
print(mystr4.lower())

"""
MY NAME IS VED PRAKASH GUPTA DEVELOPER AT NEXT INNOVATION . HELOO EVERYONE MY NAME IS VED
my name is ved prakash gupta developer at next innovation . heloo everyone my name is ved
"""

# ----------------------replace word on a string
# Replace word on a string
mystr5 = "my name is ved prakash Gupta Developer at Next Innovation . heloo EveryOne my name is ved"
print(mystr5.replace("is" , "the"))

"""
my name the ved prakash Gupta Developer at Next Innovation . heloo EveryOne my name the ved
"""

# -------------------------------------
