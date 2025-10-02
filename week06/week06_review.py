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
plt.figure(figsize=(8,4))#그래프 해상도 설정
sns.countplot(data=df, x="class", order=["First","Second", "Third"]) #x축 y축 설정 (x축 bins:분포 섹션 나누기, KDE : 추세선)
plt.title("Passenger Count by Class", fontsize=14) #title
plt.ylabel('class') #y축
plt.xlabel('Count') #x축
#plt.tight_layout()#화면 채우기 (안써도됨)
plt.show()#그리기