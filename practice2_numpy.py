import numpy as np

Sales = [100, 200, 300, 500]
print(Sales * 2)

sales = np.array([100, 200, 300, 500])
print(sales)
print(sales * 2)
print(sales + 100)

# 1D array indexing
print(sales [0])
print(sales [-1])
print(sales[1:3])
print(sales[:2])
print(sales[2:])

# Boolean indexing
print(sales[sales >= 300])

# Shape: return the shape(row, column) of an array.
print(sales.shape)

# Operation
print(sales.sum())
print(sales.mean())
print(sales.max())
print(sales.min())

# Reshape
sales2 = sales.reshape(2,2)
print(sales2[1,1])  #check

sales3 = np.array([[100, 200, 300, 500], [800, 900, 700, 400]])
print(sales3.shape)
# 2D array indexing
print(sales3[0, 0])
print(sales3[1, 2])

# dtype = data type
print(sales3.dtype)

# Little Test
nums = np.array([120, 350, 80, 500, 250])
print(nums[0])
print(nums[-1])
print(nums[1:3])
print(nums[2:])
print(nums * 2)
print(nums + 100)
print(nums[nums>=300])
print(nums.sum())
print(nums.mean())
print(nums.max())
print(nums.min())
print(nums.shape)
print(nums.dtype)
nums2 = np.array([
    [100, 200, 300],
    [400, 500, 600]
])
print(nums2.shape)
print(nums2[1, 1])