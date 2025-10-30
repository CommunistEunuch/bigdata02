import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

german = pd.read_csv('german.csv')

#----------------------------------
#print(pd.cut(german['Age'], bins=8).reset_index().groupby('Age').size())

#qcut : quantity cut 인원수
print(pd.qcut(german['Age'], q=8).reset_index().groupby('Age').size())
#125*8 (x) -> 중복된 나이가 있기 때문에
print(german['Age'].value_counts().sort_values(ascending=False))
#사람을 반으로 자를 수는 없잖아요.. 정확하게 나눌 수가 없어요..
#대략 비율 별로 볼 때 쓴다. qcut은..




