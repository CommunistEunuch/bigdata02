import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

german = pd.read_csv('german.csv')
#print(german.info()) #세부 정보
print(german.tail(5)) #끝에서 5줄

print(german['Age'].describe())

#cut : 분위를 나누어줌 #------------------------------
print(pd.cut(german['Age'], bins=8)) #8분위로 나눔
print(pd.cut(german['Age'], bins=2)) #2분위로 나눔
##결과값 : Categories (2, interval[float64, right]): [(18.944, 47.0] < (47.0, 75.0]]
#여기서 ( ] <- 각각 초과 이하 기호

#---------------------------------------------------
#reset_index
print(pd.cut(german['Age'], bins=8).reset_index().groupby('Age').count()) #8개의 구간으로 초기화. index로 나누어서 보여줌
ages = [10,20,30,40,50,60,70,80]
#------------------
#inclusive exclusive
print(pd.cut(german['Age'], bins=ages).reset_index().groupby('Age').count())

#-------------------
#초과 미만 이런거 수정 (또한 나이 분류와 같이)
print(pd.cut(german['Age'], bins=ages,right=False).reset_index().groupby('Age').count())

#--------------------
#qcut : quantity cut

