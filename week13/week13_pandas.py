import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

apple = pd.read_csv('APPL_price.csv')
print(apple.info())
apple['Date'] = pd.to_datetime(apple['Date']) # object -> datetime
print(apple.info())

#넘버를 날짜순으로 바꾸고 싶다.
apple = apple.set_index('Date') #index를 날짜시간 칼럼으로 대체
print(apple.info())

print(apple.tail())

#C계열 데이터 슬라이싱
print(apple['2022-06-14':'2022-06-16'])
print(apple['2022-04':'2022-06'])
#index로 바꿔놓았기 때문에 가능한 것이다


