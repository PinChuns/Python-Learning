'''
The first python program
'''

# hello world

print ("hello, world")

'''
Variables and Types
'''
# int

print(0b100)  # 二進制整数
print(0o100)  # 八進制整数
print(100)    # 十進制整数
print(0x100)  # 十六進制制整数

# float

print(123.456)

# string

print("hello, world")
print('hello, world')

'''
Variable Naming
Variable names consist of letters, digits, and underscores, and cannot start with a digit.
Special characters (such as !, @, #, etc.) cannot appear in variable names.
Python is a case-sensitive programming language; uppercase "A" and lowercase "a" are two different variables.
Variable names should not conflict with Python keywords, such as: is, if, else, for, while, True, False, etc.
Variable names should not conflict with Python Reserved words, such as int, print, input, str, math, os, etc.
'''

# Using Variables

a = 59        # 定義变量a，赋值59
b = 11        # 定義变量b，赋值11
print(a, b)   # 59 11
print(a + b)  # 70
print(a - b)  # 48
print(a * b)  # 649
print(a / b)  # 5.363636363636363

"""
Check the variable type using type().
"""

a = 98
b = 456.23
c = 'hello, world'
d = True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>

"""
Explicit Type Conversion (Type Casting)
"""

a = 100
b = 123.45
c = '123'
d = '100'
e = '123.45'
f = 'hello, world'
g = True
print(float(a))         # int類型的100轉成float，輸出100.0
print(int(b))           # float類型的123.45轉成int，輸出123
print(int(c))           # str類型的'123'轉成int，輸出123
print(int(c, base=16))  # str類型的'123'按十六進制轉成int，輸出291
print(int(d, base=2))   # str類型的'100'按二進制轉成int，輸出4
print(float(e))         # str類型的'123.45'轉成float，輸出123.45
print(bool(f))          # str類型的'hello, world'轉成bool，輸出True
print(int(g))           # bool類型的True轉成int，輸出1
print(chr(a))           # int類型的100轉成str，輸出'd'
print(ord('d'))         # str類型的'd'轉成int，輸出100

'''
Python Operators
'''

# Operators

print(321 + 12)     # 加法運算，輸出333
print(321 - 12)     # 减法運算，輸出309
print(321 * 12)     # 乘法運算，輸出3852
print(321 / 12)     # 除法運算，輸出26.75
print(321 // 12)    # 整除運算，輸出26
print(321 % 12)     # 求模(取餘數)運算，輸出9
print(321 ** 12)    # 求幂(次方)運算，(321的12次方)輸出1196906950228928915420617322241

"""
Operator Precedence
First: ()
Second: **
Third: * / // %
Fourth: + -
"""

result1 = 2 + 3 * 4  # result is 14
result2 = (2 + 3) * 4  # result is 20
result3 = 2 ** 3 ** 2  # 等於 2 ** 9 = 512，而不是 8 ** 2 = 64 （次方運算子具有由右至左的結合性）
print(result1, result2, result3)
print(2 + 3 * 5)           # 17
print((2 + 3) * 5)         # 25
print((2 + 3) * 5 ** 2)    # 125
print(((2 + 3) * 5) ** 2)  # 625

'''
Assignment Operators
= += -= *= /= //= %= **=
'''

a = 7
b = 3
a += b        # a = a + b
a *= a + 2    # a = a * (a + 2)
print(a)      # 120

'''
Comparison Operators
== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

Logical Operators
and: Logical AND,兩者皆Ture才是Ture
or: Logical OR,其中一個為Ture就是True
not: Logical Not,反轉結果,True變False,False變Ture
'''

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False

age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Allowed to enter")


'''
Conditional Statements
if
elif(else if)
else
'''

# Example 1

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# Example 2
'''
height = float(input('Height(cm): '))
weight = float(input('Weight(kg): '))
bmi = weight / (height / 100) ** 2
print(f'{bmi = }')
if 18.5 <= bmi < 24:
    print('Good!')
elif bmi < 18.5:
    print('Underweight')
else:
    print('Overweight')
'''
'''
Loops
1.For loop
2.While loop
3.Loop Control Statements: break, continue
'''

# For loop: The number of repetitions is known. Iterate over a sequence.

# Default
for i in range(5):  #range() defaults to 0, so the sequence is [0, 1, 2, 3, 4].
    print(i)

# range(start, stop): defaults to a step of 1.
for i in range(1, 6):  # 手動指定：從 1 開始，到 6 之前停止（所以包含 5）
    print(i)

# range(start, stop, step)
for i in range(0, 10, 2):  # 從 0 開始，到 10 之前停止，每次加 2
    print(i)

for i in range(1, 11, 3):
    print(i)

# While loop: The number of repetitions is unknown. Execute as long as the condition is true.

total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

# Loop Control Statements

# break: Terminate the loop

# Example 1
for i in range(1, 6):
    if i == 3:
        break  # 當 i 等於 3 時，立刻打破迴圈！
    print(i)

# Example 2
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total) 

# continue

# Example 1
for i in range(1, 6):
    if i == 3:
        continue  # 當 i 等於 3 時，跳過它，直接進入下一輪！
    print(i)

# Example 2
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
print(total)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')
    print()