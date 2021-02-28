import os
import pandas as pd

def booking_info():
    df = pd.read_csv("data/skas_data.csv", sep=";")
    df = df[['Operationsdatum', 'BehandlingsNummer','HuvudDiagnosNamn1',
                'Operationskort Undergrupp Namn','Anestesikort']]
    df = df.dropna()
    return df



def filter_data(df, col, val):
    filtered = df.where(df[col] == val).dropna()
    return filtered.to_dict("records")



def find_similar(row_nr):
    if row_nr != None:
        row = CURRENT_FILE.iloc[row_nr]
        opCard = row['Operationskort Undergrupp Namn']
        print(row['BehandlingsNummer'])
        return CURRENT_FILE.where(CURRENT_FILE['Operationskort Undergrupp Namn'] ==  opCard).dropna()


CURRENT_FILE = booking_info()
