import pandas as pd



df = pd.read_csv('input.txt', sep=',', escapechar='\\',
                  encoding="utf-16")
df['2010'] = pd.to_numeric(df['2010'], errors='coerce')

print(df['2010'].sum())
df.rename(columns={'year':'country'},inplace=True)
df.set_index('country', inplace=True)


