import pandas as pd
import csv

# Supongamos que tienes un archivo CSV llamado 'description.csv' con "ñññ" como delimitador
# Puedes leerlo así:
df = pd.read_csv('description.csv')

# Divide el DataFrame en grupos de 10 filas cada uno
grupos = [df.iloc[i:i+10] for i in range(0, len(df), 10)]

# Itera sobre los grupos y guarda cada uno en un archivo separado
for i, grupo in enumerate(grupos):
    nombre_archivo = f'archivo_{i + 1}.txt'  # Nombre del archivo: archivo_1.txt, archivo_2.txt, etc.

    # Guarda el grupo en un archivo de texto sin el header "descripcion" y sin comillas
    grupo.to_csv(nombre_archivo, index=False, header=False, lineterminator='^', sep='\n')

    # Lee el archivo recién creado y elimina las líneas en blanco y las comillas
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Elimina el carácter ^ del final de cada línea
    lines = [line.rstrip('^') for line in lines]

    lines = [line.strip().replace('"', '') for line in lines if line.strip()]

    # Vuelve a escribir el archivo sin las líneas en blanco y sin comillas ni el carácter ^
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_txt:
        archivo_txt.write('\n'.join(lines))
