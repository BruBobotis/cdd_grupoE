import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

DATA_PATH = "data/processed/dados_tratados.csv"
MODEL_PATH = "models/modelo_rf.pkl"


def main():
    os.makedirs("models", exist_ok=True)

    df = pd.read_csv(DATA_PATH)

    features = [
        "type",
        "air_temperature_[k]",
        "process_temperature_[k]",
        "rotational_speed_[rpm]",
        "torque_[nm]",
        "tool_wear_[min]"
    ]
    target = "machine_failure"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    categorical_features = ["type"]
    numeric_features = [
        "air_temperature_[k]",
        "process_temperature_[k]",
        "rotational_speed_[rpm]",
        "torque_[nm]",
        "tool_wear_[min]"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
            ("num", StandardScaler(), numeric_features)
        ]
    )

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    )

    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, MODEL_PATH)
    print(f"Modelo salvo com sucesso em: {MODEL_PATH}")


if __name__ == "__main__":
    main()