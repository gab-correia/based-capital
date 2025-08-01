# Based Capital

## Descrição

Based Capital é um projeto de análise financeira que implementa a teoria moderna de portfólio de Markowitz para otimização de carteiras de investimento. O projeto coleta dados históricos de ativos financeiros brasileiros e internacionais, calcula retornos logarítmicos e constrói a fronteira eficiente para determinar a alocação ótima de ativos.

## Funcionalidades

- 📊 Coleta automática de dados históricos via Yahoo Finance (yfinance)
- 💱 Análise de múltiplos ativos: ações, índices, câmbio e títulos
- 📈 Cálculo de retornos logarítmicos e matriz de correlação
- 🎯 Otimização de portfólio usando teoria de Markowitz
- 📉 Visualização da fronteira eficiente
- 🔢 Cálculo do índice Sharpe para maximização de retorno ajustado ao risco

## Ativos Analisados

| Ticker      | Nome              | Tipo de Ativo              | Status na Análise        |
|-------------|-------------------|-----------------------------|--------------------------|
| ^BVSP       | IBOVESPA          | Índice de ações (Brasil)    | ✅ Incluído              |
| ^GSPC       | S&P 500           | Índice de ações (EUA)       | ✅ Incluído              |
| USDBRL=X    | Dólar/Real        | Taxa de câmbio              | ✅ Incluído              |
| EURBRL=X    | Euro/Real         | Taxa de câmbio              | ✅ Incluído              |
| ^TNX        | Treasury 10Y Yield| Taxa de juros (10 anos)     | ⚠️ Coletado, mas com cautela |

## Tecnologias Utilizadas

- **Python 3.x**
- **pandas** - Manipulação e análise de dados
- **numpy** - Computação numérica
- **yfinance** - Coleta de dados financeiros do Yahoo Finance
- **PyPortfolioOpt** - Otimização de portfólio
- **matplotlib** - Visualização de dados
- **seaborn** - Visualização estatística
- **Jupyter Notebook** - Ambiente de desenvolvimento interativo

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos para instalação

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITORIO]
   cd based-capital
   ```

2. Instale as dependências:
   ```bash
   pip install pandas numpy yfinance PyPortfolioOpt matplotlib seaborn jupyter
   ```

3. Crie a pasta de output (se não existir):
   ```bash
   mkdir output
   ```

## Uso

### 1. Coleta de Dados

Execute o script de coleta para baixar dados históricos:

```python
from coleta_dados import obter_dados_yfinance

# Coleta dados dos últimos 2 anos
dados = obter_dados_yfinance(periodo="2y", intervalo="1d", exportar_csv=True)
```

### 2. Análise no Jupyter Notebook

Abra o notebook principal:

```bash
jupyter notebook estudo.ipynb
```

### 3. Otimização de Portfólio

O projeto calcula automaticamente:

- **Retornos logarítmicos**: 
  ```
  r_t = ln(P_t / P_{t-1})
  ```
- **Matriz de correlação** entre os ativos
- **Fronteira eficiente** de Markowitz
- **Pesos ótimos** para maximizar o índice Sharpe

## Estrutura do Projeto

```
based-capital/
├── estudo.ipynb              # Notebook principal com análises
├── coleta_dados.py           # Script para coleta de dados
├── output/                   # Dados históricos em CSV
│   ├── ^BVSP_1d.csv
│   ├── ^GSPC_1d.csv
│   ├── USDBRLX_1d.csv
│   └── EURBRLX_1d.csv
└── README.md
```

## Metodologia

### Teoria de Markowitz

O projeto implementa a teoria moderna de portfólio, que busca:

1. **Diversificação eficiente**: Combinação de ativos que minimize o risco para um dado retorno
2. **Fronteira eficiente**: Conjunto de portfólios ótimos que maximizam retorno para cada nível de risco
3. **Índice Sharpe**: Métrica que mede retorno por unidade de risco

### Fórmulas Principais

- **Retorno logarítmico**: `ln(P_t / P_{t-1})`
- **Retorno anualizado**: `retorno_diário * 252`
- **Índice Sharpe**: `(retorno - taxa_livre_risco) / volatilidade`

## Resultados Esperados

- Matriz de correlação visualizada com heatmap
- Gráfico da fronteira eficiente
- Pesos ótimos para cada ativo na carteira
- Métricas de performance: retorno esperado, volatilidade e índice Sharpe

## Limitações e Considerações

- **Treasury 10Y Yield (^TNX)**: Representa uma taxa de juros, não um preço. Usar com cautela na otimização
- **Dados históricos**: Performance passada não garante resultados futuros
- **Modelo simplificado**: Não considera custos de transação, impostos ou restrições de liquidez

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaAnalise`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova análise de risco'`)
4. Push para a branch (`git push origin feature/NovaAnalise`)
5. Abra um Pull Request

## Próximos Passos

- [ ] Implementar análise de Value at Risk (VaR)
- [ ] Adicionar mais ativos brasileiros (ações individuais)
- [ ] Incluir análise de backtesting
- [ ] Desenvolver interface web para visualização
- [ ] Implementar rebalanceamento automático

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato

Gabriel - Estudante Insper

Link do Projeto: [https://github.com/gabriel/based-capital](https://github.com/gabriel/based-capital)

## Agradecimentos

- **Insper - Instituto de Ensino e Pesquisa** pelo ambiente acadêmico
- **Yahoo Finance** pelos dados financeiros gratuitos
- **Comunidade PyPortfolioOpt** pela excelente biblioteca de otimização
- **Harry Markowitz** pela teoria fundamental de portfólio
