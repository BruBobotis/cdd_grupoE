# Fluxo de Dados - Projeto M1

## Objetivo
Documentar o fluxo inicial dos dados para o projeto de manutenção preditiva de "Zero-Downtime".

## Etapas do Fluxo

### 1. Entrada de Dados
Os dados brutos serão armazenados na pasta:

`data/raw/`

Os arquivos poderão estar em formatos como:
- `.csv`
- `.xlsx`

### 2. Extração
O script `scripts/etl.py` será responsável por:
- localizar o arquivo bruto;
- realizar a leitura inicial;
- validar a estrutura do dataset.

### 3. Transformação
Nesta etapa serão aplicados:
- padronização dos nomes das colunas;
- remoção de linhas totalmente vazias;
- remoção de duplicidades;
- inspeção inicial de inconsistências.

### 4. Saída de Dados Tratados
Os dados tratados serão salvos em:

`data/processed/dados_tratados.csv`

### 5. Próximas Etapas
Após a M1, os dados processados serão utilizados em:
- análise exploratória de dados (M2);
- preparação para modelagem preditiva (M3);
- refinamento e apresentação final (M4).

## Resumo Visual

Dataset bruto -> ETL -> dados tratados -> EDA -> modelagem -> avaliação