import pandas as pd

data = [
    [1, 'A'],
    [2, 'B'],
    [3, 'C'],
    [4, 'D'],
    [5, 'E']
]

df = pd.DataFrame(data)
# df.columns = ['Column1', 'Column2']
print(df)