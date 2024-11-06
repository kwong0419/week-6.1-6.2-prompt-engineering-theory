import pandas as pd

df = pd.read_csv('./data.csv')
# print(df['username'])
print(df['gpa'].median())