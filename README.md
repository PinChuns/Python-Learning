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

# Pandas

## Import

```python
import pandas as pd
```

---

## Series

A Pandas Series is a one-dimensional data structure with an index.

Example:

```python
sales = pd.Series([120, 350, 80, 500, 250])

print(sales)
```

Output:

```text
0    120
1    350
2     80
3    500
4    250
dtype: int64
```

Pandas automatically creates an index starting from `0`.

### Custom Index

You can specify your own index labels:

```python
sales = pd.Series(
    [120, 350, 80],
    index=["Jan", "Feb", "Mar"]
)

print(sales)
```

Output:

```text
Jan    120
Feb    350
Mar     80
```

Access data by label:

```python
print(sales["Feb"])
```

Output:

```text
350
```

### Series Name

A Series can have a name:

```python
sales = pd.Series(
    [120, 350, 80],
    index=["Jan", "Feb", "Mar"],
    name="sales"
)
```

---

## DataFrame

A DataFrame is a two-dimensional table made up of rows and columns.

It can be thought of as multiple Series combined into a table.

Example:

```python
data = {
    "name": ["Alice", "Bob", "John"],
    "city": ["Taipei", "London", "Tokyo"],
    "sales": [850, 500, 720]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    name    city  sales
0  Alice  Taipei    850
1    Bob  London    500
2   John   Tokyo    720
```

### Select a Column

Select one column:

```python
print(df["name"])
```

Selecting one column returns a Series.

```text
DataFrame
    ↓
df["name"]
    ↓
Series
```

### Series vs DataFrame

```text
Series
→ one column of data

DataFrame
→ multiple columns / a table
```

---

## DataFrame Basic Information

### `.shape`

View the number of rows and columns:

```python
print(df.shape)
```

Example output:

```text
(3, 3)
```

This means:

```text
3 rows
3 columns
```

### `.columns`

View the column names:

```python
print(df.columns)
```

Example output:

```text
Index(['name', 'city', 'sales'], dtype='object')
```

### `.head()`

View the first rows of a DataFrame.

```python
print(df.head())
```

By default, `.head()` shows the first 5 rows.

You can specify the number of rows:

```python
print(df.head(2))
```

This shows the first 2 rows.

---

## DataFrame Calculations

Select a column and use a method to calculate values.

Example:

```python
print(df["sales"].mean())
```

Output:

```text
690.0
```

Important:

```python
.mean
```

refers to the method itself.

```python
.mean()
```

calls / executes the method.

```text
.mean
→ the method

.mean()
→ execute the method
```

---

# Pandas Data Filtering

Pandas can filter rows based on conditions.

This is similar to SQL `WHERE`.

### Single Condition

SQL:

```sql
SELECT *
FROM table
WHERE sales >= 700;
```

Pandas:

```python
df[df["sales"] >= 700]
```

The condition:

```python
df["sales"] >= 700
```

produces a Boolean Series:

```text
True
False
True
```

Pandas keeps the rows where the condition is `True`.

---

## Multiple Conditions

Pandas uses:

- `&` — AND
- `|` — OR

### AND

SQL:

```sql
WHERE sales >= 700
AND city = 'Taipei'
```

Pandas:

```python
df[
    (df["sales"] >= 700)
    &
    (df["city"] == "Taipei")
]
```

### OR

SQL:

```sql
WHERE sales >= 700
OR city = 'London'
```

Pandas:

```python
df[
    (df["sales"] >= 700)
    |
    (df["city"] == "London")
]
```

### Important Rule

When using multiple conditions in Pandas:

**Each condition must be wrapped in `()` parentheses.**

Use:

```python
(condition1) & (condition2)
```

or:

```python
(condition1) | (condition2)
```

Do not directly use Python's `and` / `or` for Pandas Series conditions.

Why?

Because Pandas conditions produce a whole Series of `True` / `False` values, so Pandas needs to perform the logical operation element by element.

Example:

```text
Condition 1     Condition 2       AND (&)

True            True              → True
False           False             → False
True            False             → False
```

---

## Select Multiple Columns

Select one column:

```python
df["name"]
```

→ returns a Series.

Select multiple columns:

```python
df[["name", "city", "sales"]]
```

→ returns a DataFrame.

The inner `[]` is a Python list of column names.

```text
One column:

df["sales"]
→ Series


Multiple columns:

df[["name", "city", "sales"]]
→ DataFrame
```

The number of selected columns does not determine the number of brackets.

```python
df[["name", "city"]]

df[["name", "city", "sales"]]

df[["name", "city", "sales", "age"]]
```

All use two levels of `[]`.