# 🔧 Projeto: Manutenção Preditiva de "Zero-Downtime"

> Projeto desenvolvido para a disciplina de **Ciência de Dados**, com foco na aplicação de técnicas de **análise de dados**, **ETL**, **Análise Exploratória de Dados (EDA)** e **Machine Learning** em um cenário de **manutenção preditiva industrial**.

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
O foco do trabalho é a **predição de falhas em motores e equipamentos industriais**, utilizando dados de sensores e variáveis operacionais para antecipar comportamentos anormais e reduzir paradas não planejadas.

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

Em ambientes industriais, motores elétricos e outros ativos críticos são fundamentais para a continuidade da operação. Quando ocorrem falhas inesperadas, os impactos podem incluir:

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
Como utilizar dados de sensores industriais para prever falhas em equipamentos e, assim, reduzir o downtime não planejado?

### 💡 Hipótese
A partir da análise de variáveis operacionais, como temperatura, velocidade rotacional, torque e desgaste da ferramenta, é possível detectar padrões associados a falhas e apoiar decisões de manutenção de forma antecipada.

---

## 🎯 4. Objetivos do Projeto

### Objetivo Geral
Desenvolver um pipeline de dados capaz de organizar, tratar e analisar informações operacionais de equipamentos industriais, servindo de base para modelos de **Machine Learning aplicados à manutenção preditiva**.

### Objetivos Específicos
- selecionar um dataset compatível com o tema proposto;
- estruturar o processo de **ETL**;
- realizar a **Análise Exploratória de Dados (EDA)**;
- identificar correlações, padrões e possíveis outliers;
- preparar os dados para futuras etapas de modelagem;
- contribuir para a redução de falhas inesperadas em equipamentos industriais.

---

## 🗂️ 5. Arquitetura de Dados (Fonte e Dataset)

O projeto utiliza um conjunto de dados estruturado com informações associadas à condição operacional de equipamentos industriais.

### 📥 Origem dos Dados
Os dados foram obtidos a partir de um dataset público de manutenção preditiva.

### Dataset selecionado
Para as etapas M1 e M2, o grupo utiliza o **AI4I 2020 Predictive Maintenance Dataset**, disponibilizado pela **UCI Machine Learning Repository**. A base foi escolhida por ser voltada especificamente para manutenção preditiva industrial, contendo **10.000 registros** e variáveis operacionais relevantes para análise de falhas, como:

- temperatura do ar;
- temperatura de processo;
- velocidade rotacional;
- torque;
- desgaste da ferramenta;
- indicação de falha da máquina;
- tipos específicos de falha.

### 🧾 Estrutura dos dados
As principais variáveis presentes na base são:

- `udi`
- `product_id`
- `type`
- `air_temperature_[k]`
- `process_temperature_[k]`
- `rotational_speed_[rpm]`
- `torque_[nm]`
- `tool_wear_[min]`
- `machine_failure`
- `twf`
- `hdf`
- `pwf`
- `osf`
- `rnf`

### 🎯 Variável alvo
A variável alvo principal adotada no projeto é:

- **`machine_failure`** → indica ocorrência ou não de falha geral da máquina.

---

## 🔄 6. Plano de Tratamento de Dados (ETL)

O pipeline de dados segue as seguintes etapas de processamento:

### 1. Extração
A coleta dos dados é realizada a partir de arquivos `.csv` armazenados localmente no repositório.

### 2. Transformação
Nesta etapa, são executados procedimentos como:

- leitura e inspeção inicial dos dados;
- padronização dos nomes das colunas;
- verificação de valores nulos;
- verificação de duplicidades;
- identificação inicial de outliers;
- preparação da base para análise exploratória.

### 3. Carga
Após o tratamento inicial, os dados são armazenados na pasta `data/processed`, ficando prontos para as etapas de exploração, visualização e modelagem preditiva.

---

## 📊 7. Etapa Atual — M2: Análise Exploratória de Dados (EDA)

Na etapa M2, o grupo realizou a **Análise Exploratória de Dados (EDA)** com o objetivo de compreender melhor a estrutura da base e identificar padrões importantes para o problema de manutenção preditiva.

### Atividades desenvolvidas na M2
- carregamento e inspeção da base tratada;
- análise descritiva das variáveis;
- verificação de consistência e duplicidades;
- análise da distribuição da variável alvo;
- análise de variáveis categóricas e numéricas;
- identificação visual de possíveis outliers;
- construção de matriz de correlação;
- elaboração de gráficos analíticos para apoiar hipóteses iniciais.

### Principais focos da EDA
Durante esta etapa, buscou-se observar:

- o comportamento da variável de falha da máquina;
- a distribuição dos tipos de produto;
- a relação entre desgaste da ferramenta, torque e falhas;
- o comportamento da velocidade rotacional em registros com e sem falha;
- a influência da temperatura de processo na ocorrência de falhas.

---

## 📈 8. Notebook da EDA

A análise exploratória foi desenvolvida em notebook Jupyter, contendo células de código e markdown para documentação do raciocínio analítico.

### Arquivo principal
- `notebooks/M2_EDA.ipynb`

### Conteúdo do notebook
O notebook contempla:

- objetivo da análise;
- carregamento dos dados;
- estatísticas descritivas;
- visualizações gráficas;
- análise de correlação;
- identificação de outliers;
- levantamento de hipóteses;
- conclusão da etapa.

---

## 🧱 9. Estrutura do Repositório

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
│   └── M2_EDA.ipynb
│
├── scripts/                # Scripts de ETL e pré-processamento
│   ├── etl.py
│   └── preprocess.py
│
├── requirements.txt        # Dependências do projeto
├── .gitignore              # Arquivos e pastas ignorados pelo Git
└── README.md               # Documentação principal do projeto
```
--- 

## 🛠️ 10. Tecnologias Utilizadas

As principais ferramentas e bibliotecas utilizadas até o momento são:

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Jupyter Notebook / VS Code**
- **OpenPyXL**

---

## 🚀 11. Instruções para Execução

### 1. Clone este repositório
```bash
git clone https://github.com/BruBobotis/cdd_grupoE.git
### 2. Acesse a pasta do projeto
```bash
cd cdd_grupoE
### 3. Instale as dependências
```bash
py -m pip install -r .\requirements.txt
### 4. Execute o ETL inicial
```bash
py scripts/etl.py
### 5. Abra o notebook da EDA
```bash
notebooks/M2_EDA.ipynb

---

## 📅 12. Planejamento por Milestones

### 🟦 M1 — Diagnóstico e ETL
- definição do problema;
- escolha do dataset;
- criação e organização do repositório;
- estruturação inicial do pipeline de ETL;
- documentação do projeto.

### 🟨 M2 — Análise Exploratória de Dados (EDA)
- análise estatística descritiva;
- visualização das distribuições;
- análise de correlação;
- identificação de padrões e outliers;
- validação inicial de hipóteses.

### 🟧 M3 — Modelagem Preditiva
- preparação dos dados para treino;
- aplicação de algoritmos de Machine Learning;
- avaliação com métricas adequadas;
- comparação entre modelos.

### 🟥 M4 — Refinamento e Entrega Final
- ajustes no pipeline;
- melhoria dos modelos;
- apresentação dos resultados;
- possível construção de dashboard ou protótipo visual.

---

## 📌 13. Status Atual do Projeto

📍 **Fase atual:** **M2 — Análise Exploratória de Dados (EDA)**

No momento, o grupo está concentrado em:

- explorar o comportamento das variáveis do dataset;
- identificar correlações relevantes;
- detectar possíveis outliers;
- levantar hipóteses analíticas para a etapa de modelagem.

---

## 🔮 14. Próximos Passos

Os próximos passos planejados são:

- concluir e refinar a EDA;
- selecionar atributos mais relevantes;
- preparar os dados para modelagem;
- iniciar testes com algoritmos de classificação;
- comparar abordagens preditivas na M3.

---

## 🤝 15. Considerações Finais

Este projeto busca aplicar conceitos de **Ciência de Dados** em um problema real da engenharia, conectando análise de dados, automação industrial e inteligência computacional. A proposta está alinhada aos princípios da **Indústria 4.0**, com potencial para contribuir na confiabilidade de sistemas produtivos e na redução de custos operacionais.

---

## 🤖 16. Apêndice de IA

A ferramenta de IA foi utilizada como apoio em atividades de:

- organização da estrutura do repositório;
- revisão de código Python;
- apoio na construção do pipeline inicial de ETL;
- sugestões de visualizações e estruturação da EDA;
- apoio textual na documentação do projeto.

Toda interpretação dos resultados, validação das análises e conferência das informações foi realizada manualmente pelo grupo.