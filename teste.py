import pandas as pd

# Datas de início e fim (formato dd/mm/aaaa)
data_inicial = '01/08/2024'
data_final = '01/08/2025'

# URL do endpoint (formato JSON)
url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}'

# Carrega os dados em um DataFrame do pandas
df = pd.read_json(url)

# Exibe as primeiras linhas do DataFrame
print(df.tail())
