import pandas as pd
import matplotlib.pyplot as plt

# Lectura del archivo Excel
df = pd.read_excel('../ANALISIS BACKLOG/Sabana de datos enero2023-ago2025.xlsx')

# Filtrado de columnas y datos
col = ["Numero de caso", "Fecha de registro", "Asunto", "Descripcion", "Estado", "Grupo de especialista", "Especialista", "Primer Nivel", "Segundo Nivel"]
df = df[col]
df = df[df["Grupo de especialista"] == "Nivel II - Aplicaciones"].reset_index()

# Convertimos la columna "Fecha de registro" a formato datetime
df["Fecha de registro"] = pd.to_datetime(df["Fecha de registro"], format="%d/%m/%Y")
df["Fecha de registro"] = df["Fecha de registro"].dt.strftime("%m/%Y")

#Imprimir cabezales de las tablas para visualizar datos
print(df.head())