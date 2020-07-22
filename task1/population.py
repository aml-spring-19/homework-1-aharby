import pandas as pd


df = pd.read_csv('input.txt', sep=',', escapechar='\\',
                 index_col=0, encoding="utf-16")
print(df)
fhgaewhkahfskdf