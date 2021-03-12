import pandas as pd


dummy_data = pd.read_csv('data.csv', sep=';')
print(dummy_data.columns.values.tolist())
