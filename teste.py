import pandas as pd


df = pd.read_csv(r"C:\Users\Akira\PycharmProjects\DjangoTest\data\Fast_Food_Restaurants_US.csv", index_col=0)
df['length'] = df.websites.str.len()
print(df)