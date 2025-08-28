import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('../ANALISIS BACKLOG/datafiltrada_nv2.xlsx')

df = df.dropna(how='all')

df["Fecha de registro"] = pd.to_datetime(df["Fecha de registro"], format="%d/%m/%Y")

df["Mes"] = df["Fecha de registro"].dt.month
df["Año"] = df["Fecha de registro"].dt.year

group = df.groupby(["Año", "Mes"])["Numero de caso"].count().reset_index()
group = group.rename(columns={"Numero de caso": "Cantidad de casos"})

print(group)

