from utils import *

df = LoadCSV(config["load_path"])
df = ByPayee(df, config["payee"])

SaveCSV(FilterColumns(df=df, columns=config["columns"]), config["save_path"])

CheckDF(config["save_path"])