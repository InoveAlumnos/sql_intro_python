#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():
    '''
    Función para crear la base de datos y las tablas
    '''
    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('personas.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS persona;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE persona(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER,
                [nationality] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def insert_persona(name, age, nationality=""):
    '''
    Función para insertar a una nueva persona
    '''
    # Conectarse a la base de datos
    conn = sqlite3.connect('personas.db')
    c = conn.cursor()

    values = [name, age, nationality]

    # Insertar la persona con los valores
    # de values
    c.execute("""
        INSERT INTO persona (name, age, nationality)
        VALUES (?,?,?);""", values)

    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()


def insert_grupo(group):
    '''
    Función para insertar a un grupo persona
    '''
    # Conectarse a la base de datos
    conn = sqlite3.connect('personas.db')
    c = conn.cursor()

    c.executemany("""
        INSERT INTO persona (name, age, nationality)
        VALUES (?,?,?);""", group)

    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()


def show():
    '''
    Función para mostrar el contenido de toda
    la base de datos
    '''
    # Conectarse a la base de datos
    conn = sqlite3.connect('personas.db')
    c = conn.cursor()

    # Leer todas las filas y obtener todos los datos juntos
    c.execute('SELECT * FROM persona')
    data = c.fetchall()
    print(data)

    # Leer todas las filas y obtener los datos de a uno
    c.execute('SELECT * FROM persona')
    print('Recorrer los datos desde el cursor')
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)

    print('Recorrer los datos directamente de la query')
    for row in c.execute('SELECT * FROM persona'):
        print(row)

    # Cerrar la conexión con la base de datos
    conn.close()


def get_all():
    '''
    Función obtener todas personas de la base de datos
    '''
    # Conectarse a la base de datos
    conn = sqlite3.connect('personas.db')
    c = conn.cursor()

    c.execute("SELECT * FROM persona;")
    
    # Luego de ejecutar la query pedimos los datos
    # de todas las personas encontradas
    personas = c.fetchall()

    # Save
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

    return personas


def get_persona(name):
    '''
    Función obtener una persona de la base de datos
    por su nombre
    '''
    # Conectarse a la base de datos
    conn = sqlite3.connect('personas.db')
    c = conn.cursor()

    values = [name]
    c.execute("SELECT * FROM persona WHERE name =?",
                         values)
    
    # Luego de ejecutar la query pedimos los datos
    # de la persona
    # Si la persona no existe, fetchone returna None
    persona = c.fetchone()

    # Save
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

    return persona


def update_persona_age(name, age):
    '''
    Función para actualizar la edad de una persona
    '''
    # Conectarse a la base de datos
    conn = sqlite3.connect('personas.db')
    c = conn.cursor()

    values = [age, name]
    rowcount = c.execute("UPDATE persona SET age =? WHERE name =?",
                         values).rowcount

    print('Filas actualizadas:', rowcount)

    # Save
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()


def delete_persona(name):
    '''
    Función para eliminar una persona por su nombre
    '''
    # Conectarse a la base de datos
    conn = sqlite3.connect('personas.db')
    c = conn.cursor()

    # Borrar la fila cuyo nombre coincida con la búsqueda
    # NOTA: Recordar que las tupla un solo elemento se definen como
    # (elemento,)
    # Si presta a confusión usar una lista --> [elemento]
    rowcount = c.execute("DELETE FROM persona WHERE name =?", (name,)).rowcount

    print('Filas actualizadas:', rowcount)

    # Save
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()
    insert_persona('Inove', 12, 'Argentina')
    insert_persona('Python', 29, 'Holanda')
    insert_persona('Max', 35, 'Estados Unidos')
    insert_persona('Mirta', 93, 'Argentina')

    show()

    personas = get_all()
    print("Personas en la base de datos:")
    print(personas)

    mirta = get_persona('Mirta')
    print("Mira:", mirta)

    update_persona_age('Max', 52)
    delete_persona('Max')

    show()

    group = [('Max', 40, 'Estados Unidos'),
             ('SQL', 13, 'Inglaterra'),
             ('SQLite', 20, 'Estados Unidos'),
             ]

    insert_grupo(group)

    # Prestar atención que ahora se agrega nuevamente Max
    # pero con un nuevo id (id=5), y el ex id de Max (id=3)
    # quedó perdido y ya nadie lo use, este comportamiento es normal.
    show()
