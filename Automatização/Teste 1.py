import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "xxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token = "xxxxxxxxxxxxxxxx"

client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="Numero que sera enviado",
            from_="Numero twilio",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
