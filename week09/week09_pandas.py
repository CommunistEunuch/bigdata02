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
uber = uber.drop(1155)
print(uber.tail())
print(uber.describe())