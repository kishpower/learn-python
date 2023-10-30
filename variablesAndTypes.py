twenty = 20

# print(type(type) == str)
# print(isinstance(twenty,int))

twentyStr = str(twenty) # "20"
twentyFloat = float(twentyStr) # float(twenty)
dynamicString = f"this is {twenty}" # this is twenty 

# print(isinstance(twentyStr,str))
# print(isinstance(twentyFloat,float), twentyFloat)

# --- logicals

#0,False,and [] are falsy

# print(1 or 0) #1
# print("hey" and 1) #1
# print("hey" or 0) #hey
# print(False or 0) #0
# print(True or "hey") #True
# print(False and 0) #False
# print("hey" and False) #False
# print("hey" and "something") #something


# --- any,all,in,of

# -- Lists
list1 = [2,"ganesh","abhi","bhushan"]

list1.insert(1,{"name" : "CHETAN"}) # mutated(returns void),[2, {'name': 'CHETAN'}, 'ganesh', 'abhi', 'bhushan']
# list.sort() # error.cant support dict or int
list1.remove({"name": "CHETAN"}) #mutated, [2, 'ganesh', 'abhi', 'bhushan']
list1.remove(2) #'ganesh', 'abhi', 'bhushan']

list2 = list1 # create ref , any operations on list2 will be affected on list
list2 = list1.copy() #create copy,now we can use list2 without affecting list
list2 = ['Ganesh', 'abhi', 'bhushan'] 
list2.sort() #mutates and sorts the strings, ['Ganesh', 'abhi', 'bhushan']
# print(sorted(list2,key=str.lower)) #return a new list with lower fn applied to each element ['abhi', 'bhushan', 'Ganesh']
# print(list2)

# --- tuples
# use tuples if you want your data to be immutable and list when your data changes continuosly at runtime.
# can also use split,splice ,[:] etc

tuple = ("abhi","ganesh","bhushan")
tuple.index('ganesh') # 1
len(tuple) #3
sorted(tuple) #['abhi', 'bhushan', 'ganesh']
tuple[-1] # bhushan
"ganesh" in tuple # True


# --- dictionaries
dog = {
    "name" : "roger",
    "age" : 8,
    "color" : "brown"
}

dog["age"] # 8
dog.get("name") # roger
# dog.pop("color") # brown 
dog.get("toy","horse") # defaults -> horse
# print(dog.popitem()) # ('color', 'brown')
# print(list(dog))
# print(dog.keys()) #dict_keys(['name', 'age', 'color'])
# print(dog.items()) #dict_items([('name', 'roger'), ('age', 8), ('color', 'brown')])
# print(list(dog.items())) # [('name', 'roger'), ('age', 8), ('color', 'brown')]


# --- Sets
set1 = {"ganesh","bhushan","abhi"}
set2 = {"ganesh"}

intersect = set1 & set2 # {'ganesh'}
mod = set1 | set2 # {'ganesh', 'bhushan', 'abhi'} 
check = set1 > set2 # True


# --- functions

def hello(str="default"):
    return "hello" , "world" , "ganesh"
type(hello()) # <class 'tuple'>

def counter():
    count = 0 
    def increment():
        nonlocal count # use nonlocal to tell the variable is from outer closure
        count+=1
        return count    
    return increment 

inc= counter()
# inc() #1
# inc() #2
# inc() #3

# --- loops

condition = True

while condition is True:
    # print("condiition is true")
    condition = False


count = 1
while count < 10:
    count = count + 1
    # print(count)

items = ["1","2","3"]
# for item in items:
    # print(item)

# for item in range(10):
#     print(item) # prints 0 - 9 

# for index,item in enumerate(items): # enumerate creates an index for an iterable oject
#     print(index,item,end=".") #0 1.1 2.2 3.

# continue and break is supported

# --- Classes
# self is keyword particularly used in classes which points to the instansiated object
class Animal:
    # pass # we use pass to define classes without contructors or methods
    def walk(self):
        print('walking ...')
class Dog(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print("woof!")

roger = Dog('roger',8)
# roger.bark() #bark
roger.name # roger

# using inherited methods
# roger.walk()


print()


