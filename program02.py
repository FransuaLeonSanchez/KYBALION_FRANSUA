<<<<<<< HEAD
import sqlite3
from estudiantes import Estudiante

conn = sqlite3.connect('FIIS.db')
c= conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS estudiantes(
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    promedio REAL)""")

c.execute("INSERT INTO estudiantes VALUES ('20210019D','Fransua','Leon',14.6)")

est_1 =Estudiante('20210048F','Diego','Martin',12.7)
est_2 =Estudiante('20210154A','Ximena','Quispe',15.3)
est_3=Estudiante('20214468F','Ever','Burga',16.9)

def insertar_estudiantes(estudiante):
        c.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)",
          (estudiante.codigo, estudiante.nombre,estudiante.apellido,estudiante.promedio))

insertar_estudiantes(est_1)
insertar_estudiantes(est_2)
insertar_estudiantes(est_3)

def update_prom(codigo,promedio):
      c.execute("UPDATE estudiantes SET promedio=? WHERE codigo=?",
                (promedio,codigo))
      
update_prom('20210154A',12.1)

def delete_estudiante(codigo):
      c.execute("DELETE from estudiantes Where codigo=?",(codigo,))

delete_estudiante('20214468F')

conn.commit()

c.execute("SELECT * FROM estudiantes")
estudiantes=c.fetchall()
print(estudiantes)

def select_estudiante(codigo):
    c.execute("SELECT * FROM estudiantes WHERE codigo=?",(codigo,))
    alumno=c.fetchone()
    print(alumno)
select_estudiante('20210019D')



conn.close
=======
import sqlite3
from estudiantes import Estudiante

conn = sqlite3.connect('FIIS.db')
c= conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS estudiantes(
    codigo TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    promedio REAL)""")

c.execute("INSERT INTO estudiantes VALUES ('20210019D','Fransua','Leon',14.6)")

est_1 =Estudiante('20210048F','Diego','Martin',12.7)
est_2 =Estudiante('20210154A','Ximena','Quispe',15.3)
est_3=Estudiante('20214468F','Ever','Burga',16.9)

def insertar_estudiantes(estudiante):
        c.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)",
          (estudiante.codigo, estudiante.nombre,estudiante.apellido,estudiante.promedio))

insertar_estudiantes(est_1)
insertar_estudiantes(est_2)
insertar_estudiantes(est_3)

def update_prom(codigo,promedio):
      c.execute("UPDATE estudiantes SET promedio=? WHERE codigo=?",
                (promedio,codigo))
      
update_prom('20210154A',12.1)

def delete_estudiante(codigo):
      c.execute("DELETE from estudiantes Where codigo=?",(codigo,))

delete_estudiante('20214468F')

conn.commit()

c.execute("SELECT * FROM estudiantes")
estudiantes=c.fetchall()
print(estudiantes)

def select_estudiante(codigo):
    c.execute("SELECT * FROM estudiantes WHERE codigo=?",(codigo,))
    alumno=c.fetchone()
    print(alumno)
select_estudiante('20210019D')



conn.close
>>>>>>> ac4c52f02c68b6181324853e83d5c635df83a2ba
