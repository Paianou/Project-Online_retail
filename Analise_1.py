from unittest.mock import inplace

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.width', None)

df = pd.read_csv('online_retail_II.csv')

print(df.head().to_string())

print(f'linhas : ', df.shape[0])
print(f'colunas : ', df.columns)

antes= len(df)
df = df.dropna(subset=['Description'])
df = df.dropna(subset=['Customer ID'])
depois = len(df)

nulos = df.isnull().sum()
print('Dados nulos: ', df.isnull().sum())

print('Valores Unicos: ',df.nunique())
print(df['Invoice'].nunique(),'Faturas Unicas')

df = df.drop_duplicates()
print('Duplicados: ', df.duplicated().sum())

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Costomer ID'] = df['Customer ID'].astype(str)
df['Quantity'] = df['Quantity'].astype(int)
print('Tipos :', df.dtypes)

print('Devoluções:', df['Invoice'].astype(str).str.startswith('C').sum())
df = df[~df['Invoice'].str.startswith('C')]

df = df[df['Quantity'] > 0]
print(f"Após limpeza: {len(df):,} linhas")

df['TotalPrice'] = df['Quantity'] * df['Price']
print(f'Faturamento total: ', df['TotalPrice'].sum())

df.to_csv('online_retail_limpo.csv', index=False)
print('Arquivo salvo com sucesso!')

