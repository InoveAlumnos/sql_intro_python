


import sqlite3
import matplotlib.pyplot as plt
import numpy as np


def fetch():
    print("Lectura del valor de la columna pulso de todas las filas de la tabla sensor de la base de datos heart.db ")
    # Conectarse a la base de datos
    conn = sqlite3.connect("heart.db")
    c = conn.cursor()
    # Deben usar la sentencia SELECT indicando que desean leer solamente la columna pulso,
    # y leer todo junto utilizando "fetchall"
    c.execute("SELECT pulso FROM sensor")
    data = c.fetchall()
    # Cerrar la conexión con la base de datos
    conn.close()
    return data


def show(data):
    x = list(range(0,len(data)))
    y = data
    # Con esa lista de datos deben graficar utilizando matplotlib todos los pulsos en un gráfico de línea "plot"   
    fig = plt.figure()
    fig.suptitle("Ritmo cardiaco", fontsize=16)
    ax = fig.add_subplot()
    ax.plot(x, y, c='red', marker=' ', label="Pulsaciones")
    ax.set_facecolor('whitesmoke')
    ax.legend()
    ax.grid()
    ax.set_xlabel("Tiempo")
    plt.show()


def estadistica(data):
    # Calcular e imprimir el valor medio (mean) con numpy
    prom_pulse = np.mean(data)
    print("Promedio:", prom_pulse)
    # Calcular e imprimir el valor mínhimo (min) con numpy
    min_pulse = np.amin(data)
    print("Minima pulsacion:", min_pulse)
    # Calcular e imprimir el valor máximo (max) con numpy
    max_pulse = np.amax(data)
    print("Maxima pulsacion:", max_pulse)
    # Calcular e imprimir el desvio estandar (std) con numpy
    std_pulse = np.std(data)
    print("Desviacion estandar de las pulsaciones:", std_pulse)

    return prom_pulse, min_pulse, min_pulse, std_pulse


def regiones(data, prom_pulse, std_pulse): 
    # En una lista x1 e y1 para almacenar todos los valores menores o iguales 
    # al valor medio menos el desvio (pulso <= mean-std) y su índice correspondiente
    x1 = []
    y1 = []
    for i in range(len(data)):
        if data[i] <= (prom_pulse-std_pulse):
            x1.append(i)
            y1.append(data[i])

    # En una lista x2 e y2 para almacenar todos los valores mayores o iguales 
    # al valor medio más el desvio (pulso >= mean+std) y su índice correspondiente
    x2 = []
    y2 = []
    for i in range(len(data)):
        if data[i] >= (prom_pulse+std_pulse):
            x2.append(i)
            y2.append(data[i])
    
    # En una lista x3 e y3 para almacenar todos aquellos valores que no haya guardado en
    # ninguna de las dos listas anteriores y su índice correspondiente
    x3 = []
    y3 = []
    for i in range(len(data)):
        if data[i] not in y1 and data[i] not in y2:
            x3.append(i)
            y3.append(data[i])

    # dibujar tres scatter plot en un solo gráfico. Cada uno de los tres scatter plot
    # representa cada una de las listas mencionadas que debe dibujar con un color diferente.
    fig = plt.figure()
    fig.suptitle('Distribucion de pulsaciones', fontsize=16)
    ax = fig.add_subplot()

    ax.scatter(x1, y1, c='darkgreen', label="pulso <= mean+std")
    ax.scatter(x2, y2, c='darkred', label="pulso >= mean+std")
    ax.scatter(x3, y3, c='darkblue', label="otros pulsos")

    ax.legend()
    ax.grid()
    plt.show()


if __name__ == '__main__':

    # Leer la DB
    data = fetch()
    # Data analytics
    show(data)

    prom_pulse, min_pulse, min_pulse, std_pulse = estadistica(data)

    regiones(data, prom_pulse, std_pulse)