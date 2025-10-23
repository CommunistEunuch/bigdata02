import matplotlib.pyplot as plt
import pandas as pd

#DataFrame 객체
uber = pd.read_csv("Uber.csv")
#원본을 아는 것이 중요하다

#print(uber.head())
#print(uber.info()) #7개의 columns 1개의 float, purpose는 결측값이 상당함

#1년간의 공유택시 기록. 컬럼 7개, 1156개의 행, 수치형 1개 외에는 object,
# purpose는 운행목적이 필수가 아니기에 누락이 많은 것으로 추정

#print(uber.describe()) #수치형 데이터 통계
#최솟값과 최댓값에서 데이터 수치가 이상함

#print(uber[uber["MILES*"] ==12204.7]) #describe
#print(uber[uber["MILES*"] == uber["MILES*"].max()]) #max
#print(uber.tail()) #여기서 맨 마지막 행이 총 합을 적어놓은 것이라고 알 수 있음

#특정 행 값을 날려버리는 방법
#uber = uber.drop(1155)
#print(uber.tail())
#print(uber.describe())

########################################################

#에러를 처리하는 방법(datetime 안에 있는) 날짜 시간으로 데이터 변환
#uber['START_DATE*'] = pd.to_datetime(uber['START_DATE*'])
#print(uber)

#error='coerce'를 쓰면 에러를 처리할 수 있다. (각 행에서 보이도록)
uber['START_DATE*'] = pd.to_datetime(uber['START_DATE*'], errors='coerce')
uber['END_DATE*'] = pd.to_datetime(uber['END_DATE*'], errors='coerce')
#print(uber)

uber = uber.sort_values(['START_DATE*', 'END_DATE*'])
#print(uber)

#따라서 Dtype도 바뀐다.
#print(uber.info())

#곂치는거 솎아내기
#print(uber['START_DATE*'].unique())
#print(uber['END_DATE*'].unique())


#활용 -->
#uber = uber.drop(1155)
#print(uber['END_DATE*'].unique())
#print(uber[uber['MILES*'] == uber['MILES*'].max()])


#_#_#_#_#_#_#_#_#

#이용 사유 보기
#print(uber['PURPOSE*'].value_counts())

#이동 사유가 없는 것 보기
#print(uber['PURPOSE*'].isna().sum())

#새로운 컬럼 만들기 (걸린 시간)
uber['DURATION*'] = (uber['END_DATE*'] - uber['START_DATE*'])
#print(uber['CATEGORY*'].value_counts())

# VVVVV 활용하는 방법 VVVVV
#print(uber.groupby(['CATEGORY*', 'PURPOSE*'])[['MILES*']].agg(['mean', 'std'])) #산술 평균, 표준 편차

#print(uber[uber['PIRPOSE*'] == 'Airport/Travel']['MILES*'])

#print(uber.groupby(['CATEGORY*', 'PURPOSE*'])[['MILES*','DURATION*']].agg(['mean', 'median', 'std'])) #산술 평균, 표준 편차

#print(uber[uber['PURPOSE*'] == 'Airport/Travel'][['MILES*', 'DURATION*']])


#시각화
import seaborn as sns
from scipy.stats import linregress


uber = uber.drop(1155)
uber['DURATION*'] = (uber['END_DATE*'] - uber['START_DATE*']).dt.total_seconds() / 60

slope, intercept, r, _, _ = linregress(uber["MILES*"], uber["DURATION*"])
# print(slope)
# print(intercept)
# print(r)

sns.regplot(x='MILES*', y='DURATION*', data=uber,
           line_kws={'label': f'y={slope:.2f}x+{intercept:.2f}, R^2={r:.2f}'})
plt.legend()
plt.show()