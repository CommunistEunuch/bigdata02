import pandas as pd

df = pd.read_csv('savant_data.csv')
#print(df.info)
#print(df['player_name'])
#df.drop

df_new = df[['player_id', 'player_name', 'total_pitches','velocity','hrs','so','bb']]
#print(df_new.info())
#print(df_new.tail())
#print(df_new.head())
#print(df_new.query('player_name == "Ohtani, Shohei"'))