# --- modules
from modules.dog import bark
# bark()


# --- using built-in libraries in Python
from math import sqrt
sqrt(4) # 2.0

import sys
sys.argv # ['main.py', 'ganesh']

# print(sys.argv)

# lambda funtions

square = lambda x : x * x # or s
square(2) # 4
 
numbers = [1,2,3,4]
map(square,numbers) #<map object at 0x102acec50>
list(map(square,numbers)) #[1, 4, 9, 16]

list(filter(lambda x : x%2 == 0,numbers))# [2, 4]

from functools import reduce
reduce(lambda a,b : a + b,numbers) # 10


# --- Decoratorss
def logtime(func):
    def wrapper():
        print('before')
        val = func()
        print('after')
        return val
    return wrapper

@logtime
def hello():
    print("hello world")
# hello() # before hello world after

# --- Docstrings

class Cat:
    """hey cat can have a name,age and can meow!!"""
    def __init__(self,name):
        """hey this is a constructor for cat"""
        self.name = name
# help(Cat)        

# --- Annotations(used to add datatypes to varibles)

def increment(n : int) -> int:
    return n + 1
increment(2) #3

# --- Exceptions

try:
    result = 2/0
    # raise Exception("an error") # alternatively we can also raise exception
except Exception as error:
    error # can print error
finally:
    result = 1
# result # 1

class parrotNotFound(Exception):
    pass

try:
    raise parrotNotFound
except parrotNotFound:
    avoiding = None # adding variable so that we can comment peacefully.
    # print("parrot not found")

# --- File handling 
filename = '/Users/flavio/test.txt'

# try: # using try catch to read a file,check alternative below this example for easier impl
#     file = open(filename,'r')
#     content = file.read()
#     print(content)
# finally:
#     file.close()

# with open(filename, 'r') as file: # implicit file closing,and exception handling
#     content = file.read()
#     print(content)

# ---  pip python package manager,its global install 
# use terminal,here are some commands:
# pipy.org for more packages
# pip install <packageName>
# pip uninstall <packageName>
# pip show <packageName>

# --- List Compressions(can use if you don't want to use lamdas/for loops)
numbers_power_2 = [n**2 for n in numbers]
(numbers_power_2) #[1, 4, 9, 16] 

#--- Operator Overload
class Fish:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __gt__(self,other):
        return True if self.age > other.age else False

sinsa = Fish('sinsa',10)
fishoo = Fish('fishoo',9)
sinsa > fishoo # True
#check out others __add__(),sub,mul,truediv,and

print(sinsa > fishoo)

