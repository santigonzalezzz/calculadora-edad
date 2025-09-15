import tkinter as tk

def calcular_edad():
    try:
        anio_nacimiento = int(entry_anio.get())
        edad = 2025 - anio_nacimiento
        label_resultado.config(text=f"Tienes aproximadamente {edad} años.")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un año válido.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Edad")

# Etiqueta: Año de nacimiento
label_anio = tk.Label(ventana, text="Año de nacimiento:")
label_anio.grid(row=0, column=0, padx=10, pady=10)

# Caja de texto para ingresar el año
entry_anio = tk.Entry(ventana)
entry_anio.grid(row=0, column=1, padx=10, pady=10)

# Botón para calcular edad
boton_calcular = tk.Button(ventana, text="Calcular Edad", command=calcular_edad)
boton_calcular.grid(row=1, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=2, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
ventana.mainloop()
