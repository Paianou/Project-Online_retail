import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('online_retail_limpo.csv')

engine = create_engine('mysql+pymysql://root:Thzinn975@localhost/ecommerce')
#create_engine('mysql+pymysql://'root':' + passaword + '@' + host + '/' + db)

df.to_sql('vendas', con=engine, if_exists='replace', index=False)

print("Dados importados com sucesso!")