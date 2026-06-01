# 🔧 Projeto: Manutenção Preditiva de "Zero-Downtime"

> Projeto desenvolvido para a disciplina de **Ciência de Dados**, com foco na aplicação de técnicas de **análise de dados**, **ETL**, **Análise Exploratória de Dados (EDA)** e **Machine Learning** em um cenário de **manutenção preditiva industrial**.

---

## 👥 1. Identificação do Grupo

- **Instituição:** Faculdade Engenheiro Salvador Arena  
- **Curso:** Engenharia de Controle e Automação  
- **Disciplina:** Ciência de Dados  
- **Grupo:** E  

### Integrantes
- **Bruno Alves Guirado** - RA: [062210033]
- **Guilherme Nascimento** - RA: [062210016]
- **Guilherme Fernando** - RA: [062210038]
- **Lucas Guedes** - RA: [062210002]
- **Pedro Henrique Mateus** - RA: [062220039]

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
Desenvolver um pipeline de dados capaz de organizar, tratar, analisar e modelar informações operacionais de equipamentos industriais, servindo de base para modelos de **Machine Learning aplicados à manutenção preditiva**.

### Objetivos Específicos
- selecionar um dataset compatível com o tema proposto;
- estruturar o processo de **ETL**;
- realizar a **Análise Exploratória de Dados (EDA)**;
- identificar correlações, padrões e possíveis outliers;
- preparar os dados para as etapas de modelagem;
- desenvolver e avaliar modelos preditivos;
- contribuir para a redução de falhas inesperadas em equipamentos industriais.

---

## 🗂️ 5. Arquitetura de Dados (Fonte e Dataset)

O projeto utiliza um conjunto de dados estruturado com informações associadas à condição operacional de equipamentos industriais.

### 📥 Origem dos Dados
Os dados foram obtidos a partir de um dataset público de manutenção preditiva.

### Dataset selecionado
Para as etapas do projeto, o grupo utiliza o **AI4I 2020 Predictive Maintenance Dataset**, disponibilizado pela **UCI Machine Learning Repository**. A base foi escolhida por ser voltada especificamente para manutenção preditiva industrial, contendo **10.000 registros** e variáveis operacionais relevantes para análise de falhas, como:

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
- preparação da base para análise exploratória e modelagem.

### 3. Carga
Após o tratamento inicial, os dados são armazenados na pasta `data/processed`, ficando prontos para as etapas de exploração, visualização e modelagem preditiva.

---

## 📊 7. Etapas Desenvolvidas

### M2 — Análise Exploratória de Dados (EDA)
Na etapa M2, o grupo realizou a **Análise Exploratória de Dados (EDA)** com o objetivo de compreender melhor a estrutura da base e identificar padrões importantes para o problema de manutenção preditiva.

#### Atividades desenvolvidas na M2
- carregamento e inspeção da base tratada;
- análise descritiva das variáveis;
- verificação de consistência e duplicidades;
- análise da distribuição da variável alvo;
- análise de variáveis categóricas e numéricas;
- identificação visual de possíveis outliers;
- construção de matriz de correlação;
- elaboração de gráficos analíticos para apoiar hipóteses iniciais.

#### Principais focos da EDA
Durante esta etapa, buscou-se observar:

- o comportamento da variável de falha da máquina;
- a distribuição dos tipos de produto;
- a relação entre desgaste da ferramenta, torque e falhas;
- o comportamento da velocidade rotacional em registros com e sem falha;
- a influência da temperatura de processo na ocorrência de falhas.

### M3 — Modelagem de IA
Na etapa M3, o grupo iniciou a transformação dos achados da EDA em uma solução prática de **Machine Learning**, com foco na predição da variável **`machine_failure`**.

#### Atividades desenvolvidas na M3
- seleção das variáveis preditoras relevantes;
- preparação da base para treino e teste;
- treinamento de modelos de classificação;
- avaliação de desempenho com métricas adequadas;
- comparação entre abordagens de modelagem;
- definição do modelo com melhor desempenho para o problema proposto.

---

## 📈 8. Notebooks e Modelagem

### Arquivos principais
- `notebooks/M2_EDA.ipynb`
- `notebooks/M3_Modelagem_IA.ipynb`

### Conteúdo do notebook da M2
O notebook contempla:

- objetivo da análise;
- carregamento dos dados;
- estatísticas descritivas;
- visualizações gráficas;
- análise de correlação;
- identificação de outliers;
- levantamento de hipóteses;
- conclusão da etapa.

### Conteúdo do notebook da M3
O notebook contempla:

- preparação dos dados para modelagem;
- definição das variáveis de entrada e saída;
- separação entre treino e teste;
- treinamento dos modelos;
- avaliação de desempenho;
- comparação entre modelos;
- seleção do modelo final.

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
│   ├── M2_EDA.ipynb
│   ├── M3_Modelagem_IA.ipynb
│   └── n1_individual/
│
├── scripts/                # Scripts de ETL, pré-processamento e modelagem
│   ├── etl.py
│   ├── preprocess.py
│   ├── train_model.py
│   └── predict.py
│
├── models/                 # Modelos treinados/exportados
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
```

### 2. Acesse a pasta do projeto

```bash
cd cdd_grupoE
```

### 3. Instale as dependências

```bash
py -m pip install -r .\requirements.txt
```
### 4. Execute o ETL inicial
```bash
py scripts/etl.py
```
### 5. Abra o notebook da EDA
```bash
notebooks/M2_EDA.ipynb
```
### 6. Abra o notebook da Modelagem
```bash
notebooks/M3_Modelagem_IA.ipynb
```
### 7. Execute o script de treino do modelo (quando disponível)
```bash
py scripts/train_model.py
```
---

## 🤖 12. Modelagem Preditiva

### Problema de modelagem
O problema foi tratado como uma tarefa de **classificação supervisionada**, com o objetivo de prever a ocorrência de falha da máquina com base nas variáveis operacionais do dataset.

### Variável alvo
- `machine_failure`

### Variáveis preditoras utilizadas
- `type`
- `air_temperature_[k]`
- `process_temperature_[k]`
- `rotational_speed_[rpm]`
- `torque_[nm]`
- `tool_wear_[min]`

### Variáveis descartadas
- `udi`
- `product_id`

Essas variáveis foram descartadas por atuarem como identificadores, sem contribuição relevante esperada para a predição.

### Modelos avaliados
- **Regressão Logística**
- **Árvore de Decisão**
- **Random Forest**

### Modelo selecionado na M3
**Árvore de Decisão**

### Métricas obtidas na M3
- **Acurácia:** 0.9780
- **Precisão:** 0.7143
- **Recall:** 0.5882
- **F1-score:** 0.6452

### Matriz de confusão da M3
A matriz de confusão do melhor modelo da M3 apresentou os seguintes resultados:

- **Verdadeiros Negativos (TN):** 1916
- **Falsos Positivos (FP):** 16
- **Falsos Negativos (FN):** 28
- **Verdadeiros Positivos (TP):** 40

### Interpretação dos resultados da M3
Os resultados obtidos indicaram que a **Árvore de Decisão** foi o modelo com melhor desempenho entre os algoritmos avaliados na etapa M3, principalmente ao considerar o **F1-score**, adotado como métrica principal devido ao desbalanceamento da variável alvo. O modelo apresentou alta acurácia e desempenho satisfatório na identificação da classe de falha, sendo selecionado como base para a etapa de refinamento técnico da M4.

---

## 🚀 13. Resultados da Otimização do Modelo (M4)

Na etapa M4, foi realizada a otimização da **Árvore de Decisão** por meio de **GridSearchCV**, com validação cruzada de 5 dobras e foco na métrica **F1-score**, devido ao desbalanceamento da variável alvo.

### Melhores hiperparâmetros encontrados
- **criterion:** entropy
- **max_depth:** None
- **min_samples_leaf:** 2
- **min_samples_split:** 2

### Comparação entre modelo base (M3) e modelo otimizado (M4)

| Modelo | Acurácia | Precisão | Recall | F1-score |
|--------|----------|----------|--------|----------|
| Árvore de Decisão Base (M3) | 0.9780 | 0.7143 | 0.5882 | 0.6452 |
| Árvore de Decisão Otimizada (M4) | 0.9785 | 0.6712 | 0.7206 | 0.6950 |

### Matriz de confusão do modelo otimizado
A matriz de confusão do modelo final apresentou os seguintes resultados:

- **Verdadeiros Negativos (TN):** 1908
- **Falsos Positivos (FP):** 24
- **Falsos Negativos (FN):** 19
- **Verdadeiros Positivos (TP):** 49

### Interpretação dos resultados
A otimização do modelo resultou em melhora no desempenho geral, especialmente no **recall** e no **F1-score**, que são métricas fundamentais em problemas com classes desbalanceadas. Embora a precisão tenha apresentado leve redução, o modelo otimizado passou a identificar uma quantidade maior de falhas reais, o que é desejável no contexto de manutenção preditiva industrial.

A matriz de confusão mostra que o modelo mantém excelente capacidade de reconhecer máquinas sem falha, ao mesmo tempo em que aumenta a detecção dos casos positivos de falha. Dessa forma, a solução final tornou-se mais robusta e mais adequada para apoiar decisões de manutenção.

### Modelo final selecionado
O modelo final adotado pelo grupo foi a **Árvore de Decisão Otimizada**, por apresentar melhor equilíbrio entre desempenho geral, interpretabilidade e capacidade de detecção de falhas.

---

## 🌐 14. Protótipo e Integração

### Link do protótipo no Google AI Studio
**(https://ai.studio/apps/537d8210-d70f-4d54-b574-368bb188dc8a)**

### Observação sobre a implementação
O desenvolvimento analítico e a modelagem preditiva do projeto foram conduzidos em **Python**, utilizando **VS Code** e notebooks Jupyter. O **Google AI Studio** foi utilizado como ambiente complementar de prototipação, permitindo disponibilizar uma interface interativa para inserção de variáveis operacionais e visualização da previsão de falha da máquina.

O protótipo desenvolvido permite ao usuário informar o tipo do produto, temperatura do ar, temperatura de processo, velocidade rotacional, torque e desgaste da ferramenta, retornando uma classificação final (**Falha** ou **Sem falha**), nível de risco, probabilidade estimada, justificativa técnica e recomendação operacional.

Essa integração permitiu transformar os resultados da modelagem em uma solução visual e funcional, alinhada à proposta da etapa M3.

---

## 📅 15. Planejamento por Milestones

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
- comparação entre modelos;
- definição do modelo final.

### 🟥 M4 — Refinamento e Entrega Final
- ajustes no pipeline;
- melhoria dos modelos;
- apresentação dos resultados;
- refinamento técnico da solução.

---

## 📌 16. Status Atual do Projeto

📍 **Fase atual:** **M4 — Refinamento, Otimização e Entrega Final**

No momento, o grupo está concentrado em:

- otimizar o modelo final por meio de ajuste de hiperparâmetros;
- validar a robustez da solução com validação cruzada;
- consolidar o dashboard funcional no Google AI Studio;
- organizar o repositório final com estrutura profissional;
- preparar os materiais finais de documentação e apresentação.

---

## 🔮 17. Próximos Passos

Os próximos passos planejados são:

- consolidar os resultados finais da M4 no repositório;
- publicar e validar o dashboard funcional;
- adicionar imagens e evidências visuais do projeto na pasta `images/`;
- finalizar a documentação técnica e o apêndice de IA;
- gravar o vídeo curto de apresentação da solução;
- realizar a entrega final do projeto.

---

## 🤝 18. Considerações Finais

Este projeto busca aplicar conceitos de **Ciência de Dados** em um problema real da engenharia, conectando análise de dados, automação industrial e inteligência computacional. A proposta está alinhada aos princípios da **Indústria 4.0**, com potencial para contribuir na confiabilidade de sistemas produtivos e na redução de custos operacionais.

Ao longo das etapas desenvolvidas, o grupo estruturou o pipeline de dados, explorou estatisticamente o dataset, validou hipóteses relevantes, treinou modelos de classificação e refinou tecnicamente a solução por meio de otimização de hiperparâmetros e validação cruzada.

Como resultado final, o projeto passou a contar com uma solução preditiva funcional, integrada a um protótipo visual no **Google AI Studio**, permitindo transformar dados operacionais em uma aplicação prática de apoio à manutenção preditiva industrial.

---

## 🤖 19. Apêndice de IA

A ferramenta de IA foi utilizada como apoio em atividades de:

- organização da estrutura do repositório;
- revisão de código Python;
- apoio na construção do pipeline inicial de ETL;
- sugestões de visualizações e estruturação da EDA;
- apoio na estruturação da etapa de modelagem preditiva;
- apoio textual na documentação do projeto.

Toda interpretação dos resultados, validação das análises, conferência das métricas e avaliação dos modelos foi realizada manualmente pelo grupo.

---

## 🧪 20. N1 Individual — Aprofundamento Estatístico

Como continuidade da etapa de Análise Exploratória de Dados (EDA), cada integrante do grupo desenvolveu uma investigação individual com foco em **Estatística Inferencial**, utilizando o dataset **AI4I 2020 Predictive Maintenance Dataset**. O objetivo desta atividade foi verificar, por meio de testes estatísticos, se os padrões observados na etapa exploratória representam evidências relevantes para o problema de manutenção preditiva.

### Integrantes e temas individuais

- **Bruno Alves Guirado** — `notebooks/n1_individual/Aprofundamento_Estatistico_BrunoAlvesGuirado.ipynb`  
  O aluno investigou estatisticamente a variável **`torque_[nm]`**, comparando máquinas com falha e sem falha. Os resultados indicaram diferença estatisticamente significativa entre os grupos, com evidência de maior torque em máquinas com falha e tamanho de efeito elevado.

- **Lucas Guedes** — `notebooks/n1_individual/Aprofundamento_Estatistico_LucasGuedes.ipynb`  
  O aluno investigou estatisticamente a variável **`process_temperature_[k]`**, comparando máquinas com falha e sem falha. Os resultados indicaram diferença estatisticamente significativa entre os grupos, porém com efeito prático pequeno.

- **Pedro Henrique Mateus** — `notebooks/n1_individual/Aprofundamento_Estatistico_PedroHenrique.ipynb`  
  O aluno investigou estatisticamente a variável **`rotational_speed_[rpm]`**, comparando máquinas com falha e sem falha. Os resultados indicaram diferença estatisticamente significativa entre os grupos, com velocidade rotacional inferior nas máquinas com falha, mas com efeito prático pequeno.

- **Guilherme Nascimento** — `notebooks/n1_individual/Aprofundamento_Estatistico_GuilhermeNascimento.ipynb`  
  O aluno investigou estatisticamente a variável **`tool_wear_[min]`**, comparando máquinas com falha e sem falha. Os resultados indicaram associação estatisticamente significativa entre o desgaste da ferramenta e a ocorrência de falhas, reforçando a relevância da variável para o problema estudado.

## 🚀 21. Resultados da Otimização do Modelo (M4)

Na etapa M4, foi realizada a otimização da **Árvore de Decisão** por meio de **GridSearchCV**, com validação cruzada de 5 dobras e foco na métrica **F1-score**, devido ao desbalanceamento da variável alvo.

### Melhores hiperparâmetros encontrados
- **criterion:** entropy
- **max_depth:** None
- **min_samples_leaf:** 2
- **min_samples_split:** 2

### Comparação entre modelo base (M3) e modelo otimizado (M4)

| Modelo | Acurácia | Precisão | Recall | F1-score |
|--------|----------|----------|--------|----------|
| Árvore de Decisão Base (M3) | 0.9780 | 0.7143 | 0.5882 | 0.6452 |
| Árvore de Decisão Otimizada (M4) | 0.9785 | 0.6712 | 0.7206 | 0.6950 |

### Matriz de confusão do modelo otimizado
A matriz de confusão do modelo final apresentou os seguintes resultados:

- **Verdadeiros Negativos (TN):** 1908
- **Falsos Positivos (FP):** 24
- **Falsos Negativos (FN):** 19
- **Verdadeiros Positivos (TP):** 49

### Interpretação dos resultados
A otimização do modelo resultou em melhora no desempenho geral, especialmente no **recall** e no **F1-score**, que são métricas fundamentais em problemas com classes desbalanceadas. Embora a precisão tenha apresentado leve redução, o modelo otimizado passou a identificar uma quantidade maior de falhas reais, o que é desejável no contexto de manutenção preditiva industrial.

A matriz de confusão mostra que o modelo mantém excelente capacidade de reconhecer máquinas sem falha, ao mesmo tempo em que aumenta a detecção dos casos positivos de falha. Dessa forma, a solução final tornou-se mais robusta e mais adequada para apoiar decisões de manutenção.

### Modelo final selecionado
O modelo final adotado pelo grupo foi a **Árvore de Decisão Otimizada**, por apresentar melhor equilíbrio entre desempenho geral, interpretabilidade e capacidade de detecção de falhas.