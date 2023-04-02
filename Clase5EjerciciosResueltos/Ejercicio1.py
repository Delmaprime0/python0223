import pandas as pd
import sqlite3
from Ejercicio2 import lectura

datos= pd.read_csv('Clase5EjerciciosResueltos/tiktoks_1_-_tiktoks_2.csv',delimiter=',')
print(datos)
filtro=datos['Camara']
print("\n*******************El Archivo .csv filtrado*******************\n")
print(filtro)

conn = sqlite3.connect('Base.db')
filtro.to_sql('miTabla', conn, if_exists='replace', index=False)
conn.close()

lectura()