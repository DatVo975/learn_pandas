import pandas as pd

# Đọc file CSV vào DataFrame
df = pd.read_csv("student.csv")

# Xem dữ liệu
print("5 dòng đầu:")
print(df.head())

# Thông tin bảng
print("\nThông tin bảng:")
print(df.info())

# Thống kê
print("\nThống kê dữ liệu:")
print(df.describe())

# Kích thước của dataframe
print("\nKích thước:")
print(df.shape)

# Tên các cột
print("\nTên các cột:")
print(df.columns)

# Kiểu dữ liệu các cột
print("\nKiểu dữ liệu các cột")
print(df.dtypes)

# Tính điểm trung bình
print("\nĐiểm trung bình:", df["english.grade"].mean())

# Truy cập dữ liệu trong data frame
print(df.loc[0, 'name'])
print(df.iloc[0, 1])
print(df.at[1, 'name'])
print(df.iat[1, 1])

# Tạo cột mới, xoá cột
df["sci+lang_score"] = df["sciences.grade"] + df["language.grade"]
df = df.drop(columns='sci+lang_score')

# Lọc sinh viên có điểm >= 3
print("\nSinh viên có điểm >= 3:")
print(df[df["english.grade"] >= 3])
