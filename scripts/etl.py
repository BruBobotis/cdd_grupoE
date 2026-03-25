from pathlib import Path
import pandas as pd


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
OUTPUT_FILE = PROCESSED_DIR / "dados_tratados.csv"


def ensure_directories() -> None:
    """Garante que as pastassprincipais existam."""
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


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Executa limpeza inicial."""
    df = df.dropna(how="all")
    df = df.drop_duplicates()
    return df


def save_data(df: pd.DataFrame) -> None:
    """Salva os dados tratados na pasta processed."""
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")


def main() -> None:
    print("Iniciando ETL da M1...")
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
    df = basic_cleaning(df)

    print(f"Dimensão após limpeza inicial: {df.shape}")
    print("Colunas identificadas:")
    print(list(df.columns))

    save_data(df)

    print(f"ETL concluído com sucesso. Arquivo salvo em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()