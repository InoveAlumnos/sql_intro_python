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

import os
import csv
import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()
    c.execute("""
                DROP TABLE IF EXISTS sensor;
            """)
    c.execute("""
            CREATE TABLE sensor(
                [id] INTEGER PRIMARY KEY,
                [pulso] INTEGER NOT NULL
            );
            """)

    conn.commit()
    conn.close()


if __name__ == '__main__':

    import numpy as np

    conn = sqlite3.connect('heart.db')
    c = conn.cursor()

    pulsos = c.execute("SELECT pulso FROM sensor").fetchall()

    pulsos = np.asanyarray(pulsos)
    print(pulsos.mean())
    print(pulsos.max())
    print(pulsos.min())
    print(pulsos.std())

    

    # print("Bienvenidos a otra clase de Inove con Python")
    # create_schema()
    

    # conn = sqlite3.connect('heart.db')
    # c = conn.cursor()

    # path = os.path.dirname(__file__)
    # sensor_path = os.path.join(path, 'sensor.csv')

    # with open(sensor_path) as fi:
    #     data = csv.DictReader(fi)

    #     for row in data:
    #         pulso = int(row['pulso'])
    #         if pulso <= 50:
    #             continue

    #         c.execute("INSERT INTO sensor (pulso) VALUES (?);", [pulso])

    # conn.commit()
    # conn.close()
