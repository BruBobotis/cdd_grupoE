# 🔧 Projeto: Manutenção Preditiva de "Zero-Downtime"

> Projeto desenvolvido para a disciplina de **Ciência de Dados**, com foco na aplicação de técnicas de **análise de dados**, **ETL** e **Machine Learning** em um cenário de **manutenção preditiva industrial**.

---

## 👥 1. Identificação do Grupo

- **Instituição:** Faculdade Engenheiro Salvador Arena  
- **Curso:** Engenharia de Controle e Automação  
- **Disciplina:** Ciência de Dados  
- **Grupo:** E  

### Integrantes
- **Bruno Alves Guedes** - RA: [062210033]
- **Guilherme Nascimento** - RA: [062210016]
- **Guilherme Fernando** - RA: [062210038]
- **Lucas Guedes** - RA: [062210002]
- **Pedro Henrique Matias** - RA: [062220039]

---

## 🎯 2. Área-Problema Selecionada

O grupo selecionou a área de **Manutenção Preditiva de "Zero-Downtime"** para o desenvolvimento do projeto.

### ✅ Recorte definido do projeto
O foco será a **predição de falhas em motores elétricos industriais**, utilizando dados de sensores e variáveis operacionais para antecipar comportamentos anormais e reduzir paradas não planejadas.

### 📌 Justificativa da escolha
A manutenção preditiva é uma abordagem estratégica dentro da **Indústria 4.0**, pois permite:

- reduzir custos com manutenção corretiva;
- evitar interrupções inesperadas na produção;
- aumentar a confiabilidade dos equipamentos;
- melhorar a segurança operacional;
- apoiar a tomada de decisão com base em dados.

Além disso, o tema está diretamente relacionado à área de **Controle e Automação**, integrando sensores, monitoramento de processos e inteligência computacional.

---

## 🧩 3. Diagnóstico e Definição do Problema

Em ambientes industriais, motores elétricos são ativos críticos para a continuidade da operação. Quando ocorrem falhas inesperadas, os impactos podem incluir:

- parada total ou parcial da linha de produção;
- aumento de custos operacionais;
- desperdício de recursos;
- queda de produtividade;
- riscos à segurança e à confiabilidade do processo.

Tradicionalmente, muitas empresas ainda dependem de:

- **manutenção corretiva**, realizada apenas após a falha;
- **manutenção preventiva**, baseada em intervalos fixos.

Essas abordagens nem sempre refletem a real condição do equipamento. Nesse contexto, a **manutenção preditiva** se destaca por utilizar dados históricos e operacionais para identificar sinais de falha antes que ela aconteça.

### ❓ Problema de pesquisa
Como utilizar dados de sensores industriais para prever falhas em motores elétricos e, assim, reduzir o downtime não planejado?

### 💡 Hipótese
A partir da análise de variáveis operacionais, como vibração, temperatura, corrente e tempo de operação, é possível detectar padrões associados a falhas e apoiar decisões de manutenção de forma antecipada.

---

## 🎯 4. Objetivos do Projeto

### Objetivo Geral
Desenvolver um pipeline de dados capaz de organizar, tratar e analisar informações operacionais de equipamentos industriais, servindo de base para modelos de **Machine Learning aplicados à manutenção preditiva**.

### Objetivos Específicos
- selecionar um dataset compatível com o tema proposto;
- estruturar o processo de **ETL**;
- organizar o repositório para evolução das próximas milestones;
- preparar os dados para análise exploratória;
- apoiar futuramente o desenvolvimento de modelos preditivos;
- contribuir para a redução de falhas inesperadas em equipamentos industriais.

---

## 🗂️ 5. Arquitetura de Dados (Fonte e Dataset)

O projeto utilizará um conjunto de dados estruturado com informações associadas à condição operacional de equipamentos industriais.

### 📥 Origem dos Dados
Os dados poderão ser obtidos a partir de:

- dataset público para manutenção preditiva;
- arquivos em formato `.csv`;
- bases contendo medições de sensores e status do equipamento.

### Dataset selecionado
Para a fase M1, o grupo utilizará o **AI4I 2020 Predictive Maintenance Dataset**, disponibilizado pela UCI Machine Learning Repository. A base foi escolhida por ser voltada especificamente para manutenção preditiva industrial, contendo 10.000 registros e variáveis operacionais relevantes para análise de falhas, como temperatura, rotação, torque, desgaste da ferramenta e indicação de falha da máquina.

### 🧾 Estrutura esperada dos dados
Exemplos de atributos que poderão compor o dataset:

- temperatura;
- vibração;
- corrente elétrica;
- rotação;
- pressão;
- horas de operação;
- estado do equipamento;
- registro de falha;
- tipo de falha.

### 🎯 Variável alvo
A variável alvo poderá representar, dependendo da base escolhida:

- **falha / não falha**;
- **tipo de falha**;
- **nível de criticidade do equipamento**.

---

## 🔄 6. Plano de Tratamento de Dados (ETL)

O pipeline de dados seguirá as seguintes etapas de processamento:

### 1. Extração
A coleta dos dados será realizada por meio de arquivos `.csv` e/ou datasets públicos relacionados à manutenção preditiva.

### 2. Transformação
Nesta etapa, serão executados procedimentos como:

- leitura e inspeção inicial dos dados;
- identificação de valores ausentes;
- remoção ou tratamento de inconsistências;
- análise de outliers;
- padronização de colunas;
- conversão de tipos de dados;
- normalização ou padronização de variáveis numéricas;
- seleção de atributos relevantes para análise.

### 3. Carga
Após o tratamento, os dados serão armazenados na pasta `data/processed`, ficando prontos para as etapas de:

- análise exploratória de dados;
- modelagem preditiva;
- avaliação de desempenho dos modelos.

---

## 🧱 7. Estrutura do Repositório

A organização das pastas foi definida para facilitar a manutenção, rastreabilidade e evolução do projeto ao longo das milestones.

```bash
cdd_grupoE/
│
├── data/
│   ├── raw/                # Dados brutos originais
│   └── processed/          # Dados tratados e prontos para análise
│
├── docs/                   # Diagramas, imagens e documentação complementar
│
├── notebooks/              # Análises exploratórias e experimentos
│
├── scripts/                # Scripts de ETL e pré-processamento
│
├── requirements.txt        # Dependências do projeto
├── .gitignore              # Arquivos e pastas ignorados pelo Git
└── README.md               # Documentação principal do projeto
