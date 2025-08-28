import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos desde Excel
df = pd.read_excel("voltajes.xlsx", sheet_name="Hoja 1")

pendientes = []

# Recorremos cada frecuencia
for f in df["Frecuencia (Hz)"].unique():
    datos = df[df["Frecuencia (Hz)"] == f]

    # Variables
    x = datos["V_pp (V)"].values
    y = datos["V_t (V)"].values
    
    #Errores
    err_x=datos["Error V_pp (V)"].values
    err_y=datos["Error V_t (V)"].values
    
    

    # Ajuste lineal
    coef = np.polyfit(x, y, 1)  # grado 1 -> recta
    m, b = coef
    pendientes.append((f, m))

    # Graficar con barras de error
    plt.errorbar(x, y, xerr=err_x, yerr=err_y, fmt="o", color="blue", ecolor="black", capsize=4, label="Datos con error")
    plt.plot(x, m*x + b, color="red", label=f"Ajuste: y={m:.2f}x+{b:.2f}")

    plt.xlabel("Vpp (V)")
    plt.ylabel("Vt (V)")
    plt.title(f"Vt vs Vpp a frecuencia {f} Hz")
    plt.legend()
    plt.show()

# Crear tabla de pendientes
tabla_pendientes = pd.DataFrame(pendientes, columns=["Frecuencia (Hz)", "Pendiente"])
print(tabla_pendientes)
