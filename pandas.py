import pandas as pd


# Pandas: Loading Data


Pandas
read_csv()
Series()
DataFrame
values
...
...
...


# Importing
csv_path = 'file1.csv'
df = pd.read_csv(csv_path)    # df=dataframe縮寫
df.head()    # 讀取dataframe前五行

# read excel
xlsx_path = 'file1.xlsx'
df = pd.read_excel(xlsx_path)
df.head()


# 用dict創建DF

sales = {'city':['Taipei','London','Berlin'],\
         'sale':[1000, 5000, 550],\
         'date':['20250809','20250910','20250917']
}
sales_fram = pd.DataFrame(sales)
print(sales_fram)