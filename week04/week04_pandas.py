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