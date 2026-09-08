# Conditions and Branching

# Comparison operators
a = 6
b = 2.5
print(a == 7)  #False, == means equal
print(a != 7)  #True
print(a > 5)  #True
print(a < 4)  #False
print(b > 3)  #False
print(b < 7)  #True
# compare strings
print("ab/cd" == "Serena Lee")  #False
print("ab/cd" != "Serena Lee")  #True

# Branching

# The "if..." Statement

# case1: move on
age = 17
if (age > 18):
    print("you can enter")
print("move on")

# case2: you can enter, move on
age = 19
if age > 18:  #可以沒有括號
    print("you can enter")
print("move on")

# The "if...else" Statement

# case1: go see meat loaf, move on
age = 17
if (age > 18):
    print("you can enter")
else:
    print("go see meat loaf")
print("move on")

# case2: you can enter, move on
age = 19
if (age > 18):
    print("you can enter")
else:
    print("go see meat loaf")
print("move on")


# The "elif..." Statement

# case1: go see Pink Floyd, move on
age = 18
if (age > 18):
    print("you can enter")
elif (age == 18):
    print("go see Pink Floyd")
else:
    print("go see meat loaf")
print("move on")

# case2: go see meat loaf, move on
age = 17
if (age > 18):
    print("you can enter")
elif (age == 18):
    print("go see Pink Floyd")
else:
    print("go see meat loaf")
print("move on")

# case2: you can enter, move on
age = 30
if (age > 18):
    print("you can enter")
elif (age == 18):
    print("go see Pink Floyd")
else:
    print("go see meat loaf")
print("move on")


# Logic operators
print(not(True))
print(not(False))

# OR
# it's in 70's or 90's.
year = 1990
if (year < 1980) or (year > 1989):
    print("it's in 70's or 90's." )
else:
    print("it's in 80's.")

# AND
# it's in 80's.
year1 = 1983
if (year1 > 1979) and (year1 <1990):
    print("it's in 80's.")



