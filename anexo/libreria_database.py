###################################################

# ESTE SCRIPT SE CREO PARA GENEARAR LA BASE DE DATOS
# DE "libreria.db" PARA SU USO EN LOS EJERCICIOS

###################################################


import sqlite3

conn = sqlite3.connect('libreria.db')
c = conn.cursor()
c.execute("""
            DROP TABLE IF EXISTS libro;
        """)
c.execute("""
            CREATE TABLE libro(
            id               INTEGER  NOT NULL PRIMARY KEY,
            titulo           TEXT NOT NULL,
            cantidad_paginas INTEGER  NOT NULL,
            autor            TEST NOT NULL
            );
        """)

conn.commit()


c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor) VALUES (1,'Cien anios de soledad',471,'Gabriel Garcia Marquez');")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor) VALUES (2,'El Aleph',146,'Jorge Luis Borges');")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor) VALUES (3,'El libro de Arena',181,'Jorge Luis Borges');")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor) VALUES (4,'Las intermitencias de la muerte',214,'Jose Saramago');")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor) VALUES (5,'Relato de un naufrago',141,'Gabriel Garcia Marquez');")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor) VALUES (6,'El amor en los tiempos del colera',464,'Gabriel Garcia Marquez');")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor) VALUES (7,'La caverna',454,'Jose Saramago');")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor) VALUES (8,'El tunel',184,'Ernesto Sabato');")
c.execute("INSERT INTO libro(id,titulo,cantidad_paginas,autor) VALUES (9,'Boquitas pintadas',218,'Manuel Puig');")

conn.commit()
conn.close()