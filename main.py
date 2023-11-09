from utils import *

path = "C:/Users/Utku/Downloads/n26-csv-transactions.csv"
payee = "Landeshauptkasse Nordrhein-Westfalen fuer LBV"

df = LoadCSV(path)
df = ByPayee(df, payee)
columns = ["Date", "Payee", "Amount (EUR)"]

#SaveCSV(FilterColumns(df=df, columns=columns), "C:/Users/Utku/Downloads/n26-csv-transactions-filtered.csv")