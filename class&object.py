# Classes/Objects
'''
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties(屬性) and methods(方法).
A Class is like an object constructor, or a "blueprint" for creating objects.
'''

# Creat class 

class MyClass:    #Create a class named MyClass
    x = 5.        #with a property named x

p1 = MyClass()    #creat an object named p1
print(p1.x)       #print the value of x

# Delete object

del p1

# Multiple Objects

pa = MyClass()
pb = MyClass()
pc = MyClass()

print(pa.x)
print(pb.x)
print(pc.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p2 = Person("Emil", 25)

print(p2.name)
print(p2.age)