# Python Learning

My Python learning notes and practice for Data Analytics and Python fundamentals.

---

# Python Basics

## Variables and Data Types

- Variables
- `int` — integer
- `float` — decimal number
- `str` — string
- `bool` — Boolean value

### Number Systems

Python integers can also be written in different number systems:

```python
print(0b100)  # Binary
print(0o100)  # Octal
print(100)    # Decimal
print(0x100)  # Hexadecimal
```

---

## Variable Naming

Variable names can contain:

- Letters
- Numbers
- Underscores `_`

Rules:

- Variable names cannot start with a number.
- Special characters such as `!`, `@`, and `#` cannot be used.
- Python is case-sensitive.

Example:

```python
A = 10
a = 20
```

`A` and `a` are different variables.

Variable names should not use Python keywords such as:

```text
if
else
for
while
True
False
```

It is also better to avoid overwriting Python built-in names such as:

```text
int
str
print
input
```

---

## Using Variables

Variables can store values:

```python
a = 59
b = 11
```

Variables can also be used in calculations:

```python
print(a, b)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
```

---

## Check Variable Type

Use `type()` to check the data type of a variable.

```python
a = 98
b = 456.23
c = "hello, world"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

# Type Conversion

Python can explicitly convert one data type into another.

This is called **Type Casting**.

## `int` → `float`

```python
a = 100

print(float(a))
```

Output:

```text
100.0
```

---

## `float` → `int`

```python
b = 123.45

print(int(b))
```

Output:

```text
123
```

`int()` removes the decimal part. It does not round the number.

---

## `str` → `int`

```python
c = "123"

print(int(c))
```

---

## Base Conversion

```python
print(int("123", base=16))
```

Converts `"123"` from hexadecimal to an integer.

```python
print(int("100", base=2))
```

Converts binary `"100"` to an integer.

---

## `str` → `float`

```python
e = "123.45"

print(float(e))
```

---

## `str` → `bool`

```python
f = "hello, world"

print(bool(f))
```

A non-empty string returns:

```text
True
```

---

## `bool` → `int`

```python
g = True

print(int(g))
```

Python represents:

```text
True  → 1
False → 0
```

---

## `int` → Character

```python
a = 100

print(chr(a))
```

Output:

```text
d
```

---

## Character → Unicode Number

```python
print(ord("d"))
```

Output:

```text
100
```

---

# Python Operators

## Arithmetic Operators

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor Division |
| `%` | Modulus / Remainder |
| `**` | Exponent |

Example:

```python
print(321 + 12)
print(321 - 12)
print(321 * 12)
print(321 / 12)
print(321 // 12)
print(321 % 12)
print(321 ** 12)
```

---

# Operator Precedence

Python operators follow an order of precedence:

```text
1. ()
2. **
3. * / // %
4. + -
```

Example:

```python
result1 = 2 + 3 * 4
```

The multiplication happens first:

```text
2 + 12 = 14
```

Using parentheses:

```python
result2 = (2 + 3) * 4
```

Result:

```text
20
```

---

## Exponent Associativity

```python
result3 = 2 ** 3 ** 2
```

Python evaluates this from right to left:

```python
2 ** (3 ** 2)
```

So:

```text
2 ** 9 = 512
```

It is not:

```text
(2 ** 3) ** 2 = 64
```

---

# Assignment Operators

Common assignment operators:

```text
=
+=
-=
*=
/=
//=
%=
**=
```

Example:

```python
a = 7
b = 3

a += b
```

This is equivalent to:

```python
a = a + b
```

Another example:

```python
a *= a + 2
```

This is equivalent to:

```python
a = a * (a + 2)
```

---

# Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

---

# Logical Operators

## `and`

Both conditions must be `True`.

```python
True and True
```

Result:

```text
True
```

---

## `or`

At least one condition must be `True`.

```python
True or False
```

Result:

```text
True
```

---

## `not`

Reverses a Boolean value.

```python
not True
```

Result:

```text
False
```

Example:

```python
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1

flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0

print(flag0)
print(flag1)
print(flag2)
print(flag3)
print(flag4)
print(flag5)
```

---

# Conditional Statements

Python uses:

```text
if
elif
else
```

Example:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: C")
```

---

# List

- `[]` — create a list
- `list[index]` — access an element by index
- `list[-1]` — access the last element
- `list[start:end]` — slicing
- `list[index] = value` — modify an element

Example:

```python
price = [100, 250, 80, 500, 300]

print(price)
print(price[0])
print(price[-1])

price[3] = 550

print(price)
```

---

# Loops

Python mainly uses:

```text
1. for loop
2. while loop
```

There are also loop control statements:

```text
break
continue
```

---

# For Loop

A `for` loop is used to iterate over a sequence.

Example:

```python
for item in items:
    print(item)
```

---

## `range()`

### `range(stop)`

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

`range()` starts from `0` by default.

The stop value is not included.

---

### `range(start, stop)`

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

`6` is not included.

---

### `range(start, stop, step)`

```python
for i in range(0, 10, 2):
    print(i)
```

Output:

```text
0
2
4
6
8
```

---

# For + If

Use a `for` loop with an `if` condition to filter or process data.

```python
sales = [120, 350, 80, 500, 250]

for sale in sales:
    if sale >= 200:
        print(sale)
```

---

# While Loop

A `while` loop continues running while its condition is `True`.

Example:

```python
total = 0
i = 1

while i <= 100:
    total += i
    i += 1

print(total)
```

This calculates the sum from `1` to `100`.

---

# Loop Control Statements

## `break`

`break` immediately terminates the entire loop.

Example:

```python
for i in range(1, 6):
    if i == 3:
        break

    print(i)
```

Output:

```text
1
2
```

---

## `continue`

`continue` skips the current iteration and continues with the next iteration.

Example:

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

---

# Nested Loops

A loop can contain another loop.

Example: multiplication table.

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}×{j}={i * j}", end="\t")
    print()
```

---

# Dictionary

A Dictionary stores data using **key-value pairs**.

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

---

# Functions

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

Another example:

```python
def check_sales(sales):
    if sales >= 500:
        return "High"
    else:
        return "Low"

print(check_sales(800))
print(check_sales(300))
```

---

# String Methods

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
print(name.replace("Leona", "Linda"))
print(len(name))

print("Hello " + name)
print(f"Hello {name}")

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

# NumPy

Import:

```python
import numpy as np
```

## Array

- `np.array()` — create a NumPy array
- `.shape` — view the shape of an array
- `.dtype` — view the data type of an array

Example:

```python
sales = np.array([100, 200, 300, 500])
```

---

## Indexing and Slicing

- `array[0]` — select the first element
- `array[-1]` — select the last element
- `array[start:end]` — select a range of elements
- `array[2:]` — select elements from index `2` to the end

Example:

```python
print(sales[0])
print(sales[-1])
print(sales[1:3])
print(sales[2:])
```

---

## Array Operations

NumPy arrays allow calculations to be applied to all elements.

```python
print(sales * 2)
print(sales + 100)
```

- `array * 2` — multiply each element by `2`
- `array + 100` — add `100` to each element

---

## Boolean Indexing

Use a condition to filter elements.

```python
print(sales[sales >= 300])
```

This selects elements that meet the condition.

---

## Statistics

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

---

## Shape

`.shape` shows the dimensions of an array.

Example:

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

For a 2D array:

```text
(rows, columns)
```

---

## 2D Array Indexing

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

# Series

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

---

## Custom Index

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

---

## Series Name

A Series can have a name:

```python
sales = pd.Series(
    [120, 350, 80],
    index=["Jan", "Feb", "Mar"],
    name="sales"
)
```

---

# DataFrame

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

---

## Select a Column

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

---

## Series vs DataFrame

```text
Series
→ one column of data

DataFrame
→ multiple columns / a table
```

---

# DataFrame Basic Information

## `.shape`

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

---

## `.columns`

View the column names:

```python
print(df.columns)
```

Example output:

```text
Index(['name', 'city', 'sales'], dtype='object')
```

---

## `.head()`

View the first rows of a DataFrame.

```python
print(df.head())
```

By default, `.head()` shows the first `5` rows.

You can specify the number of rows:

```python
print(df.head(2))
```

This shows the first `2` rows.

---

# DataFrame Calculations

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

## Single Condition

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

# Multiple Conditions

Pandas uses:

- `&` — AND
- `|` — OR

## AND

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

---

## OR

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

---

## Important Rule

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

# Select Multiple Columns

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