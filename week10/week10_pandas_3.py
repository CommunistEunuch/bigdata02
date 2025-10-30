import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

s1 = pd.Series([0,0,1,1,0,1,1,1,1,0,1])
print(s1)

#누적합
#cumulative sum

#cumsum <-- 판다스
sc1 = s1.cumsum()
print(sc1)

#대응되는 값을 서로 곱함
print(s1.mul(sc1)) #multiply

#--------------
#diff
#빼기 (difference)
#현재 값과 이전 값과의 차이
print(s1.mul(sc1).diff())
#이 값에서만 적용되는거 다시 리마인드

#-------------------
#where(조건에 맞는것만 필터링해서 보고 싶다)
print(s1.mul(sc1).diff().where(lambda n:n<0))
print(s1.mul(sc1).diff().where(lambda n:n>0).ffill())
s1.mul(sc1).diff().where(lambda n:n>0).ffill().add(sc1, fill_value=0)

#-----------------------

wh = pd.read_csv('wh.csv')
#print(wh.describe())

###아웃라이어에 대한 값을 어떻게 할 것인가?
sns.scatterplot(x='Weight', y='Height', data=wh)
plt.show()