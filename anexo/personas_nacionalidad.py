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
    conn = sqlite3.connect('personas_nacionalidad.db')
    c = conn.cursor()
    c.execute("""
                DROP TABLE IF EXISTS persona;
            """)
    c.execute("""
                DROP TABLE IF EXISTS nacionalidad;
            """)
    c.execute("""
            CREATE TABLE nacionalidad(
                [id] INTEGER PRIMARY KEY,
                [name] STRING NOT NULL
            );
            """)
    conn.commit()
    c.execute("""
            CREATE TABLE persona(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] STRING NOT NULL,
                [age] INTEGER NOT NULL,
                [nationality] INTEGER NOT NULL REFERENCES nacionalidad(id)
            );
            """)
    conn.commit()


def insert_nacionalidad(nat_id, name):
    conn = sqlite3.connect('personas_nacionalidad.db')
    c = conn.cursor()

    values = (nat_id, name)

    c.execute("""
        INSERT INTO nacionalidad (id, name)
        VALUES (?,?);""", values)

    conn.commit()


def insert_persona(name, age, nationality):
    conn = sqlite3.connect('personas_nacionalidad.db')
    c = conn.cursor()

    values = (name, age, nationality)

    c.execute("""
        INSERT INTO persona (name, age, nationality)
        VALUES (?,?,?);""", values)

    conn.commit()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()
    insert_nacionalidad(1, 'Argentina')
    insert_nacionalidad(2, 'Holanda')
    insert_nacionalidad(3, 'Estados Unidos')
    insert_persona('Inove', 12, 1)
    insert_persona('Python', 29, 2)
    insert_persona('Max', 35, 3)
    insert_persona('Mirta', 93, 1)
