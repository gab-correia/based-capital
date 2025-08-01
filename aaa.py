import pandas as pd
from datetime import datetime
import yfinance as yf
 
def obter_dados_yfinance(periodo="2y", intervalo="1d", exportar_csv=False):
    """
    Baixa dados históricos de múltiplos ativos usando o Yahoo Finance (yfinance).
    
    Parâmetros:
        periodo (str): Período de tempo (ex: '1y', '2y', '5y', 'max')
        intervalo (str): Intervalo dos dados ('1d', '1wk', '1mo')
        exportar_csv (bool): Se True, exporta os dados para CSVs separados por ticker

    Retorna:
        dict: dicionário com os dados históricos de cada ativo
    """

    # Lista de ativos com tickers e nomes descritivos
    tickers = {
        # Câmbio
        'USDBRL=X': 'Dólar/Real',
        'EURBRL=X': 'Euro/Real',
        'CNYBRL=X': 'Yuan/Real',

        # Índices e juros
        '^BVSP': 'IBOVESPA',
        '^GSPC': 'S&P 500',
        '^TNX': 'Treasury 10Y Yield',

        # Futuros
        # 'ES=F': 'S&P 500 Futures',
        # 'DX=F': 'Dollar Index Futures',
    }

    resultados = {}

    print(f"🔍 Coletando dados históricos ({periodo}, {intervalo})...\n")

    for ticker, nome in tickers.items():
        try:
            print(f"➡️  {nome} ({ticker})")

            ativo = yf.Ticker(ticker)
            dados = ativo.history(period=periodo, interval=intervalo)

            if dados.empty:
                print("   ⚠️  Nenhum dado encontrado.\n")
                continue

            dados.index = pd.to_datetime(dados.index)
            #dados = dados[['Close']].rename(columns={'Close': nome})
            # resultados[ticker] = {
            #     'nome': nome,
            #     'dados': dados
            # }

            # print(f"   ✅ {len(dados)} registros de {dados.index.min().date()} até {dados.index.max().date()}")
            # print(f"   Último preço: {dados[nome].iloc[-1]:.4f}\n")

            
            resultados[ticker] = {
                'nome': nome,
                'dados': dados
            }

            print(f"   ✅ {len(dados)} registros de {dados.index.min().date()} até {dados.index.max().date()}")
            #print(f"   Último preço de fechamento: {dados['Close'].iloc[-1]:.4f}\n")
            
            if exportar_csv:
                dados.to_csv(f"{ticker.replace('=','')}_{intervalo}.csv")

        except Exception as e:
            print(f"   ❌ Erro ao obter dados: {e}\n")

    print("✅ Coleta finalizada.")

    return resultados

dados_obtidos = obter_dados_yfinance(periodo="2y", intervalo="1d", exportar_csv=True)
# # ===============================
# # USO DO SCRIPT
# # ===============================
# if __name__ == "__main__":
#     # Exemplo de uso
#     dados_obtidos = obter_dados_yfinance(periodo="2y", intervalo="1d", exportar_csv=True)

#     # Unificar retornos em um único DataFrame
#     todos_dados = [info['dados'] for info in dados_obtidos.values()]
#     df_merge = pd.concat(todos_dados, axis=1)

#     # Calcular retornos mensais
#     retornos_mensais = df_merge.resample('M').ffill().pct_change().dropna()

#     # Mostrar exemplo
#     print("\n📈 Retornos mensais (head):")
#     print(retornos_mensais.head())
