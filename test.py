
x=[[1,2,3,4,5], 
   [6,7,8,9,10]]
print(x)


x=[[1,2,3,4,5], [6,7,8,9,10]]
for row in x:
    print(*row)

x = [
    [1, 2, 3],
    [4, 5, 6]
]
for y in x:
    print(sum(y))

x = [
    [3, 8, 2],
    [10, 5, 7],
    [4, 6, 1]
]

max_num = 0
for z in x:
    row_max = max(z)

    if row_max > max_num:
        max_num = row_max

print(max_num)


x = [1, 4, 7, 10, 12, 15]

q = 0

for i in x:
    if i % 2 == 0:
        q = q + 1

print(q)


        