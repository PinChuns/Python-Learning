# lambda (arguments : expression)

x = lambda a : a + 10
print(x(5))

y = lambda a, b, c : a + b + c
print(y(5, 6, 2))

def myf(n):
    return lambda a: a * n
mydoubler = myf(2)
print(mydoubler(11))

# 數組: 在單個varible中存多個值

cars = ['Benz', 'Volvo', 'Toyota']

# 訪問數組

x = cars[0]
print(x)

# 數組長度
y = len(cars)
print(y)

#循環數組元素
for z in cars:
    print(z)

# 添加數組元素 append()
cars.append('Audi')

# 刪除數組元素 pop()
cars.pop(1)     #刪除第2個元素
print(cars)
cars.remove('Benz')    #僅刪除首次出現的元素
print(cars)