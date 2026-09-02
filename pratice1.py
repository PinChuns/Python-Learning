#import pandas as pd
import math as ma

# Variable and Data Type

name = "Lin"
age = 21
height = 165.8
is_student = True
print(name, age, height, is_student)

# List[]: find data by "index" 
Price = [100, 250, 80, 500, 300]

# A.print list
print(Price)

# B.print the first price of the list
print(Price[0])

# C.print the last price of the list
print(Price[4])
print(Price[-1])

# D.change 500 to 550, then print the new list
Price[3] = 550
print(Price)

# If
Sales = 850
if Sales >= 1000:
    print ("High")
else:
    print ("Low")

# For
Sales = [120, 350, 80, 500, 250]
for sale in Sales:
    print(sale)

Cities = ["Istanbul", "Taipei", "London", "New York", "Rome"]
for city in Cities:
    print(city)

# For...If...
# Find all sales bigger than 200 and print them out.
Sales = [120, 350, 80, 500, 250]
for sale in Sales:
    if sale >= 200:
        print(sale)

# Dict: find data by "key"
customer = {
    "name": "Linda",
    "age": 21,
    "city": "Taipei",
    "sales": 850
}
print (customer)
print (customer["name"])
print (customer["age"])
print (customer["city"])
customer["sales"] = 1000
print (customer)

# Function
def square(x):
    return x * x
print(square(5))
print(square(10))

def check_sales(sales):
    if sales >= 500:
        return("High")
    else:
        return("Low")
print(check_sales(800))
print(check_sales(500))
print(check_sales(300))

# Import
print(ma.sqrt(16))
print(ma.pow(5, 2))    # x的y次方
print(ma.floor(3.14))  # 無條件捨去
print(ma.ceil(3.65))   # 無條件進位
print(ma.fabs(-8))     # 絕對值
print(ma.pi)

# String Methods
name = "Lin"
age = 21
print(name.upper())
print(name.lower())
print(name.replace("Lin", "Linda"))
print(len(name))
print("Hello " + name)
print(f"Hello {name}")
print(f"My name is {name}, and I am {age}.") #f{}:add variable

name = "Leona"
city = "Taipei"
print(name.upper())
print(city.lower())
print(name.replace("Leona", "Linda"))
print(len(name))
print(f"My name is {name}, and I live in {city}.")

# Little Test
Name = "Leona"
Age = "25"
Hight = "168.6"
Student = False
print(Name, Age, Hight, Student)

Sales = [120, 350, 80, 500, 250]
print(Sales)
print(Sales[0])
print(Sales[-1])
Sales[3] = 550
print(Sales)

Sales = [120, 350, 80, 550, 250]
for sale in Sales:
    if sale >=200:
        print(sale)

customer = {
    "name": "Leona",
    "age": 25,
    "city": "Taipei",
    "sales": 850
}
print (customer["name"])
print (customer["city"])
print (customer["sales"])

def check_sales(sale):
    if sale >= 500:
        return "high"
    else:
        return "low"
print(check_sales(800))
print(check_sales(300))

name = "Leona"
print(name.upper())
print(name.lower())
print(len(name))

name = "Leona"
age = 25
city = "Taipei"
print(f"My name is {name}, I am {age} years old, and I live in {city}.")