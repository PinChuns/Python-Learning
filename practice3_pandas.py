import pandas as pd
import numpy as np

sales = pd.Series([120, 350, 80, 500, 250])
print(sales)

sales2 = pd.Series(
    [120, 350, 80],
    index=["Jan", "Feb", "Mar"]
)
print(sales2)

# Numpy Array
numpy_sales = np.array([120, 350, 80])
print("NumPy:")
print(numpy_sales)
print(numpy_sales[1])

# Pandas Series
pandas_sales = pd.Series([120, 350, 80], index = ["Jan", "Feb", "Mar"], name = "sales3")
print("Pandas:")
print(pandas_sales)
print(pandas_sales["Feb"])
print(pandas_sales["Jan"])

# DataFrame
data = {
    "name": ["Alice", "Bob", "John"],
    "city": ["Taipei", "London", "Tokyo"],
    "sales": [850, 500, 720]
}
df = pd.DataFrame(data)
print(df)
print(df["name"])
print(df["sales"])
print(df["sales"].mean())
print(df.shape)
print(df.columns)
print(df.head(2))

# Little Test
data1 = {
    "name1": ["Alice", "Bob", "John"],
    "city1": ["Taipei", "London", "Tokyo"],
    "sales1": [850, 500, 720]
}
df1 = pd.DataFrame(data1)
print(df1["sales1"])
print(df1["sales1"].mean()) #()call the function
print(df1.shape)
print(df1.columns)
print(df1.head(2))

# Pandas (data filtering)
data2 = {
    "name2": ["Alice", "Bob", "John"],
    "city2": ["Taipei", "London", "Tokyo"],
    "sales2": [850, 500, 720]
}
df2 = pd.DataFrame(data2)
print(df2[df2["sales2"] >= 700]) #like SQL "WHERE sales >= 700;"
print(df2[(df2["sales2"] >= 700) & (df2["city2"] == "Taipei")]) #like SQL "WHERE sales >= 700 AND city = 'Taipei';"
print(df2[(df2["sales2"] >= 700) | (df2["city2"] == "London")]) #like SQL "WHERE sales >= 700 OR city = 'London'"
print(df2[["name2", "sales2"]])