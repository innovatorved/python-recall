# python3 py51-python-cahching-by-funtools.py

import time
from functools import lru_cache

@lru_cache(maxsize = 3) # save last 3 value
def sleep_n_time(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    print(sleep_n_time(3)) # it create an cahe for this same def for for reducing time and space 
    print(sleep_n_time(3))
    print(sleep_n_time(2))
    