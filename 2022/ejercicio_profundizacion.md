# Ejercicios de profundización [Python]
EL propósito de este ejercicio es que el alumno ponga sus habilidades de SQL junto con otras adqueridas a lo largo del curso como ser dibujado de gráficos con matplotlib y análisis de datos con numpy. Este es un caso típico de análisis de datos

# Enunciado
El objetivo es análizar los datos del rítmo cardíaco que se tomaron de una persona real mirando un partido de futbol. Toda la información que necesita ya se encuentra almacenada en una base de datos la cual deberá leer para luego analizar.

Deberá leer de la base de datos "heart.db" la tabla "sensor". Dicha tabla "sensor" solo tiene dos columnas:
- id --> número (autoincremental, lo define y completa SQL)
- pulso --> número (registro del pulso cardíaco de la persona en ese momento)

El objetivo es leer los valores de la columna "pulso" de toda la base de datos.

## fetch()
Deben crear una función "fetch" que lea el valor de la columna "pulso" de todas las filas de la tabla "sensor" de la base de datos "heart.db".\
Deben usar la sentencia SELECT indicando que desean leer solamente la columna pulso, y leer todo junto utilizando "fetchall".\
Al finalizar la función rebe retornar la lista de todos los pulsos cardícos obtenidos de la tabla.

# Análisis de datos
Una vez que tengan en sus manos la información de las pulsaciones de todo el partido de futbol en una lista, deben armar las siguientes funciones que serán las que realizarán el análisis de los datos.

## show(data)
Deben crear una función "show" que reciba como parámetro la lista de datos recolectada en el punto anterior. Con esa lista de datos deben graficar utilizando matplotlib o seaborn todos los pulsos en un gráfico de línea "plot". El objetivo de esta función es que puedan visualizar la evolución del rítmo cardíaco.

## estadistica(data)
Deben crear la función "estadistica" para obtener algunos valores estadísticos de los datos e imprimirlos en pantalla. Para eso deberán utilizar numpy y obtener los siguientes valores:
- Calcular e imprimir el valor medio (mean) con numpy
- Calcular e imprimir el valor mínhimo (min) con numpy
- Calcular e imprimir el valor máximo (max) con numpy
- Calcular e imprimir el desvio estandar (std) con numpy

## regiones(data)
Deben crear la función "regiones" para graficar en matplotlib las zonas donde la persona estuvo tranquila mirando el partido, donde estuvo aburrida y donde estuvo muy enganchada y entusiasmada. Para ello se utilizará numpy para calcular el valor medio y el desvio estandar como se hizo en el punto anterior y deberá realizar el siguiente proceso:
- Calcular el valor medio (mean) y el desvio estandar (std) con numpy

Debe crear 3 pares de listas de datos a partir de data:
- En una lista x1 e y1 para almacenar todos los valores menores o iguales al valor medio menos el desvio (pulso <= mean-std) y su índice correspondiente
- En una lista x2 e y2 para almacenar todos los valores mayores o iguales al valor medio más el desvio (pulso >= mean+std) y su índice correspondiente
- En una lista x3 e y3 para almacenar todos aquelas valores que no haya guardado en niguna de las dos listas anteriores y su índice correspondiente

Una vez obtenidos las listas mencionadas, debe dibujar tres scatter plot en un solo gráfico. Cada uno de los tres scatter plot representa cada una de las listas mencionadas que debe dibujar con un color diferente.

NOTA: Les dejamos el ejemplo de como tendrían que armar una de las tres pares de listas, deben modificar el código siguiente para poder agregar las otras dos pares listas mencionadas (x2 y2 e x3 y3).
IMPORTANTE: Recuerdo calcular "mean" y "std" antes con numpy.

```
x1 = []
y1 = []
for i in range(len(data)):
    if data[i] <= (mean-std):
        x1.append(i)
        y1.append(data[i])
```

# Esquema del ejercicio
Deben crear su archivo de python y crear las funciones mencionadas en este documento. Deben crear la sección "if _name_ == "_main_" y ahí crear el flujo de prueba de este programa:
```
if __name__ == "__main__":
  # Leer la DB
  data = fetch()

  # Data analytics
  show(data)
  estadistica(data)
  regiones(data)
```
