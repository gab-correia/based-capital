import pandas as pd
from datetime import datetime, timedelta

def obter_dados_bacen_periodo_ano(codigo_serie=12, periodo_ano=1, exportar_csv=True):
    """
    Baixa dados históricos de uma série do BACEN (SGS) para o período de 'periodo_ano' anos atrás até hoje.
    
    Parâmetros:
        codigo_serie (int): Código da série no SGS (ex: 12 para CDI diário)
        periodo_ano (int): Quantos anos atrás pegar os dados (padrão 1)
        exportar_csv (bool): Se True, exporta os dados para CSV
    
    Retorna:
        pd.DataFrame: DataFrame com os dados obtidos (colunas: 'Data' e 'Valor')
    """
    data_final = datetime.today()
    data_inicial = data_final - pd.DateOffset(years=periodo_ano)
    
    # Convertendo para string no formato dd/mm/aaaa
    data_inicial_str = data_inicial.strftime('%d/%m/%Y')
    data_final_str = data_final.strftime('%d/%m/%Y')
    
    url = (
        f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados'
        f'?formato=json&dataInicial={data_inicial_str}&dataFinal={data_final_str}'
    )
    try:
        df = pd.read_json(url)
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)
        df = df.rename(columns={'data': 'Date', 'valor': 'CDI'})
        df = df.set_index('Date')
        
        print(f"✅ Dados obtidos: {len(df)} registros de {df.index.min().date()} até {df.index.max().date()}")
        
        if exportar_csv:
            # nome_arquivo = f"output/CDI_SGS_{codigo_serie}_{data_inicial_str.replace('/','')}_{data_final_str.replace('/','')}.csv"
            nome_arquivo = f"output/CDI_SGS_{codigo_serie}.csv"
            df.to_csv(nome_arquivo)
            print(f"📄 Dados exportados para {nome_arquivo}")
        
        return df
    
    except Exception as e:
        print(f"❌ Erro ao obter dados: {e}")
        return pd.DataFrame()


if __name__ == "__main__":

    df_cdi = obter_dados_bacen_periodo_ano(codigo_serie=12, periodo_ano=1, exportar_csv=True)