# Loop

# For Loop

# case1
squares = ["red", "yellow", "green", "purple", "blue"]
for i in range(0,5):
    squares[i] = "white"
    print(squares)

# case2
colors = ["red", "yellow", "green"]
for color in colors:
    print(color)

# case3: enumerate ans:['orange']
colors = ["red", "yellow", "green"]
for i, color in enumerate(colors):
    print(color)
    print(i)

# While Loop

# case1 ans:['orange', 'orange']
squares1 = ["orange", "orange", "purple", "orange", "blue"]
newsquares1 = []
i=0
while(squares1[i] == "orange"):
    newsquares1.append(squares1[i])
    i = i + 1
    print(newsquares1)

# range(n) = [0,....,(n-1)]
for x in range(3):
    print(x)

for y in range(0, 3):
    print(y)

#print(list(range(3)))  #[0, 1, 2]
#print(list(range(10, 15)))  #[10, 11, 12, 13, 14]



























