from itertools import groupby
import pandas as pd

df = pd.read_csv('online_retail_limpo.csv')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='mixed')
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Mes'] = df['InvoiceDate'].dt.to_period('M')
print(df['InvoiceDate'])

# Top 10 produtos
print('TOP MAIORES PRODUTOS MAIS VENDIDOS: ')
print(df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10))
#Faturamento por Pais
print('MAIORES FATURAMENTOS POR PAISES: ')
print(df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10))


df['InvoiceDate']=pd.to_datetime(df['InvoiceDate']) # DATA CONVERTIDA
data_ref = df['InvoiceDate'].max() # DATA REFERENCIA

rfm = df.groupby('Customer ID').agg(
    Recencia   = ('InvoiceDate', lambda x: (data_ref - x.max()).days), # quanto cliente comprou
    Frequencia = ('Invoice', 'nunique'),                              # quantas vezes o cliente comprou
    Valor      = ('TotalPrice', 'sum')                              #quanto o cliente gastou
).reset_index()

print('RFM geral : ',rfm.head())

rfm['R_score'] = pd.qcut(rfm['Recencia'],   q=4, duplicates='drop').cat.codes
rfm['F_score'] = pd.qcut(rfm['Frequencia'], q=4, duplicates='drop').cat.codes
rfm['M_score'] = pd.qcut(rfm['Valor'],      q=4, duplicates='drop').cat.codes

rfm['RFM_score'] = rfm['R_score']


rfm['RFM_score'] = rfm ['R_score'].astype(int) + rfm['F_score'].astype(int)+ rfm['M_score'].astype(int)

def classificar(score):
    if score >= 10: return 'Campeao',
    elif score >=7: return 'Fiel',
    elif score >=5: return 'Em risco',
    else :       return 'Inativo'

rfm['Segmento'] = rfm['RFM_score'].apply(classificar)
print(rfm['Segmento'].value_counts())

rfm.to_csv('online_retail_explorado', index=False)
print('Salvo com Sucesso!!')