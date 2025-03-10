import matplotlib.pyplot as plt
import numpy as np

# Definir los tamaños del eje X e Y
x = np.linspace(-10, 10, 400)
# Establecemos la función seno al eje Y
y = np.sin(x)

# Crear el gráfico
plt.figure(figsize = (10, 3))
# Creamos la gráfica del seno con color rojo y tamaño de línea 3
plt.plot(x, y, color = "red", linewidth = 3)
# Establecemos el título del gráfico
plt.title("Gráfica del seno")
# Establecemos el nombre del eje X
plt.xlabel("x")
# Establecemos el nombre del eje Y
plt.ylabel("sen(x)")
# Ocultamos la rejilla
plt.grid(False)
# Establecemos el color y grosor de la línea divisora del eje X
plt.axhline(0, color = "gray", lw = 1)
# Establecemos el color y grosor de la línea divisora del eje Y
plt.axvline(0, color = "gray", lw = 1)
# Mostramos el gráfico del seno
plt.show()