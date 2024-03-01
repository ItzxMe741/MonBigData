import pandas as pd

# đọc file csv chứa dữ liệu vào DataFrame
df = pd.read_csv('D:/HKII-Năm 4/Big Data/XuLySongSong/csv/17042023.csv', encoding="utf8")

# xóa hết dấu chấm trong cột Tổng số ca
df['Tổng số ca'] = df['Tổng số ca'].str.replace('.', '')
df['Tử vong'] = df['Tử vong'].apply(str).str.replace('.', '')


# in kết quả
print(df)