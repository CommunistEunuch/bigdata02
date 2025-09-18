import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('savant_data.csv')
#print(df.info)
#print(df['player_name'])
#df.drop

df_new = df[['player_id', 'player_name', 'total_pitches','velocity','hrs','so','bb']]
#print(df_new.info())
#print(df_new.tail())
#print(df_new.head())
#print(df_new.query('player_name == "Ohtani, Shohei"'))
#print(df_new.query('player_id = 660271'))
#print(df_new.sort_values(by=['velocity'], ascending=False))
#print(df_new.sort_values(by=['so'], ascending=False))
#print(df_new.sort_values(by=['bb'], ascending=True))
#print(df_new.sort_values(by=['hrs'], ascending=False))

#df_new.plot()
#오타니 쇼헤이의 정보 가져오기
#print(df_new.query('player_name == "Ohtani, Shohei"'))
#print(df_new.describe())

# plt.figure(figsize = (10,5))
# plt.boxplot(df_new['total_pitches'])
# plt.show()

# plt.title('Ohtani, Shohei', fontsize=20, fontweight='bold')
# plt.xlabel('player_id', fontsize=15)
# plt.ylabel('total_pitches', fontsize=15)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.show()

##이거 복습해요
#print(len(df_new[df_new['total_pitches'] > 1000])) #이게 더 빠름
#print(len(df_new.query('total_pitches > 1000')))



import seaborn as sns

#데이터셋 확인
# print(sns.get_dataset_names())
# titanic = sns.load_dataset('titanic')
# print(titanic.head())

#데이터셋 개수
#print(len(sns.get_dataset_names()))


# print(sns.get_dataset_names())
# titanic = sns.load_dataset('titanic')
# print(titanic.head())
# print(titanic.describe())
# print(titanic.nlargest(5,'age'))



#나이대별 산 사람
titanic = sns.load_dataset('titanic')
plt.figure(figsize= (15,12))

plt.subplot(2,3,1)
sns.boxplot(x="survived", data=titanic, y="age")
plt.title("Age Distribution by Survival Status")
plt.xlabel("Survived(0:No 1:Yes)")
plt.ylabel("Age")


##성별 확인
plt.subplot(2,3,2)
sns.boxplot(x="sex", data=titanic, y="age")
plt.title("Age Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Age")

##
plt.subplot(2,3,3)
sns.boxplot(x="class", data=titanic, y="fare")
plt.title("Fare Distribution by Class")
plt.xlabel("Passinger Class")
plt.ylabel("Fare")

##
plt.subplot(2,3,4)
sns.boxplot(x="survived", data=titanic, y="fare")
plt.title("Fare Distribution by Survival Status")
plt.xlabel("Survived(0:No 1:Yes)")
plt.ylabel("Fare")

##
plt.subplot(2,3,5)
sns.boxplot(x="sex", data=titanic, y="age", hue="survived")
plt.title("Age by Gender and Survival")
plt.xlabel("Gender")
plt.ylabel("Age")

handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles, ["No", "Yes"], title="Survived")


plt.show()