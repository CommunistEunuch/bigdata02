import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df =sns.load_dataset('titanic')

#각종 정보 확인
print(df.head())
print(df.info()) #중간 생략된 것 볼 수 있음 (결측값도 볼 수 있음)
print(df.describe()) #수치형 데이터 요약 통계


# #그 날 탑승한 나이 확인하고 싶어서 만듦
# #데이터 시각화
# plt.figure(figsize=(8,4))#그래프 해상도 설정
# sns.histplot(data=df, x="age", bins=16, kde=True) #x축 y축 설정 (x축 bins:분포 섹션 나누기, KDE : 추세선)
# plt.title("Age Distrubution of Passengers") #title
# plt.ylabel('Frequency') #y축
# plt.xlabel('Age') #x축
# plt.tight_layout()#화면 채우기 (안써도됨)
# plt.show()#그리기

#생존자 생존하지 않은 자
# plt.figure(figsize=(8,4))#그래프 해상도 설정
# sns.countplot(data=df, x="survived") #x축 y축 설정 (x축 bins:분포 섹션 나누기, KDE : 추세선)
# plt.title("Survivors vs Non-Suvivor", fontsize=14) #title
# plt.ylabel('survived (0: No, 1: Yes)') #y축
# plt.xlabel('Counter') #x축
# #plt.tight_layout()#화면 채우기 (안써도됨)
# plt.show()#그리기

#좌석 등급에 따른 사람 수
# plt.figure(figsize=(8,4))#그래프 해상도 설정
# sns.countplot(data=df, x="class", order=["First","Second", "Third"]) #x축 y축 설정 (x축 bins:분포 섹션 나누기, KDE : 추세선)
# plt.title("Passenger Count by Class", fontsize=14) #title
# plt.ylabel('class') #y축
# plt.xlabel('Count') #x축
# #plt.tight_layout()#화면 채우기 (안써도됨)
# plt.show()#그리기

#성별에 따른 생존 분류
# plt.figure(figsize=(8,4))#그래프 해상도 설정
# sns.countplot(data=df, x="sex", hue="survived") #x축 y축 설정 (survived의 값으로 나누기)
# plt.title("Survival Status by Survival")
# plt.ylabel('Count') #y축
# plt.xlabel('Sex') #x축
# plt.legend(loc='upper right',title="Survived", labels=['no', 'yes'])
# plt.show()#그리기

#요금 분포 등급별로 (박스 플롯)
# plt.figure(figsize=(8,4))#그래프 해상도 설정
# sns.boxplot(data=df, x="class", y="fare", order=["First", "Second", "Third"]) #x축 y축 설정
# plt.title("Fare Distribution by Class", fontsize=14)
# plt.ylabel('Fare') #y축
# plt.xlabel('Passenger Class') #x축
# plt.show()#그리기
# # 2사분위 / 3사분위 / 1사분위 ( 50 / 75 / 25 )
# # IQR (파란색 박스)

#나이별 요금 분표
# plt.figure(figsize=(8,4))#그래프 해상도 설정
# sns.boxplot(data=df, x="class", y="age", order=["First", "Second", "Third"]) #x축 y축 설정 (class의 값으로 나누기)
# plt.title("Fare Distribution by Class", fontsize=14)
# plt.ylabel('age') #y축
# plt.xlabel('Passenger Class') #x축
# plt.show()#그리기
# 2사분위 / 3사분위 / 1사분위 ( 50 / 75 / 25 )
# IQR (파란색 박스)

#바이올린 플롯
# plt.figure(figsize=(8,4))#그래프 해상도 설정
# sns.violinplot(data=df, x="survived", y="age") #x축 y축 설정
# plt.title("Fare Distribution by Survival Status", fontsize=14)
# plt.ylabel('age') #y축
# plt.xlabel('survived(0: No 1: Yes)') #x축
# plt.show()#그리기

#카테고리 플롯
# plt.figure(figsize=(8,4))#그래프 해상도 설정
# sns.catplot(#남자, 여자로 나누어 class로 order순서 / 1등석 2등석 3등석 생존여부
#     data=df,
#     x="class",
#     hue="survived",
#     col="sex",
#     kind="count",
#     order=["First", "Second", "Third"]
# )
# #group by와 비슷함
# plt.show()#그리기

#--------------------------------------------------
# #df =sns.load_dataset('titanic') //dataFrame이요~
# print(df.groupby('survived').describe()) #판다스를 활용한 groupBy //Test
#
#
# print(df.groupby('sex')['survived'].describe()) #판다스를 활용한 groupBy //아래와 비교 (통계)
# print(df.groupby('sex')['survived'].mean()) #판다스를 활용한 groupBy //아래와 비교 (평균)
#
# #성별에 따른 생존자 //판다스를 시각화 한다면 아래와 같음.
# plt.figure(figsize=(8,4))#그래프 해상도 설정
# sns.countplot(data=df, x="sex", hue="survived") #x축 y축 설정 (survived의 값으로 나누기)
# plt.title("Survival Status by Survival")
# plt.ylabel('Count') #y축
# plt.xlabel('Sex') #x축
# plt.legend(loc='upper right',title="Survived", labels=['no', 'yes'])
# plt.show()#그리기


#aggregation 성별로 그룹을 묶어서 탑습 등급을 나누어 평규, 인원수 보여주는
#print(df.groupby(['sex','class'])['survived'].agg(['mean','count']))
#print(df.groupby(['sex','class'])['survived'].agg(['median','count'])) #중간값이 있냐 없냐
#print(df.groupby(['sex','class'])['survived'].agg(['min','max'])) #살았냐 죽었냐
#print(df.groupby(['sex','class'])['survived'].agg(['min','count'])) #집계 함수