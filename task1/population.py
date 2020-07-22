import pandas as pd



df = pd.read_csv('input.txt', sep=',', escapechar='\\',
                  encoding="utf-16")
df['2010'] = pd.to_numeric(df['2010'], errors='coerce')

print(df['2010'].sum())
df.rename(columns={'year':'country'},inplace=True)
df.set_index('country', inplace=True)




def test_row():
    """Check row number in df."""
    assert len(df) == 225


def test_column():
    """Check column number in df."""
    assert len(df.columns) == 31


def test_population():
    """Check sum of '2010' column in df."""
    assert round(df['2010'].sum()) == 7065