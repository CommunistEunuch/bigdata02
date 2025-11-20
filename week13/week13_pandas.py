import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

apple = pd.read_csv('APPL_price.csv')
apple['Date'] = pd.to_datetime(apple['Date']) # object -> datetime
#넘버를 날짜순으로 바꾸고 싶다.
apple = apple.set_index('Date') #index를 날짜시간 칼럼으로 대체
# print(apple.head())
# apple = apple.reset_index()
# print(apple.head())

print(apple.isnull())
print(apple.isnull().sum())
print(apple['Close'].max())
print(apple['Close'].min())

#일일 수익률 계산 결과 칼럼 추가
apple['Daily_Return'] = apple['Close'].pct_change() *100
print(apple['Close','Daily_Return'])
#일일 가격 변화 (달러)
apple['Price_Change'] =apple['Close'].diff()
print(apple[['Close','Price_Change']])

#일일 가격 변동폭(%)
apple['High_Low_Range'] = ((apple['High'] - apple['Low']) / apple['Low'])
print(apple['High','Low','High_Low_Range'])

#이동평균 (20일)
apple['MA_20'] = apple['Close'].rolling(window=20).mean()
print(apple['MA_20'].head(20))

#변동성 (20일 표준편차)
apple['Volatility'] = apple['Daily_Return'].rolling(window=20).std()
# print(apple['Volatility'])

# print(apple.info())
apple = apple.reset_index()
print(apple[['Date', 'Close', 'Daily_Return', 'MA_20', 'Volatility']].tail(10))