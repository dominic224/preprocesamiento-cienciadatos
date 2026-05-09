import pandas as pd 
import numpy as np

def cargar_datos(ruta):
    return pd.read_csv(ruta)

def eliminar_nulos(df):
    return df.dropna()

def eliminar_duplicados(df):
    return df.drop_duplicates()

print("Preprocesamiento completado")
