# python3 prob1-sol2.py

def countChar(string , char):
    if len(string) == 0:
        return 0
    if string[0] == char:
        return 1 + countChar_(string[1:] , char)
    if string[0] != char:
        return countChar_(string[1:] , char)

def main(string , char):
    return f"countchar('{string}' , '{char}') = {countChar('abacada', 'a')}"

print(main("abacada","a"))
