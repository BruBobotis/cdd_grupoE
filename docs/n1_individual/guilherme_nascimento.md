## 🧪 N1 Individual — Aprofundamento Estatístico

Como continuidade da etapa de Análise Exploratória de Dados (EDA), cada integrante do grupo desenvolveu uma investigação individual com foco em **Estatística Inferencial**, utilizando o dataset **AI4I 2020 Predictive Maintenance Dataset**. O objetivo desta atividade é verificar, por meio de testes estatísticos, se os padrões observados na etapa exploratória representam evidências reais e relevantes para o problema de manutenção preditiva, ou se podem ter ocorrido ao acaso.

Cada aluno selecionou uma variável numérica relacionada à condição operacional da máquina e avaliou sua relação com a variável alvo **`machine_failure`**, formulando hipóteses estatísticas, testando a normalidade dos dados, aplicando o teste adequado e interpretando o resultado com base em p-valor e tamanho de efeito.

### Integrante e tema individual

- **Guilherme Nascimento** — `notebooks/n1_individual/Aprofundamento_Estatistico_GuilhermeNascimento.ipynb`  
 - O aluno **Guilherme Nascimento** investigou estatisticamente a variável **`tool_wear_[min]`**, comparando máquinas com falha e sem falha no dataset AI4I 2020 Predictive Maintenance Dataset. O teste de normalidade indicou ausência de distribuição normal, levando à aplicação do **teste de Mann-Whitney U**, que apontou diferença estatisticamente significativa entre os grupos. Os resultados indicaram que máquinas com falha tendem a apresentar maior desgaste da ferramenta, sugerindo que essa variável pode ser relevante para as próximas etapas da modelagem preditiva.