# Previsão de churn com machine learning

Projeto didático de classificação de cancelamento de clientes de telecomunicações usando o conjunto de exemplo Telco Customer Churn da IBM. O notebook percorre a leitura e exploração dos dados, a separação entre treino e teste, um baseline, uma regressão logística e a avaliação por métricas e matriz de confusão.

## Estrutura

- `projeto_churn.ipynb`: análise e treinamento do modelo.
- `tests/test_dados.py`: quatro testes para validar o arquivo e campos essenciais.
- `data/Telco-Customer-Churn.csv`: arquivo obtido localmente, não incluído neste repositório.

## Requisitos

Python 3.14 ou compatível com as versões indicadas em `requirements.txt`.

Crie e ative um ambiente virtual e instale as dependências:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Dados

O CSV é disponibilizado pelo repositório de exemplos da IBM: [Telco Customer Churn](https://github.com/IBM/telco-customer-churn-on-icp4d/blob/master/data/Telco-Customer-Churn.csv). O notebook baixa o arquivo automaticamente da fonte oficial na primeira célula e o salva em `data/`. Execute essa célula antes dos testes. O CSV fica fora do controle de versão porque a licença do padrão de código da IBM não estabelece, por si só, os termos de redistribuição do conjunto de dados.

## Executar

Abra `projeto_churn.ipynb` no Jupyter ou VS Code e execute as células em ordem. Depois que o CSV estiver em `data/`, rode os testes: 

```bash
python -m pytest -q
```

## Licença

A licença deste projeto ainda não foi definida. O CSV é uma obra separada, portanto seus termos de uso e redistribuição devem ser verificados na fonte antes de qualquer distribuição. Este repositório não inclui o arquivo de dados.
