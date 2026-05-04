import { GoogleGenAI, Type } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY || "" });

export interface MachineData {
  type: "M" | "L" | "H";
  airTemperature: number;
  processTemperature: number;
  rotationalSpeed: number;
  torque: number;
  toolWear: number;
}

export interface PredictionResult {
  failure: boolean;
  probability: number;
  interpretation: string;
  riskLevel: "Baixo" | "Moderado" | "Alto";
  recommendation: string;
}

export async function predictFailure(data: MachineData): Promise<PredictionResult> {
  const prompt = `
    Aja como um modelo de Classificação supervisionada com Árvore de Decisão especializado no "AI4I 2020 Predictive Maintenance Dataset". 
    Analise os seguintes parâmetros operacionais de uma máquina industrial:
    - Tipo do Produto: ${data.type}
    - Temperatura do Ar: ${data.airTemperature} K
    - Temperatura de Processo: ${data.processTemperature} K
    - Velocidade Rotacional: ${data.rotationalSpeed} rpm
    - Torque: ${data.torque} Nm
    - Desgaste da Ferramenta: ${data.toolWear} min

    Com base na lógica de Árvore de Decisão aplicada a este dataset, identifique padrões de:
    1. Heat Dissipation Failure (HDF): Diferença de temperatura < 8.6K e torque > 40Nm.
    2. Power Failure (PWF): Torque < 3.8Nm ou > 76.9Nm.
    3. Overload Failure (OSF): Desgaste da ferramenta * torque excedendo limites críticos para o tipo de produto.
    4. Tool Wear Failure (TWF): Desgaste da ferramenta próximo ou superior a 200 min.

    Retorne o resultado estritamente no formato JSON com:
    - failure: booleano (true se houver falha, false caso contrário)
    - probability: número real entre 0 e 1 representando a probabilidade de falha
    - riskLevel: string ("Baixo", "Moderado" ou "Alto")
    - interpretation: justificativa técnica curta explicando quais variáveis contribuíram para o resultado
    - recommendation: recomendação operacional específica (ex: "manter monitoramento", "inspecionar componente", "planejar manutenção")
  `;

  try {
    const response = await ai.models.generateContent({
      model: "gemini-3-flash-preview",
      contents: prompt,
      config: {
        responseMimeType: "application/json",
        responseSchema: {
          type: Type.OBJECT,
          properties: {
            failure: { type: Type.BOOLEAN },
            probability: { type: Type.NUMBER },
            riskLevel: { type: Type.STRING, enum: ["Baixo", "Moderado", "Alto"] },
            interpretation: { type: Type.STRING },
            recommendation: { type: Type.STRING },
          },
          required: ["failure", "probability", "riskLevel", "interpretation", "recommendation"],
        },
      },
    });

    const result = JSON.parse(response.text || "{}");
    return {
      failure: result.failure ?? false,
      probability: result.probability ?? 0,
      riskLevel: result.riskLevel ?? "Baixo",
      interpretation: result.interpretation ?? "Análise inconclusiva.",
      recommendation: result.recommendation ?? "Monitorar parâmetros.",
    };
  } catch (error) {
    console.error("Erro na predição:", error);
    return {
      failure: false,
      probability: 0,
      riskLevel: "Baixo",
      interpretation: "Erro ao conectar com o serviço de análise.",
      recommendation: "Tente novamente mais tarde.",
    };
  }
}
