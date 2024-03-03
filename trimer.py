import pandas as pd
import csv


df = pd.read_csv('description.csv')

grupos = [df.iloc[i:i+10] for i in range(0, len(df), 10)]

for i, grupo in enumerate(grupos):
    nombre_archivo = f'archivo_{i + 1}.txt' 

    grupo.to_csv(nombre_archivo, index=False, header=False, lineterminator='^', sep='\n')

    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.rstrip('^') for line in lines]

    lines = [line.strip().replace('"', '') for line in lines if line.strip()]

    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_txt:
        archivo_txt.write('\n'.join(lines))
