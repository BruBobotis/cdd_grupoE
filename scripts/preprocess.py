from pathlib import Path
import pandas as pd


INPUT_FILE = Path("data/processed/dados_tratados.csv")


def load_processed_data() -> pd.DataFrame:
    """Carrega os dados já tratados pelo ETL."""
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Arquivo processado não encontrado. Execute primeiro scripts/etl.py"
        )
    return pd.read_csv(INPUT_FILE)


def show_basic_info(df: pd.DataFrame) -> None:
    """Exibe informações básicas do dataset."""
    print("\n=== INFORMAÇÕES GERAIS ===")
    print(df.info())

    print("\n=== ESTATÍSTICAS DESCRITIVAS ===")
    print(df.describe(include="all"))


def main() -> None:
    df = load_processed_data()
    show_basic_info(df)


if __name__ == "__main__":
    main()