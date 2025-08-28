import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_excel("voltajes.xlsx", sheet_name="Hoja 1")

# Opcional: si querés filtrar por frecuencia
frecuencias = df["Frecuencia (Hz)"].unique()

for f in frecuencias:
    df_f = df[df["Frecuencia (Hz)"] == f]
    
    plt.figure(figsize=(8,5))
    
    # Graficar Vpp con errores
    plt.errorbar(
        df_f["Voltaje (V)"], df_f["V_pp (V)"], yerr=df_f["Error V_pp (V)"], 
        fmt='o-', capsize=5, label='V_pp'
    )
    
    # Graficar Vt con errores
    plt.errorbar(
        df_f["Voltaje (V)"], df_f["V_t (V)"], yerr=df_f["Error V_t (V)"], 
        fmt='s--', capsize=5, label='Vt'
    )
    
    plt.title(f"Amplitudes vs Voltaje a Frecuencia {f} Hz")
    plt.xlabel("Voltaje (V)")
    plt.ylabel("Amplitud (V)")
    plt.legend()
    plt.grid(True)
    plt.show()
