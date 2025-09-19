import pandas as pd
df = pd.read_csv("student.csv")
print(df.head())
print(df.info())

# 1. Xử lí giá trị thiếu
df = df.dropna(axis=1) # Loại cột(1) hoặc hàng(0) có ít nhất 1 NaN
df = df.dropna(axis=1, how='all') # Chỉ loại bỏ hàng toàn NaN

df = df.fillna(0) # Điền giá trị vào các NaN

print(df.isnull().sum()) # Số lượng NaN theo cột

# 2. Tổng hợp và nhóm dữ liệu
new_df = df.groupby('gender').agg({'math.grade':'mean', 'sciences.grade':'sum'})
print(new_df)

# 3. Hàm apply và lambda
df['adjusted_age'] = df['age'].apply(lambda x: x + 2 if x > 18 else x - 1)

print(df.head())
print(df.info())