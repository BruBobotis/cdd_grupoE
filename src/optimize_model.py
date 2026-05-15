import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

DATA_PATH = "data/processed/dados_tratados.csv"
MODEL_PATH = "models/modelo_final.pkl"


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

    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", DecisionTreeClassifier(random_state=42, class_weight="balanced"))
    ])

    param_grid = {
        "model__criterion": ["gini", "entropy"],
        "model__max_depth": [3, 5, 7, 10, None],
        "model__min_samples_split": [2, 5, 10, 20],
        "model__min_samples_leaf": [1, 2, 4, 8]
    }

    grid_search = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        scoring="f1",
        cv=5,
        n_jobs=-1,
        verbose=1
    )

    grid_search.fit(X_train, y_train)

    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)

    print("=== MELHORES PARÂMETROS ===")
    print(grid_search.best_params_)

    print("\n=== MÉTRICAS NO TESTE ===")
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print("Precisão:", precision_score(y_test, y_pred, zero_division=0))
    print("Recall:", recall_score(y_test, y_pred, zero_division=0))
    print("F1-score:", f1_score(y_test, y_pred, zero_division=0))

    joblib.dump(best_model, MODEL_PATH)
    print(f"\nModelo final salvo em: {MODEL_PATH}")


if __name__ == "__main__":
    main()