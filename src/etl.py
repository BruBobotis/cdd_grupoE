from pathlib import Path
import pandas as pd


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
OUTPUT_FILE = PROCESSED_DIR / "dados_tratados.csv"


def ensure_directories() -> None:
    """Garante que as pastas principais existam."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def find_input_file() -> Path | None:
    """Procura o primeiro arquivo CSV ou XLSX dentro de data/raw."""
    supported_extensions = [".csv", ".xlsx"]
    for file_path in RAW_DIR.iterdir():
        if file_path.suffix.lower() in supported_extensions:
            return file_path
    return None


def load_data(file_path: Path) -> pd.DataFrame:
    """Carrega os dados de um arquivo CSV ou XLSX."""
    if file_path.suffix.lower() == ".csv":
        return pd.read_csv(file_path)
    if file_path.suffix.lower() == ".xlsx":
        return pd.read_excel(file_path)
    raise ValueError(f"Formato não suportado: {file_path.suffix}")


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza nomes de colunas."""
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
        .str.replace("/", "_", regex=False)
    )
    return df


def basic_cleaning(df: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    """Remove linhas totalmente vazias e duplicadas."""
    df = df.dropna(how="all")
    duplicated_count = df.duplicated().sum()
    df = df.drop_duplicates()
    return df, duplicated_count


def show_dataset_summary(df: pd.DataFrame) -> None:
    """Exibe resumo do dataset."""
    print("\n=== RESUMO DO DATASET ===")
    print(f"Quantidade de linhas: {df.shape[0]}")
    print(f"Quantidade de colunas: {df.shape[1]}")

    print("\n=== COLUNAS IDENTIFICADAS ===")
    print(list(df.columns))

    print("\n=== TIPOS DAS COLUNAS ===")
    print(df.dtypes)

    print("\n=== VALORES NULOS POR COLUNA ===")
    print(df.isnull().sum())

    print("\n=== PRÉVIA DOS DADOS ===")
    print(df.head())


def save_data(df: pd.DataFrame) -> None:
    """Salva os dados tratados na pasta processed."""
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")


def main() -> None:
    print("Iniciando ETL da M1/M2...")
    ensure_directories()

    input_file = find_input_file()

    if input_file is None:
        print("Nenhum arquivo .csv ou .xlsx encontrado em data/raw.")
        print("Adicione o dataset bruto para continuar.")
        return

    print(f"Arquivo encontrado: {input_file}")

    df = load_data(input_file)
    print(f"Dimensão original: {df.shape}")

    df = standardize_columns(df)
    df, duplicated_count = basic_cleaning(df)

    print(f"Dimensão após limpeza inicial: {df.shape}")
    print(f"Quantidade de linhas duplicadas removidas: {duplicated_count}")

    show_dataset_summary(df)
    save_data(df)

    print(f"\nETL concluído com sucesso. Arquivo salvo em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()