import sqlite3

def conectar():
    return sqlite3.connect("base_datos.db")

def crear_tabla_insumos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Insumos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Codigo INTEGER,
            Nombre TEXT NOT NULL,
            Precio INTEGER,
            Cantidad TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

def borrar_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DROP TABLE IF EXISTS Insumos')
    conexion.commit()
    conexion.close()

class Insumo:
    def __init__(self, Codigo, Nombre, Precio, Cantidad):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Precio = Precio
        self.Cantidad = Cantidad

def guardar(Insumo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO Insumos (Codigo, Nombre, Precio, Cantidad)
        VALUES (?, ?, ?, ?)
    ''', (Insumo.Codigo, Insumo.Nombre, Insumo.Precio, Insumo.Cantidad))
    conexion.commit()
    conexion.close()

def listar():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM Insumos')
    Insumo = cursor.fetchall()
    conexion.close()
    return Insumo

def editar(Insumo, id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        UPDATE Insumos SET Codigo = ?, Nombre = ?, Precio = ?, Cantidad = ?,
        WHERE id = ?
    ''', (Insumo.Codigo, Insumo.nombre, Insumo.Precio, Insumo.Cantidad, id))
    conexion.commit()
    conexion.close()

def eliminar(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM Insumos WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
