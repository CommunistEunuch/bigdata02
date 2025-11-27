import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pi = pd.read_csv('product_inspection.csv')
#print(pi)
#print(pi.info()) #결측값 확인용
#print(pi.describe()) #수치데이터

pi['date'] = pd.to_datetime(pi['date'])
#print(pi.info())
#print(pi[pi['inspection_step'] == 'B'])
#print(pi['inspection_step'].unique())
#print(pi.groupby('inspection_step')['value'])
#print(pi.groupby('inspection_step')['value'].mean())
#print(pi.groupby('inspection_step')['value'].describe())
#데이터 분석을 하고 싶으면 판다스 잘 써라

#새로운 특성을 만들자
#normalize

#표준정규분포도
pi['standard1'] = pi.groupby('inspection_step')['value'].transform(lambda x: (x-x.mean()) / x.std())
#print(pi.head())
#print(pi.groupby('inspection_step')['value'].describe()) #groupby 놓치지마요

#표준정규분포의 -부분만 보고 싶다
#print(pi[pi['standard1']<0])
#그 반대
#print(pi[pi['standard1']>0])

#정렬 (날짜기준)
temp = pi.sort_values(['inspection_step','date']).drop_duplicates(['inspection_step'])
#각 A, B, C의 첫행만 나오게끔 정렬
print(temp)

temp = temp.set_index('inspection_step')['value']

#현재 값에서 표준정규분포값을 뺀 값으로 정렬
print(pi)
pi['standard2'] = pi['value'] - temp
print(pi['standard2'])

pi = pi.reset_index()