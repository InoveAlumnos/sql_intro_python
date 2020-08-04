# Ejercicios de práctica [Python]
EL propósito de este ejercicio es que el alumno ponga sus habilidades de SQL junto con otras adqueridas a lo largo de la carrera como el manejo de archivos CSV. Este es un caso típico de ETL en donde se transforma un sistema legacy de datos (un archivo) en una base de datos.

# Enunciado
El objetivo es realizar un ejercicio muy similar al de "ejercicios_clase" pero ahora el alumno será quien genere el esquema de la base de datos para construirla.\

Deberá generar una base de datos de libros basada en el archivo CSV libreria.csv, el cual posee las siguientes columnas:
- id del libro (id) --> número (autoincremental, lo define y completa SQL por ustedes)
- Título del libro (title) --> texto
- Cantidad de páginas (pags) --> número
- Nombre del autor (author) --> texto

## create_schema
Deben crear una función "create_schema" la cual se encargará de crear la base de datos y la tabla correspondiente al esquema definido. Deben usar la sentencia CREATE para crear la tabla mencionada.\
IMPORTANTE: Recuerden que es recomendable borrar la tabla (DROP) antes de crearla si es que existe para que no haya problemas al ejecutar la query.

## fill()
Deben crear una función "fill" que lea los datos del archivo CSV y cargue esas filas del archivo como filas de la tabla SQL. Pueden resolverlo de la forma que mejor crean. Deben usar la sentencia INSERT para insertar los datos.\
Si esta parte les toma demasiado tiempo o se les complica carguen los datos en la base de datos a mano, es preferible que tengan datos en la DB para que puedan avanzar.

## fetch(id)
Deben crear una función que imprima en pantalla filas de su base de datos, pueden usar esta función para ver que "fill" realizó exactamente lo que era esperado. Deben usar la sentencia SELECT para llegar al objetivo junto con WHERE para leer la fila deseada (si se desea leer una en particular).\
Esta función recibe como parámetro un id:
- En caso de que el id sea igual a cero (id=0) deben imprimir todas las filas de la base de datos.
- En caso de que id sea mayor a cero (id>0) deben imprimir sola la fila correspondiente a ese id.
IMPORTANTE: Es posible que pasen como id un número no definido en la tabla y el sistema de fetchone les devuelva None, lo cual es correcto, pero el sistema no debe explotar porque haya retornado None. En ese caso pueden imprimir en pantalla que no existe esa fila en la base de datos (más adelante en una API responderá Error 404).

## search_author(book_title)
Deben crear una función que retorne el nombre del autor que pertenece al título del libro pasado como parámetro a esta función. Deben usar la función SELECT junto con WHERE para buscar el autor correspondiente al libro.\
Al finalizar la función rebe retornar el autor:
```
    return author
```

## Esquema del ejercicio
Deben crear su archivo de python y crear las funciones mencionadas en este documento. Deben crear la sección "if _name_ == "_main_" y ahí crear el flujo de prueba de este programa:
```
if __name__ == "__main__":
  # Crear DB
  create_schema()

  # Completar la DB con el CSV
  fill()

  # Leer filas
  fetch()  # Ver todo el contenido de la DB
  fetch(3)  # Ver la fila 3
  fetch(20)  # Ver la fila 20

  # Buscar autor
  print(search_author('Relato de un naufrago'))

```

## Para jugar
Cuando finalicen el ejercicio pueden realizar las siguientes modificaciones:
- Modificar el nombre de un nombre o creando una función que utilice la sentencia UPDATE y que modifque el título de un libro según el "id" del libro deseado.
- Puedo generar una función que utilice la sentencia DELETE para borrar libros que ya no se venden en la librería por nombre del libro (título).

