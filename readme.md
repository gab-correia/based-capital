APIs para Coleta de Dados Macroeconômicos: Guia Completo de Fontes de Dados
Este relatório apresenta uma lista abrangente de APIs (Interfaces de Programação de Aplicação) para coleta de dados relacionados aos indicadores macroeconômicos dos Estados Unidos, Brasil e dados globais de mercado, conforme solicitado. As APIs estão organizadas por categoria e incluem informações sobre como acessar cada fonte de dados.

I. APIs para Dados Macroeconômicos dos Estados Unidos
1. Federal Reserve Economic Data (FRED) API
URL Base: https://api.stlouisfed.org/fred/

A API do FRED é uma das fontes mais abrangentes para dados econômicos dos Estados Unidos, mantida pelo Federal Reserve Bank of St. Louis.

Características:

Acesso a mais de 670.000 séries temporais econômicas

Dados históricos e em tempo real

Gratuita mediante registro

Suporte a múltiplos formatos (JSON, XML)

Indicadores Disponíveis:

PIB e componentes (GDP, GDPC1)

Taxa de desemprego (UNRATE)

Inflação e expectativas (CPIAUCSL, T5YIE)

Taxa de juros (FEDFUNDS, DGS10)

Dados do mercado imobiliário (HOUST, MORTGAGE30US)

Indicadores de sentimento empresarial

Como usar:

python
import requests
api_key = 'YOUR_API_KEY'
url = f'https://api.stlouisfed.org/fred/series/observations?series_id=GDP&api_key={api_key}&file_type=json'
2. Bureau of Economic Analysis (BEA) API
URL Base: https://apps.bea.gov/api/data

A API do BEA fornece acesso a estatísticas econômicas oficiais dos Estados Unidos.

Características:

Dados do PIB por setor

Contas nacionais (NIPA)

Dados de comércio internacional

Investimento estrangeiro direto

Gratuita mediante registro

Indicadores Disponíveis:

PIB detalhado por indústria

Dados de consumo pessoal

Dados de investimento

Balança de pagamentos

3. U.S. Treasury Fiscal Data API
URL Base: https://api.fiscaldata.treasury.gov/services/api/fiscal_service/

Fornece dados sobre finanças públicas dos Estados Unidos.

Características:

Dados da dívida pública

Receitas e gastos federais

Taxas de juros de títulos do tesouro

Arrecadação de tarifas

4. Energy Information Administration (EIA) API
URL Base: https://api.eia.gov/v2/

API especializada em dados de energia.

Características:

Produção de petróleo

Preços de energia

Dados de consumo energético

Requer chave de API gratuita

II. APIs para Dados Macroeconômicos do Brasil
1. Sistema Gerenciador de Séries Temporais (SGS) - Banco Central do Brasil
URL Base: https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados

Principal fonte de dados econômicos brasileiros.

Características:

Mais de 18.000 séries temporais

Dados históricos desde 1980

Acesso gratuito sem necessidade de chave

Formato JSON

Indicadores Disponíveis:

Taxa Selic (11)

IPCA (433)

IBC-Br (24364)

Taxa de câmbio (1)

Taxa de desemprego (24369)

Agregados monetários

Crédito e endividamento das famílias

Exemplo de uso:

python
import requests
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2023&dataFinal=31/12/2023"
response = requests.get(url)
2. Portal de Dados Abertos do Banco Central
URL Base: https://dadosabertos.bcb.gov.br/

Complementa o SGS com dados estruturados adicionais.

Características:

Dados de inclusão financeira

Estatísticas do sistema financeiro

Dados do Pix

Expectativas de mercado (Focus)

3. APIs do IBGE
URL Base: https://servicodados.ibge.gov.br/api/

Instituto Brasileiro de Geografia e Estatística.

Características:

17 APIs diferentes disponíveis

Dados agregados de pesquisas e censos

Dados regionais e sociais

Acesso gratuito

Indicadores Disponíveis:

Dados demográficos

Indicadores sociais

Vendas no varejo

Produção industrial

Dados do setor agropecuário

4. API do IPEAData
URL Base: http://www.ipeadata.gov.br/api/odata4/

Instituto de Pesquisa Econômica Aplicada.

Características:

Dados macroeconômicos

Séries regionais e sociais

Protocolo OData 4.0

Retorna dados em JSON

5. Dados de Mercado API
URL Base: https://api.dadosdemercado.com.br/v1

Fonte privada de dados financeiros brasileiros.

Características:

Dados de empresas e mercados

Indicadores financeiros

Dados do Tesouro Direto

Requer autenticação

6. brapi - API de Ações Brasileiras
URL Base: https://brapi.dev/api/

API especializada em dados do mercado financeiro brasileiro.

Características:

Cotações em tempo real

Dados históricos (OHLCV)

Fundamentos de empresas

Dividendos detalhados

Gratuita para uso básico

III. APIs para Dados Globais e Sentimento de Mercado
1. World Bank Indicators API
URL Base: https://api.worldbank.org/v2/

Banco Mundial fornece dados de desenvolvimento global.

Características:

Acesso a mais de 16.000 indicadores

Dados de mais de 200 países

50+ anos de dados históricos

Múltiplos formatos (JSON, XML, CSV)

Indicadores Disponíveis:

PIB mundial

Indicadores de desenvolvimento

Dados demográficos

Indicadores ambientais

2. IMF Data API
URL Base: http://dataservices.imf.org/REST/SDMX_XML.svc/

Fundo Monetário Internacional.

Características:

Dados de balanço de pagamentos

Estatísticas financeiras internacionais

Dados fiscais

Padrão SDMX

3. OECD Data API
URL Base: https://sdmx.oecd.org/public/rest/data/

Organização para Cooperação e Desenvolvimento Econômico.

Características:

Dados de países desenvolvidos

Indicadores econômicos comparativos

Padrão SDMX 2.1

Gratuita, mas com limites de taxa

4. European Central Bank (ECB) API
URL Base: https://data-api.ecb.europa.eu/service/

Banco Central Europeu.

Características:

Dados monetários da Zona do Euro

Taxas de câmbio

Taxas de juros

Padrão SDMX 2.1

5. Trading Economics API
URL Base: Disponível através do site tradingeconomics.com

Dados econômicos globais.

Características:

Dados de mais de 196 países

Calendário econômico

Previsões econômicas

Planos pagos

IV. APIs para Análise Direta de Portfólio
1. Alpha Vantage
URL Base: https://www.alphavantage.co/query

Dados financeiros em tempo real e históricos.

Características:

Ações, ETFs, forex, criptomoedas

Indicadores técnicos

Dados fundamentais

Plano gratuito limitado

2. Financial Modeling Prep (FMP)
URL Base: https://financialmodelingprep.com/api/

Dados financeiros abrangentes.

Características:

Demonstrações financeiras

Dados históricos de preços

Indicadores econômicos

Treasury rates

3. Commodities APIs
CommodityPriceAPI
URL Base: https://api.commoditypriceapi.com/v2

130+ commodities

Dados em tempo real e históricos

Commodities-API
URL Base: https://commodities-api.com/api/

Petróleo, ouro, prata, produtos agrícolas

4. APIs de Câmbio
ExchangeRate-API
URL Base: https://api.exchangerate-api.com/

161 moedas

Dados confiáveis há 15 anos

Fixer.io
URL Base: https://data.fixer.io/api/

170 moedas mundiais

Dados do Banco Central Europeu

AwesomeAPI (Brasil)
URL Base: https://economia.awesomeapi.com.br/

Especializada em moedas brasileiras

Dados do Banco Central (PTAX)

5. APIs de Títulos e Renda Fixa
Treasury Rates (FMP)
URL Base: https://financialmodelingprep.com/api/v4/treasury

Yields de títulos americanos

Bond Yields API (Tradefeeds)
Títulos governamentais de 50+ países

Finnworlds Bond API
Dados históricos e em tempo real

Considerações Importantes
Autenticação
APIs Gratuitas: FRED, SGS/BCB, IBGE, World Bank, OECD

Requerem Registro: BEA, EIA, Alpha Vantage

APIs Pagas: Trading Economics, FMP, dados premium

Limites de Taxa
FRED: Sem limite especificado

OECD: 20 downloads por hora

Alpha Vantage: 5 calls por minuto (gratuito)

APIs do BCB: Sem limite oficial

Formatos de Dados
JSON: Maioria das APIs modernas

XML: BEA, algumas APIs do SDMX

CSV: Disponível como opção em muitas APIs

Recomendações de Implementação
Para dados dos EUA: Combine FRED + BEA + Treasury API

Para dados do Brasil: SGS/BCB + IBGE + IPEAData + brapi

Para dados globais: World Bank + IMF + OECD + ECB

Para portfólio: Alpha Vantage + FMP + CommodityAPI + ExchangeRate-API

Bibliotecas Python Recomendadas
fredapi - Para FRED

pandas_datareader - Múltiplas fontes

yfinance - Dados financeiros do Yahoo

requests - Para APIs REST genéricas

imf.data (R) - Para dados do IMF

Este guia fornece uma base sólida para implementar um sistema abrangente de coleta de dados macroeconômicos usando APIs públicas e privadas, cobrindo todos os indicadores mencionados em sua solicitação.