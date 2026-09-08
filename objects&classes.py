# Objects(對象) & Classes(類)

# Objects: Type
"""
a = 1 
type int
object1: 1

b = 12
type int
object2: 1

c = 5
type int
object3: 5

d = 21
type int
object4: 21

e = 77
type int
object5: 77

"""

"""
A = [1, 34, 3]
type list
object1: A = [1, 34, 3]

B = ['a', 'abc', 'def']
type list
object2: ['a', 'abc', 'def']

C = [34, 'aaa', 0]
type list
object3: [34, 'aaa', 0]

D = [False, True, True)]
type list
object4: D = [False, True, True)]

F = []
type list
object5: F = []
"""

# 使用type()命令找出object的class

"""
type1([1, 35, 28])
<class 'list'>

type2(2)
<class 'int'>

type3('The cat is yellow')
<class 'str'>

type1({'dog':1, 'cat':2})
<class 'dict'>
"""

# Creating your own types: Defining Classes

"""
class Circle(object):  
# Data attributes: radius, color

object1
data attributes:
radius = 2
color = red

object2
data attributes:
radius = 3
color = green

class Rectangle(object):
# Data attributes: height, width, color

object1
height = 2
width = 2
color = blue

object2
heigh = 8
width = 2
color = yellow
"""

class Circle():    #define class
    # data attributes of class
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
RedCircle = Circle(10, "red")

"""
dir(object)
回傳object的屬性列表
"""

class Circle(object):
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color
        
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius
CircleObject = Circle()
CircleObject.radius = 10

class Graph():
    def __init__(self, id):
        self.id = id
        self.id = 80

val = Graph(200)
print(val.id)














