from pathlib import Path
import pandas as pd

ARQUIVO = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "Telco-Customer-Churn.csv"
)

def test_arquivo_existe():
    assert ARQUIVO.exists()

def test_colunas_obrigatorias():
    df = pd.read_csv(ARQUIVO)
    assert {"customerID", "tenure", "MonthlyCharges", "Churn"}.issubset(df.columns)

def test_identificadores_unicos():
    df = pd.read_csv(ARQUIVO)
    assert df["customerID"].is_unique

def test_classes_validas():
    df = pd.read_csv(ARQUIVO)
    assert set(df["Churn"].unique()) == {"Yes", "No"}