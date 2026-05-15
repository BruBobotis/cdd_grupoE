from pathlib import Path
import pandas as pd


INPUT_FILE = Path("data/processed/dados_tratados.csv")


def load_processed_data() -> pd.DataFrame:
    """Carrega os dados tratados."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Arquivo processado não encontrado. Execute antes o script scripts/etl.py"
        )
    return pd.read_csv(INPUT_FILE)


def show_basic_info(df: pd.DataFrame) -> None:
    """Mostra informações básicas da base."""
    print("\n=== DIMENSÃO ===")
    print(df.shape)

    print("\n=== INFORMAÇÕES GERAIS ===")
    print(df.info())

    print("\n=== ESTATÍSTICAS DESCRITIVAS ===")
    print(df.describe(include="all"))

    print("\n=== VALORES NULOS ===")
    print(df.isnull().sum())

    print("\n=== DUPLICATAS ===")
    print(df.duplicated().sum())


def main() -> None:
    df = load_processed_data()
    show_basic_info(df)


if __name__ == "__main__":
    main()