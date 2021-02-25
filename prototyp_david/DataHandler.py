import os
import pandas as pd

def booking_info():
    df = pd.read_csv("data/skas_data.csv", sep=";")
    df = df[['Operationsdatum', 'BehandlingsNummer']]
    df = df.dropna()
    return df

CURRENT_FILE = booking_info()


def filter_data(df, col, val):
    filtered = df.where(df[col] == val).dropna()
    return filtered.to_dict("records")


def find_similar(cell):
    if cell != None:
        row = CURRENT_FILE.iloc[cell.get('row')]
        date = row['Operationsdatum']
        print(date)
        return CURRENT_FILE.where(CURRENT_FILE['Operationsdatum'] == date).dropna()


"""df = pd.DataFrame.from_dict(CURRENT_FILE)
filter_data(df, "Operationsdatum", "2021-01-01")
filter_data(df, "Operationsdatum", "2019-01-01")"""
