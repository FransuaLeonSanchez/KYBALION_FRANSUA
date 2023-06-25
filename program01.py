"""
Este programa demuestra la correcta aplicación de python venv, isort, black y pylint
Recomendaciones:
-Iniciar el entorno virtual con el comando "venv\Scripts\activate"
-Para ejecutar pylint, escribir "pylint program01.py", el codigo actual cuenta con un una califiacion 10/10
-El programa ya paso por isort y black, por lo que no es necesario ejecutarlos nuevamente
"""

import math
import matplotlib.pyplot as plt
import numpy as np


def calcular_seno(angulo):
    """"
    Función para calcular el seno de un ángulo en grados
    """
    angulo_radianes = math.radians(angulo)
    seno = math.sin(angulo_radianes)
    return seno


# Crear un array de valores de x en el rango de 0 a 2π
x = np.linspace(0, 2 * np.pi, 100)

# Calcular el seno de cada valor de x
y = np.sin(x)

# Graficar la función seno
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Gráfico de la función seno")
plt.grid(True)
plt.show()
