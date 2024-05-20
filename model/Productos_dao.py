import sqlite3

def conectar():
    return sqlite3.connect("base_datos.db")

def crear_tabla_productos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Productos (
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
    cursor.execute('DROP TABLE IF EXISTS Productos')
    conexion.commit()
    conexion.close()

class Producto:
    def __init__(self, Codigo, Nombre, Precio, Cantidad):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Precio = Precio
        self.Cantidad = Cantidad

def guardar(Producto):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO Productos (Codigo, Nombre, Precio, Cantidad)
        VALUES (?, ?, ?, ?)
    ''', (Producto.Codigo, Producto.Nombre, Producto.Precio, Producto.Cantidad))
    conexion.commit()
    conexion.close()

def listar():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM Productos')
    Producto = cursor.fetchall()
    conexion.close()
    return Producto

def editar(datos_actualizados, id):
    conexion = conectar()
    cursor = conexion.cursor()
    columnas = ', '.join(f"{col} = ?" for col in datos_actualizados.keys())
    valores = list(datos_actualizados.values())
    valores.append(id)
    
    query = f"UPDATE Productos SET {columnas} WHERE id = ?"
    
    cursor.execute(query, valores)
    conexion.commit()
    conexion.close()

def eliminar(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM Productos WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
