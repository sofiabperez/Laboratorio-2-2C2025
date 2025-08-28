import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("voltajes.xlsx", sheet_name="Hoja 1")
print(df.head())

V10 = df[df["Voltaje (V)"] == "10, -10"][["Frecuencia (Hz)", "Voltaje (V)", "V_pp (V)", "V_t (V)"]] 
# condicion booleana== para seleccionar filas cuya columna tenga el valor pedido
print(V10)

# Graficar Vt vs Frecuencia con barras de error
plt.errorbar(
    V10["Frecuencia (Hz)"], 
    V10["V_t (V)"], 
    yerr=V10["Error V_t (V)"],     # errores de Vt
    fmt='o-',                 # marcador y línea
    capsize=5,                # tamaño de las "capitas" de las barras
    color='b', 
    label='Vt'
)

# Graficar Vpp vs Frecuencia con errores (opcional)
plt.errorbar(
    V10["Frecuencia (Hz)"], 
    V10["V_pp (V)"], 
    yerr=V10["Error V_pp (V)"], 
    fmt='s--', 
    capsize=5, 
    color='r', 
    label='V_pp'
)

plt.title("Amplitudes en función de la frecuencia (V= 10V)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud [V]")
plt.grid(True, which="both")  # grilla log
plt.xscale('log')             # escala logaritmica en x
plt.legend()
plt.show()

