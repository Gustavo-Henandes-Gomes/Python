import pandas as pd
import plotly.express as px

tabela = pd.read_csv('telecom_users.csv')
tabela.drop('Unnamed: 0', axis=1)

tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

tabela = tabela.dropna(how='all', axis=1)

tabela = tabela.dropna(how='any', axis=0)

print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format))


for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()
