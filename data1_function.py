# Function

# Function Len ans:8
ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
L = len(ratings)
print(L)

# Function Sum ans:70.0
ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
S = sum(ratings)
print(S)

# Function Sorted VS Sort
ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
sorted_r = sorted(ratings)
print(sorted_r)  #[7.0, 7.0, 8.5, 9.0, 9.5, 9.5, 9.5, 10.0] 產生一個新的序列，但序列中的排列改變但值不會改變

# Making Function
def add1(a):
    b = a + 1
    return b
c = (add1(10))
print(add1(5))  #call the add1 function
print(c)

# Multiple parameters
def Mult(a,b):
    c = a * b
    return c

print(Mult(2,3))
print(Mult(10,3.14))
print(Mult(2, 'Serena'))  #SerenaSerena

# Withour Return
def SL():
    print("Serena Lee")
SL()  #Serena Lee

# With an empty body
"""
def Nowork():
    
print(Nowork())  #wrong function
"""
def Nowork():
    pass
print(Nowork())  #None

# Multiple Tasks

def add2(a):
    b = a + 1
    print(a, "plus 1 equals", b)
    return b
add2(2)

# Using loops in functions

def pStuff(Stuff):
    for i, s in enumerate(Stuff):
        print("Album", i, "Rating is", s)
Stuff = [10.0, 8.5, 9.5]
#Index:[  0 ,  1,   2 ]
pStuff(Stuff)

# Collecting arguments

def Anames (*names):
    for name in names:
        print(name)
Anames("LS", "b/cd", "PF")
Anames()

# Scope: global variable
def AddDC(x):
    x = x + "DC"
    print(x)
    return(x)
x = "AC"      #global 變量是在任何函數外定義的，所以是全局範圍變量，定義後可以在任何地方訪問
z = AddDC(x)  #global 變量是在任何函數外定義的，所以是全局範圍變量

# Scope: local variable
def Thriller():
    Date = 1982  #local 變相是在函數內定義的
    return Date
print(Thriller())

def Thriller():
    Date = 1982  #local 變相是在函數內定義的
    return Date
Date = 2017
print(Thriller())  #1982 global的2017不會影響local的1982
print(Date)  #2017 Date這個變量的全局global值是2017

# Scope: Variables
def ACDC(m):
    print(Rating)  #未定義Rating的值
    return(Rating+m)
Rating = 9
p = ACDC(1)  #call ACDC()function時，發現沒有定義值，python會檢查變量是否存在全局範圍內
print(Rating)  #9 function內未定義，會拿全局來使用

def PF():
    global CS    #定義global variable
    CS = '45 million'
    return CS
PF()
print(CS)  #45 million












