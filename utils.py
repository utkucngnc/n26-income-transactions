import pandas as pd

config = {
    "load_path": "C:/Users/Utku/Downloads/n26-csv-transactions.csv",
    "save_path": "C:/Users/Utku/Downloads/n26-csv-transactions-filtered.csv",
    "threshold":  0.0,
    "payee": "Landeshauptkasse Nordrhein-Westfalen fuer LBV",
    "columns": ["Date", "Payee", "Payment reference", "Amount (EUR)"]
    }

def LoadCSV(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def SaveCSV(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)
    
def ByIncome(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    return df.query(f'Amount (EUR) > {threshold}')

def ByPayee(df: pd.DataFrame, payee: str) -> pd.DataFrame:
    return df.query(f'Payee == "{payee}"')

def FilterColumns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    return df.filter(items=columns)

def CheckDF(save_path: str):
    df = LoadCSV(save_path)
    print(df)