print(int(False))  #0
print(int(True))   #1

print("Serena\nLee")  #\n換行
print("Serena\tLee")  #\t=tap空格
print("Serena\\Lee")

name = "Serena Lee"
print(3 * name)
print(name.find("na"))  #輸出第一個index
name2 = name + "is good."
print(name2)

A = "Serena is the best."
B = A.replace("Serena", "Jason")
print(A)
print(B)


# Tuple: Python的tuple（元組）是一種內建的有序資料結構，
#(有順序的不可動列表)
#基本語法：使用小括號 () 包裹元素，並用逗號（,）分隔。
my_tuple = (1, 2, 3.6, "apple")  
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-2])

# Concatenating Tuple
my_tuple2 = my_tuple + (5, 6, 4.8, "orange")
print(my_tuple2)

# lenth(): 獲取元素數量
print(len(my_tuple2))

# Slicing Tuple
print(my_tuple[0:3])

# Tuple is Immutable 元組是不可變的，意味著無法更改它們
Ratings = (10, 9, 6, 5, 10, 8, 9, 6, 2)
Ratings1 = Ratings  # Ratings和Ratings會指向同一個元組(10, 9, 6, 5, 10, 8, 9, 6, 2)

# Sorted
RatingsSorted = sorted(Ratings)
Ratings1Sorted = sorted(Ratings1)
print(RatingsSorted)  # ans:[2, 5, 6, 6, 8, 9, 9, 10, 10]
print(Ratings1Sorted)  # ans:[2, 5, 6, 6, 8, 9, 9, 10, 10]

# 如果想改變，可以賦予一組新的元組
Ratings = (5, 5, 6, 7, 8)
print(Ratings)  # ans:(5, 5, 6, 7, 8)
print(Ratings1)  # ans:(10, 9, 6, 5, 10, 8, 9, 6, 2)

# Tuple Nesting
NT = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))
print(NT[2])  # ans:("pop", "rock")
print(NT[2][1]) # ans:rock

# List : list are mutable可變的(有順序的可動列表)
L = ["Serena Lee", 8.21, 2025]
print(L)
print(L[0])
print(L[1])
print(L[-1])
print(L[0:2])
print(L[1:3])
L.extend(["pop", 13])
print(L)  # ans:['Serena Lee', 8.21, 2025, 'pop', 13] 增加兩個元素
L.append(["rock", 15]) 
print(L)  # ans:['Serena Lee', 8.21, 2025, 'pop', 13, ['rock', 15]] 增加一個元素

L1 = ["Serena Lee", 8.21, 2025, [2,3], ('A', 5)]
L2 = L + ["pop", 11]
print(L1)
print(L2)

A = ["rock", 10, 1.2, 5]
print(A)
A[0] = "hard rock"
print(A)  # ans:['hard rock', 10, 1.2, 5]
del(A[0])
print(A)  # ans:[10, 1.2, 5]

# Split: 將字符串轉為列表
print("hard rock".split())  # ans:['hard', 'rock']
print("A, B, C, D".split())  # ans:['A,', 'B,', 'C,', 'D']
print("A, B, C, D".split(","))  # ans:['A', ' B', ' C', ' D']

# Aliasing
C = ["big rock", 14, 1.99]
D = C
print(C)
print(D)
# C和D引用同一個對象:["big rock", 14, 1.99]

D[0] = "big rock"
C[0] = "watermelon" # C和D引用同一個對象，所以改變C的索引D也會一起變
print(C)  # ans:['watermelon', 14, 1.99]
print(D)  # ans:['watermelon', 14, 1.99]

E = ["orange", 18, 5.2]
F = E[:]  # clone相當於複製E的list
print(E)
print(F)
E[0] = "blueberry"
print(E)  # ans:['blueberry', 18, 5.2]
print(F)  # ans:['orange', 18, 5.2] 不會跟著變，因為是複製原本的list

# Dictionaries: use{}, key have to be immutable and unique. "key: value"
album = {"Thriller": 1982, "Back in Black": 1980, "The Dark Side of the Moon": 1973}
print(album)
print(album["Thriller"])
del(album["Back in Black"])
print(album)
print("The Dark Side of the Moon" in album)  # ans:Ture
print("Back in Black" in album)  # ans:False
print(list(album.keys()))
print(album.values())

# Sets集合: a type of Python collection, no orders(不記錄元素位置)
cities = {"Taipei", "London", "Taipei", "NewYork", "Berlin", "Tokyo"}
print(cities)  # ans:{'NewYork', 'London', 'Tokyo', 'Taipei', 'Berlin'} !實際創建後不會出現重複項目

# List covert to Set
cities_list = ["Taipei", "London", "Taipei", "NewYork", "Berlin", "Tokyo"]
cities_list2 = set(cities_list)
print(cities_list2)  # ans:{'Berlin', 'Taipei', 'Tokyo', 'London', 'NewYork'} !沒有重複項目

# Set Operations
g = {"abc", "efg", "ab/cd"}
print(g)
g.add("nyx")
print(g)  # ans:{'abc', 'nyx', 'ab/cd', 'efg'}
g.remove("nyx")
print(g)  # ans:{'abc', 'ab/cd', 'efg'}
print("ab/cd" in g)  # ans:True
print("abcdefg" in g)  # ans:False

# Set Mathemtaical
x = {"abc", "def", "gh/nm", 123}
y = {"abc", "def", "gh/em"}
z = x & y
print(z)  # ans:{'abc', 'def'}
print(x.union(y))  # .union包含兩個集合中的項目，ans:{'abc', 'def', 'gh/nm', 123, 'gh/em'}
print(z.issubset(x))  #ans:True














