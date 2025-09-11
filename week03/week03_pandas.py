import pandas as pd

df1 = pd.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]},
    index=[1, 2, 3]
)
# print(df1)
# print()
df2 = pd.DataFrame([
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
], columns=['A', 'B', 'C'], index=[1, 2, 3])
print(df2)

df3 = ((pd.melt(df2)
       .rename(columns={'variable':'var', 'value':'val'}))
       .query('val > 5'))
print(df3)