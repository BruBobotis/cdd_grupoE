# Resumo da Milestone M4

## Objetivo
Finalizar o ciclo de desenvolvimento do projeto de Ciência de Dados, elevando a maturidade técnica do modelo por meio de otimização, validação e integração com uma interface visual de monitoramento.

## Atividades desenvolvidas
- refinamento do modelo de classificação utilizado na M3;
- aplicação de otimização de hiperparâmetros com GridSearchCV;
- validação cruzada para análise de robustez do modelo;
- comparação entre modelo base e modelo otimizado;
- geração de métricas finais de desempenho;
- salvamento do modelo final para uso na aplicação;
- consolidação do dashboard funcional;
- organização profissional do repositório GitHub;
- preparação dos materiais finais de entrega.

## Entregáveis da M4
- notebook `M4_Otimizacao_Modelo.ipynb`;
- script `optimize_model.py`;
- modelo final salvo em `models/modelo_final.pkl`;
- dashboard funcional;
- README final atualizado;
- imagens do dashboard na pasta `images`;
- vídeo curto de demonstração.

### Resultados da Otimização do Modelo

Na etapa M4, foi realizada a otimização da **Árvore de Decisão** por meio de **GridSearchCV**, com validação cruzada de 5 dobras e foco na métrica **F1-score**, devido ao desbalanceamento da variável alvo.

Os melhores hiperparâmetros encontrados foram:

- **criterion:** entropy
- **max_depth:** None
- **min_samples_leaf:** 2
- **min_samples_split:** 2

### Comparação entre modelo base (M3) e modelo otimizado (M4)

| Modelo | Acurácia | Precisão | Recall | F1-score |
|--------|----------|----------|--------|----------|
| Árvore de Decisão Base (M3) | 0.9780 | 0.7143 | 0.5882 | 0.6452 |
| Árvore de Decisão Otimizada (M4) | 0.9785 | 0.6712 | 0.7206 | 0.6950 |

### Interpretação dos resultados

A otimização do modelo resultou em melhora no desempenho geral, especialmente no **recall** e no **F1-score**, que são métricas importantes para problemas com classes desbalanceadas. Embora a precisão tenha apresentado leve redução, o modelo otimizado passou a identificar uma proporção maior de falhas reais, tornando-se mais adequado para o contexto de manutenção preditiva industrial.

Dessa forma, o modelo final da solução foi definido como a **Árvore de Decisão Otimizada**, por apresentar melhor equilíbrio entre detecção de falhas e desempenho geral.