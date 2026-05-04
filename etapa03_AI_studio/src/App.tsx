/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import { useState } from "react";
import { motion, AnimatePresence } from "motion/react";
import { 
  AlertTriangle, 
  CheckCircle2, 
  Settings, 
  Thermometer, 
  RotateCw, 
  Wrench, 
  Zap, 
  BarChart3,
  Loader2
} from "lucide-react";
import { predictFailure, MachineData, PredictionResult } from "./services/geminiService";

export default function App() {
  const [formData, setFormData] = useState<MachineData>({
    type: "L",
    airTemperature: 300,
    processTemperature: 310,
    rotationalSpeed: 1500,
    torque: 40,
    toolWear: 0,
  });

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionResult | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    const prediction = await predictFailure(formData);
    setResult(prediction);
    setLoading(false);
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === "type" ? value : parseFloat(value) || 0,
    }));
  };

  return (
    <div className="min-h-screen bg-[#F0F2F5] text-slate-900 font-sans p-4 md:p-8">
      <div className="max-w-4xl mx-auto">
        {/* Header */}
        <header className="mb-10 text-center md:text-left border-l-4 border-slate-800 pl-6 py-2">
          <h1 className="text-3xl font-light tracking-tight text-slate-800 flex items-center gap-3">
            <Settings className="w-8 h-8 text-slate-600" />
            Sistema de Manutenção Preditiva
          </h1>
          <p className="text-slate-500 mt-2 font-medium italic text-sm leading-relaxed">
            Sistema de apoio à manutenção preditiva baseado em variáveis operacionais para detecção precoce de falhas em máquinas industriais.
          </p>
          <p className="text-slate-400 mt-1 font-semibold text-xs uppercase tracking-tighter">
            Protótipo acadêmico desenvolvido para a disciplina de Ciência de Dados.
          </p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Input Form */}
          <section className="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
            <h2 className="text-xs uppercase tracking-widest font-bold text-slate-400 mb-6 flex items-center gap-2">
              <BarChart3 className="w-4 h-4" />
              Parâmetros de Entrada
            </h2>
            
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-sm font-semibold text-slate-700 mb-1">Tipo do Produto</label>
                <select
                  name="type"
                  value={formData.type}
                  onChange={handleInputChange}
                  className="w-full bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-slate-400 transition-all"
                >
                  <option value="L">Low (L)</option>
                  <option value="M">Medium (M)</option>
                  <option value="H">High (H)</option>
                </select>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <InputGroup
                  label="Temp. Ar (K)"
                  name="airTemperature"
                  value={formData.airTemperature}
                  onChange={handleInputChange}
                  icon={<Thermometer className="w-4 h-4 text-sky-500" />}
                />
                <InputGroup
                  label="Temp. Processo (K)"
                  name="processTemperature"
                  value={formData.processTemperature}
                  onChange={handleInputChange}
                  icon={<Thermometer className="w-4 h-4 text-orange-500" />}
                />
              </div>

              <div className="grid grid-cols-2 gap-4">
                <InputGroup
                  label="Rotacional (rpm)"
                  name="rotationalSpeed"
                  value={formData.rotationalSpeed}
                  onChange={handleInputChange}
                  icon={<RotateCw className="w-4 h-4 text-emerald-500" />}
                />
                <InputGroup
                  label="Torque (Nm)"
                  name="torque"
                  value={formData.torque}
                  onChange={handleInputChange}
                  icon={<Zap className="w-4 h-4 text-amber-500" />}
                />
              </div>

              <InputGroup
                label="Desgaste Ferramenta (min)"
                name="toolWear"
                value={formData.toolWear}
                onChange={handleInputChange}
                icon={<Wrench className="w-4 h-4 text-slate-500" />}
              />

              <button
                type="submit"
                disabled={loading}
                className="w-full mt-6 bg-slate-800 text-white rounded-lg py-3 font-bold text-sm tracking-wide hover:bg-slate-900 transition-colors flex items-center justify-center gap-2 disabled:opacity-50"
              >
                {loading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    Processando...
                  </>
                ) : (
                  "Prever Falha"
                )}
              </button>
            </form>
          </section>

          {/* Result Area */}
          <section className="flex flex-col gap-8">
            <AnimatePresence mode="wait">
              {result ? (
                <motion.div
                  key="result"
                  initial={{ opacity: 0, scale: 0.95 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.95 }}
                  className={`flex-1 rounded-xl p-8 flex flex-col items-center justify-center text-center shadow-lg border-2 ${
                    result.failure 
                      ? "bg-red-50 border-red-200 text-red-900" 
                      : "bg-emerald-50 border-emerald-200 text-emerald-900"
                  }`}
                >
                  <div className="mb-4">
                    {result.failure ? (
                      <AlertTriangle className="w-16 h-16 text-red-500" />
                    ) : (
                      <CheckCircle2 className="w-16 h-16 text-emerald-500" />
                    )}
                  </div>
                  
                  <h3 className="text-2xl font-bold uppercase tracking-tighter mb-4 text-slate-800">
                    Resultado da Análise
                  </h3>
                  
                  <div className="w-full space-y-4 text-left">
                    <ResultItem 
                      label="1. Classificação final" 
                      value={result.failure ? "Falha" : "Sem falha"} 
                      highlight={result.failure ? "text-red-600" : "text-emerald-600"}
                    />
                    <ResultItem 
                      label="2. Nível de risco" 
                      value={result.riskLevel} 
                      highlight={
                        result.riskLevel === "Alto" ? "text-red-600" : 
                        result.riskLevel === "Moderado" ? "text-amber-600" : "text-emerald-600"
                      }
                    />
                    <ResultItem 
                      label="3. Probabilidade estimada" 
                      value={`${(result.probability * 100).toFixed(1)}%`} 
                    />
                    <div className="border-t border-slate-200 pt-4">
                      <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">4. Justificativa técnica</p>
                      <p className="text-sm italic leading-relaxed text-slate-700">{result.interpretation}</p>
                    </div>
                    <div className="border-t border-slate-200 pt-4">
                      <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">5. Recomendação operacional</p>
                      <p className="text-sm font-bold text-slate-800 flex items-center gap-2">
                        <CheckCircle2 className="w-4 h-4 text-slate-400" />
                        {result.recommendation}
                      </p>
                    </div>
                  </div>
                </motion.div>
              ) : (
                <div className="flex-1 bg-white p-8 rounded-xl border border-dashed border-slate-300 flex flex-col items-center justify-center text-center text-slate-400">
                  <BarChart3 className="w-12 h-12 mb-4 opacity-20" />
                  <p className="font-medium italic">Aguardando dados para processamento...</p>
                </div>
              )}
            </AnimatePresence>

            {/* Academic Notes */}
            <div className="bg-slate-800 text-slate-300 p-5 rounded-xl text-[10px] uppercase tracking-widest font-bold leading-loose shadow-sm">
              <div className="flex items-center gap-2 mb-2 text-slate-100">
                <div className="w-2 h-2 bg-sky-400 rounded-full animate-pulse" />
                Notas Técnicas
              </div>
              <p>MODELO: Classificação supervisionada com Árvore de Decisão</p>
              <p>DATASET: AI4I 2020 Predictive Maintenance Dataset</p>
              <p>VARIÁVEIS: tipo, temperatura do ar, temperatura de processo, rotação, torque e desgaste da ferramenta</p>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
}

function ResultItem({ label, value, highlight }: { label: string; value: string; highlight?: string }) {
  return (
    <div>
      <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-0.5">{label}</p>
      <p className={`text-lg font-black tracking-tight ${highlight || "text-slate-800"}`}>{value}</p>
    </div>
  );
}

function InputGroup({ label, name, value, onChange, icon }: { 
  label: string; 
  name: string; 
  value: number; 
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  icon: React.ReactNode;
}) {
  return (
    <div className="flex flex-col">
      <label className="text-xs font-bold text-slate-400 uppercase tracking-wider mb-1 flex items-center gap-2">
        {icon}
        {label}
      </label>
      <input
        type="number"
        name={name}
        value={value}
        onChange={onChange}
        className="bg-slate-50 border border-slate-200 rounded-lg px-4 py-2 text-sm font-mono focus:outline-none focus:ring-2 focus:ring-slate-400 transition-all"
        step="any"
      />
    </div>
  );
}

