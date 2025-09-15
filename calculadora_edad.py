import tkinter as tk

def calcular_edad():
    try:
        año_nacimiento = int(entry_año.get())
        edad = 2025 - año_nacimiento
        label_resultado.config(text=f"Tu edad aproximada es: {edad} años")
    except ValueError:
        label_resultado.config(text="Por favor ingresa un número válido")

ventana = tk.Tk()
ventana.title("Calculadora de Edad")

label_año = tk.Label(ventana, text="Año de nacimiento:")
label_año.grid(row=0, column=0, padx=10, pady=10)

entry_año = tk.Entry(ventana)
entry_año.grid(row=0, column=1, padx=10, pady=10)

boton_calcular = tk.Button(ventana, text="Calcular Edad", command=calcular_edad)
boton_calcular.grid(row=1, column=0, columnspan=2, pady=10)

label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=2, column=0, columnspan=2, pady=10)

ventana.mainloop()
