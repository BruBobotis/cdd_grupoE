import joblib
import pandas as pd

MODEL_PATH = "models/modelo_rf.pkl"


def load_model(model_path: str = MODEL_PATH):
    """Carrega o modelo treinado salvo em disco."""
    return joblib.load(model_path)


def predict_failure(model, input_data: dict) -> int:
    """
    Recebe um dicionário com as variáveis de entrada
    e retorna a previsão de falha da máquina.
    """
    df_input = pd.DataFrame([input_data])
    prediction = model.predict(df_input)[0]
    return int(prediction)


def predict_failure_proba(model, input_data: dict) -> float | None:
    """
    Retorna a probabilidade estimada de falha, se o modelo suportar.
    """
    df_input = pd.DataFrame([input_data])

    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(df_input)[0][1]
        return float(proba)

    return None


def main():
    model = load_model()

    exemplo_entrada = {
        "type": "M",
        "air_temperature_[k]": 298.1,
        "process_temperature_[k]": 308.6,
        "rotational_speed_[rpm]": 1551,
        "torque_[nm]": 42.8,
        "tool_wear_[min]": 10
    }

    prediction = predict_failure(model, exemplo_entrada)
    probability = predict_failure_proba(model, exemplo_entrada)

    print("=== RESULTADO DA PREVISÃO ===")
    print(f"Entrada: {exemplo_entrada}")
    print(f"Previsão de falha (0 = não, 1 = sim): {prediction}")

    if probability is not None:
        print(f"Probabilidade estimada de falha: {probability:.4f}")


if __name__ == "__main__":
    main()