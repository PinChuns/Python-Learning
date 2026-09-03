# Python Learning

My Python learning notes and practice for Data Analytics.

---

## Python Basics

### Variables and Data Types

- Variables
- `int` — integer
- `float` — decimal number
- `str` — string
- `bool` — Boolean value

### List

- `[]` — create a list
- `list[index]` — access an element by index
- `list[-1]` — access the last element
- `list[start:end]` — slicing
- `list[index] = value` — modify an element

### If Statement

```python
if condition:
    ...
else:
    ...
```

### For Loop

```python
for item in items:
    ...
```

### For + If

Use a `for` loop with an `if` condition to filter or process data.

```python
for item in items:
    if condition:
        print(item)
```

### Dictionary

- `{}` — create a dictionary
- `dict["key"]` — access a value by key
- `dict["key"] = value` — modify a value

Example:

```python
customer = {
    "name": "Linda",
    "age": 21,
    "city": "Taipei",
    "sales": 850
}

print(customer["name"])
```

### Functions

- `def` — define a function
- parameter — input passed to a function
- `return` — return a result
- `function()` — call a function

Example:

```python
def square(x):
    return x * x

print(square(5))
```

### String Methods

- `.upper()` — convert to uppercase
- `.lower()` — convert to lowercase
- `.replace()` — replace text
- `len()` — get string length
- `+` — concatenate strings
- `f"..."` — formatted string

Example:

```python
name = "Leona"
age = 25

print(name.upper())
print(name.lower())
print(len(name))
print(f"My name is {name}, and I am {age}.")
```

---

# Libraries

## math

Import:

```python
import math
```

Common functions and constants:

- `math.sqrt()` — square root
- `math.pow()` — power
- `math.floor()` — round down
- `math.ceil()` — round up
- `math.fabs()` — absolute value
- `math.pi` — pi

Example:

```python
import math

print(math.sqrt(16))
print(math.pow(5, 2))
print(math.floor(3.14))
print(math.ceil(3.65))
print(math.fabs(-8))
print(math.pi)
```

---

## NumPy

Import:

```python
import numpy as np
```

### Array

- `np.array()` — create a NumPy array
- `.shape` — view the shape of an array
- `.dtype` — view the data type of an array

Example:

```python
import numpy as np

sales = np.array([100, 200, 300, 500])
```

### Indexing and Slicing

- `array[0]` — select the first element
- `array[-1]` — select the last element
- `array[start:end]` — select a range of elements
- `array[2:]` — select elements from index 2 to the end

Example:

```python
print(sales[0])
print(sales[-1])
print(sales[1:3])
print(sales[2:])
```

### Array Operations

NumPy arrays allow calculations to be applied to all elements.

```python
print(sales * 2)
print(sales + 100)
```

- `array * 2` — multiply each element by 2
- `array + 100` — add 100 to each element

### Boolean Indexing

Use a condition to filter elements.

```python
print(sales[sales >= 300])
```

This selects elements that meet the condition.

### Statistics

- `.sum()` — calculate the sum
- `.mean()` — calculate the average
- `.max()` — find the maximum value
- `.min()` — find the minimum value

Example:

```python
print(sales.sum())
print(sales.mean())
print(sales.max())
print(sales.min())
```

### Shape

`.shape` shows the dimensions of an array.

For example:

```python
sales = np.array([100, 200, 300, 500])

print(sales.shape)
```

Output:

```text
(4,)
```

A two-dimensional array:

```python
sales2 = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

print(sales2.shape)
```

Output:

```text
(2, 3)
```

`shape` is represented as:

```text
(rows, columns)
```

### 2D Array Indexing

For a two-dimensional array:

```python
sales2[row, column]
```

Example:

```python
print(sales2[0, 0])
print(sales2[1, 1])
```

---

## pandas

Common functions and methods:

### Data Loading

- `pd.read_csv()` — read a CSV file
- `pd.read_excel()` — read an Excel file

### DataFrame

- `pd.DataFrame()` — create a DataFrame
- `.head()` — view the first rows
- `.tail()` — view the last rows
- `.info()` — view DataFrame information
- `.describe()` — view descriptive statistics
- `.shape` — view the number of rows and columns
- `.columns` — view column names