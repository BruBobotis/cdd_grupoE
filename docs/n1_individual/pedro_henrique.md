## 🧪 N1 Individual — Aprofundamento Estatístico

Como continuidade da etapa de Análise Exploratória de Dados (EDA), cada integrante do grupo desenvolveu uma investigação individual com foco em **Estatística Inferencial**, utilizando o dataset **AI4I 2020 Predictive Maintenance Dataset**. O objetivo desta atividade é verificar, por meio de testes estatísticos, se os padrões observados na etapa exploratória representam evidências reais e relevantes para o problema de manutenção preditiva, ou se podem ter ocorrido ao acaso.

Cada aluno selecionou uma variável numérica relacionada à condição operacional da máquina e avaliou sua relação com a variável alvo **`machine_failure`**, formulando hipóteses estatísticas, testando a normalidade dos dados, aplicando o teste adequado e interpretando o resultado com base em p-valor e tamanho de efeito.

### Integrante e tema individual

- **Pedro Henrique Mateus** — `notebooks/n1_individual/Aprofundamento_Estatistico_PedroHenrique.ipynb`  
  
  O aluno **Pedro Henrique Mateus** investigou estatisticamente a variável **`rotational_speed_[rpm]`**, comparando máquinas com falha e sem falha no dataset AI4I 2020 Predictive Maintenance Dataset. O teste de normalidade indicou ausência de distribuição normal, levando à aplicação do **teste de Mann-Whitney U**, que apresentou **p-valor < 0,001**. O resultado permitiu rejeitar a hipótese nula, indicando diferença estatisticamente significativa entre os grupos. Entretanto, o tamanho do efeito (**Cohen’s d = 0,2444**) foi pequeno, sugerindo que a velocidade rotacional possui associação estatística com a falha, mas com relevância prática limitada para a modelagem preditiva. 