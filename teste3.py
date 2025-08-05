import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

mt5_path = r"C:\Program Files\MetaTrader 5\terminal64.exe"
if not mt5.initialize(path=mt5_path):
    print("Falha ao inicializar MetaTrader5:", mt5.last_error())
    mt5.shutdown()
    exit()

symbols = ["DI1F27", "DI1F30"]
data_final = datetime.now()
data_inicial = data_final - timedelta(days=365)

# 1. Certificar-se de que os símbolos estão visíveis
for s in symbols:
    if not mt5.symbol_select(s, True):
        print(f"Falha ao selecionar símbolo {s}:", mt5.last_error())

def obter_series_diarias(simbolo, inicio, fim):
    rates = mt5.copy_rates_range(simbolo, mt5.TIMEFRAME_D1, inicio, fim)
    if rates is None or len(rates)==0:
        raise RuntimeError(f"Erro ao obter dados para {simbolo}: {mt5.last_error()}")
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df = df[['time','open','high','low','close','tick_volume']]
    df.columns = ['Data','Abertura','Máxima','Mínima','Fechamento','Volume']
    df.set_index('Data', inplace=True)
    return df

for simbolo in symbols:
    try:
        df = obter_series_diarias(simbolo, data_inicial, data_final)
        print(f"{simbolo}: {len(df)} registros obtidos.")
        df.to_csv(f"{simbolo}_diario.csv", sep=';', encoding='utf-8')
        print(f"Salvo em: {simbolo}_diario.csv")
    except Exception as e:
        print(str(e))

mt5.shutdown()
