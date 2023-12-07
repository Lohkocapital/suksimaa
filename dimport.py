import pandas as pd
from sqlalchemy import create_engine
import datetime


aika = datetime.datetime.now()
print(f'Avataan tietokantayhteys {aika}')

connection_url = 'mysql+mysqlconnector://root:W3bkaksi.0@54.228.193.255/suksimaagi'
engine = create_engine(connection_url)
print(f'Tietokantayhteys avattu {aika}')

# query = input(f"Anna kysely: ")
# print(f'Kysely on: {query}')
query = "SELECT * FROM oittaa1"

df = pd.read_sql(query, con=engine)
print(df.head())
print(df.tail())
