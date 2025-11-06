import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import xlabel
from sklearn.datasets import load_diabetes

#당뇨병 데이터셋 로딩

#numpy 값임
#shape 442,10
#target : array
#사이킷런 번치

diabetes = load_diabetes()
#print(diabetes.feature_names)
#print(diabetes)
#print(type(diabetes))

#print(diabetes.info()) #판다스 데이터 프레임이 아님.

#나이, 성별, BMI, 혈압, 총 콜레스테롤, 나쁜 콜레스테롤, 좋은 콜레스테롤, TCH(s1 / s3), LTG (로그로 변환된 중성 지방수치), 공복 혈당 수치

#print(diabetes.target) #당뇨병 진행 정도 값
#print(diabetes.data) #당뇨병 진행 정도 값

#데이터프레임 변환
#columns를 이미 있는 기준들을 가지고와서 적용
df_diabetes = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df_diabetes['target'] = diabetes.target
print(df_diabetes.info())

#지금 데이터가 z분포로 데이터가 변환이 되어있음 (스케일링: 표준평균분포도)
#(평균 분포를 0으로 기준잡아 고르게 분배시킴)

#print(df_diabetes['age'].describe())

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0, 0].hist(df_diabetes['s1'],bins=100) #빈도수 체크
axes[0, 0].set_title('Diabetes Data : TC distribution')
axes[0, 0].set_xlabel('Tc')
axes[0, 0].set_ylabel('Frequency')

#
axes[0, 1].boxplot([df_diabetes['s1'],df_diabetes['s2'],df_diabetes['s3']])
axes[0, 1].set_title('Diabetes Data : Boxplot')
axes[0, 1].set_xticklabels(['TC','LDL','HDL'])

#콜레스테롤의 수치와 당뇨와의 상관관계
axes[1, 0].scatter(df_diabetes['s1'],df_diabetes['target'], color='coral')
axes[1, 0].set_title('Diabetes Data : TC vs Progression')
axes[1,0].set_xlabel('')
axes[1,0].set_ylabel('')
#co-relation (상관 관계) (양이냐 음이냐)

#bmi지수에 따른 당뇨와의 상관관계
axes[1, 1].scatter(df_diabetes['bmi'],df_diabetes['target'], color='green', alpha=0.5)
axes[1, 1].set_title('Diabetes Data : bmi vs Progression')
axes[1, 1].set_xlabel('bmi')
axes[1, 1].set_ylabel('progression')

plt.show()

#
plt.figure(figsize=(12,8))
sns.histplot(df_diabetes['target'], color='blue',bins=10, kde=True)
plt.title('Histogram of Diabetes Progression (target)')
plt.xlabel('Diabetes Progression')
plt.ylabel('frequency')
plt.show()
#커널 밀도 함수로도 만들 수 있음 (추세선)


corr = df_diabetes.corr() #correlation (상관 관계)
print(corr)
#bmi지수가 target에서 제일 높음
#좋은 콜레스테롤이 제일 target에서 멈

#히트맵 만들기
#당뇨병 데이터셋 상관관계 히트맵
plt.figure(figsize=(12,10))
sns.heatmap(corr)
plt.show()

#데이터셋 각 블럭 수치화
plt.figure(figsize=(12,10))
sns.heatmap(corr, cmap="coolwarm", annot=True)
plt.show()

#꾸미기
plt.figure(figsize=(12,10))
sns.heatmap(corr, cmap="coolwarm", annot=True, fmt='.2f', linewidths=0.7)
plt.show()