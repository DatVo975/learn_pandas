import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('student.csv')
df2 = pd.read_csv('Student Depression Dataset.csv')

# Hợp nhất df1 và df2 trên cột 'id': {innner:trùng giá trị, outer:gộp chung, left:chỉ lấy df1, right: chỉ lấy df2}
df_merged = pd.merge(df1, df2, on='id', how='inner')
print(df_merged.head())

# Pivot table
df_pivot1 = df1.pivot_table(values='math.grade', index='nationality', columns='gender', aggfunc=['sum', 'mean'])
print(df_pivot1.head())
df_pivot2 = df1.pivot_table(values='english.grade', index='city', columns='gender', aggfunc='mean')
print(df_pivot2.head())

# Trực quan hoá cơ bản (Basic Visualization)
# df1.plot(kind='bar') # Vẽ biểu đồ cột cho cả csv
# df1['age'].hist() # Vẽ biểu đồ histogram

# df1['age'].value_counts().sort_index().plot(kind='bar')
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.title("Bar chart of Age")
# plt.show()

# Lấy các cột số
# numeric_df = df1.select_dtypes(include='number')

# # Vẽ bản đồ nhiệt, .corr() => tính ma trận tương quan, annot=T => tính ra số, cmap => chọn màu, vmax,vmin để chuẩn hoá màu từ -1 => 1
# sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', vmax=1, vmin=-1)
# plt.show()

mean_scores = df1.groupby('gender').agg({'sciences.grade':'mean'})
print(mean_scores)
mean_scores.plot(kind='bar')
plt.show()

score_colums = ['english.grade', 'math.grade', 'sciences.grade', 'language.grade']
score_df = df1[score_colums]
sns.heatmap(score_df.corr(), annot=True, cmap='coolwarm', vmax=1, vmin=-1)
plt.show()


