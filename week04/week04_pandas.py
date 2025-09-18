import pandas as pd
import numpy as np
import seaborn as sns

mpg = sns.load_dataset("mpg")
#print(mpg.info())

#맨처음 3개와 맨 나중 3개 출력
#print(mpg.head(3))
#print(mpg.tail(3))

#mpg를 기준으로 desc
#mpg_desc = mpg.sort_values(by=['mpg'], ascending=False)
#print(mpg_desc)

#요약 통계량 통계적 수치로 보여줘
#print(mpg.describe())

#수치 조건
#print(mpg[mpg['mpg']>40])
#print(mpg.query('mpg>40')) #편하게 쓸 수는 있지만 시간이 상대적으로 느림

#column기준 중복값 제거
#print(mpg.drop_duplicates())

#column 기준 중복값 제거
# df13 = pd.DataFrame({
#     'date':['2025-09-11','2025-09-11','2025-09-12','2025-09-11'],
#     'city':['서울', '안양','서울','안양'],
#     'temp':[23,22,24,22]
# }, index=[1,2,3,4])
# print(df13.drop_duplicates())

#df.sample 값 추출 (샘플 추출)
#print(mpg.sample(n=5))

#df.nl / df.ns 내부에서 정렬하여 나옴.
#print(mpg.nlargest(5, 'mpg'))
#print(mpg.nsmallest(5, 'mpg'))

#df 안보이는 부분 작성
#print(mpg[['displacement', 'horsepower', 'weight', 'acceleration', 'model_year']])

#iloc와 결합 혹은 loc
#print(mpg.iloc[:,2:7]) #2:7 (7 미포함)
#print(mpg.loc[:, 'displacement':'model_year']) #displacement : model_year (model_year 포함)

#정규표현식 mpg.filter(regex='')
#print(mpg.filter(regex='.me'))
#print(mpg.filter(regex='p..er'))


##print(mpg.value_counts())
# df = pd.DataFrame({
#     'city': ['seoul', 'anyang', 'incheon', 'seoul', 'seoul', 'anyang'],
#     'name': ['tom', 'jerry', 'kim', 'park', 'lee','kim']}
#     , index=[1, 2, 3, 4, 5, 6])
# print(df)
# print(df.value_counts())
# print(df['city'].nunique())


##df.apply #람다 사용 가능
#df = pd.DataFrame([
#    [1, 4, 7],
#    [2, 5, 8],
#    [3, 6, 9]
#], columns=['A', 'B', 'C'], index=[1, 2, 3])

#print(df) #기본 출력
#print(df.apply(lambda x : x*x)) #배수 출력
#print(df.apply(lambda z : z**3)) #세제곱 출력

#결집갑 찾기
#print(mpg.isnull().sum())
#print(mpg.isnull())
#print(mpg[mpg['horsepower'].isnull()])

###중요한 부분이에오
##1. 결측치 처리 (null이나 NA가 하나라도 있으면 해당하는 데이터 날리기
#mpg = mpg.dropna()
#print(mpg[mpg['horsepower'].isnull()])
#print(mpg.info())


##2. 결측치 처리 (null이나 NA가 하나라도 있는 데이터에 값을 넣기 (평균, 표준값))
#mpg = mpg.fillna(mpg['horsepower'].mean())
#print(mpg[mpg['horsepower'].isnull()])
#print(mpg.info())

##결측치 처리시 해당하는 데이터셋 바로 업데이트
#mpg.fillna(inplace=True)