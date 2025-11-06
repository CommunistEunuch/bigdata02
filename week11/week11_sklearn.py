import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes

#당뇨병 데이터셋 로딩

#numpy 값임
#shape 442,10
#target : array
#사이킷런 번치

diabetes = load_diabetes()
#print(diabetes.feature_names)
print(diabetes)
#print(type(diabetes))

#print(diabetes.info()) #판다스 데이터 프레임이 아님.

#나이, 성별, BMI, 혈압, 총 콜레스테롤, 나쁜 콜레스테롤, 좋은 콜레스테롤, TCH(s1 / s3), LTG (로그로 변환된 중성 지방수치), 공복 혈당 수치

#print(diabetes.target) #당뇨병 진행 정도 값
#print(diabetes.data) #당뇨병 진행 정도 값

#데이터프레임 변환
#columns를 이미 있는 기준들을 가지고와서 적용
df_diabetes = pd.DataFrame(diabetes.data, columns=diabetes.features)
