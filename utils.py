import pandas as pd    

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