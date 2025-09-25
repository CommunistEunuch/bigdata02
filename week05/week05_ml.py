import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
import tglearn as tg
df = pd.read_csv('lifesat.csv')
#print(len(df))
#print(df.tail(3))
#print(df.info())
#print(df.describe())

X = df[["GDP per capita (USD)"]].values
y = df[["Life satisfaction"]].values

model1 = LinearRegression()
model2 = KNeighborsRegressor(3)

model1.fit(X, y) #학습시키는 함수
model2.fit(X, y) #학습시키는 함수

new_instance = [[37_655.2]]
new_instance2 = [[31_721.3]] # 2020 GDP Korea,Republic of

print(model1.predict(new_instance)) #Linear
print(model2.predict(new_instance)) #K-NN

print(f"Life satisfaction(Linear Regression Model : {model1.predict(new_instance2)[0][0]:.1f}") #Linear
print(f"Life satisfaction(K-NN Model: {model2.predict(new_instance2)[0][0]:.1f}") #K-NN

#print(X)
# df.lifesat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
# plt.axis([23_500, 62_500, 4, 9])
# plt.show()

model3 = tg.LinearRegression()
model4 = tg.KNeighborsRegressor(3)

model3.fit(X, y)
model4.fit(X, y)

print(model3.predict(new_instance2))
print(model4.predict(new_instance2))