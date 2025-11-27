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

#값이 완전 일치는 없음
#print(pi[pi['standard1'] == 0])
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
#-------------------------------------------------

pr = pd.read_csv('product.csv')
# print(pr.info())
# print(pr.describe())
# print(pr.tail(3))
# print(pr.head(3))

#차대번호에서 작업자

print(pr['operator'].unique())
print(pr['process'].unique())
print(pr['factory'].unique())
print(pr.tail(3))
print(pr.head(3))

#생산 공정에서의 책임자를 _로 한 문장으로 볼 수 있게 만듦
#product_id를 기준으로 operator ---> path
pr['path'] = pr.groupby('product_id')['operator'].transform(lambda x: '_'.join(x))
print(pr.head(6))

#차대번호 포함
pr['path'] = pr['factory'] + '_' + pr['path']
print(pr.head(6))

#id가 항상 3개인걸 하나로 묶어버림
pr = pr.drop_duplicates('product_id')
print(pr)

#간략화
pr = pr[['date', 'product_id', 'passfail', 'path']]
print(pr)

#갯수를 셀 겁니다
print(pr.groupby('passfail')['path'].value_counts())

#------------------------#분기점___________________
#factory 만들기
pr['factory'] =pr['path'].map(lambda x: x[0:2]) #factory코드만 추출
#print(pr.tail())

#factory 분리
pr['path'] = pr['path'].map(lambda x : x[3: ]) #slice 3열부터 끝까지 추출
#print(pr)

#split _ 로 해서 분리시키기 (구분자 _로 리스트로 리턴)
pr['path'] = pr['path'].map(lambda x : x.split('_'))
#print(pr)

#path칼럼의 데이터를 기준으로 행으로 분리 (1-> 3)
pr = pr.explode('path')
print(pr.tail(15))

#process가 모호하여 map을 가지고 path의 값을 기준으로 3가지의 구분을 지어 재생성
process_map = { # map : dictionary로 표현
    '1':'P1',
    '2':'P1',
    'V':'P2',
    'W':'P2',
    'X':'P3',
    'Y':'P3'
}
pr['process'] = pr['path'].map(process_map)
print(pr)

#rename 함수를 이용하여 컬럼의 이름 바꾸기
pr = pr.rename({'path':'operator'}, axis =1)
print(pr)

#----------------------------------------------------------

