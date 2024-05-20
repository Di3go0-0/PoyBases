import sqlite3

def conectar():
    return sqlite3.connect("base_datos.db")

def crear_tabla_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cedula_nit TEXT NOT NULL,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT NOT NULL,
            direccion TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

def borrar_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DROP TABLE IF EXISTS Clientes')
    conexion.commit()
    conexion.close()

class Cliente:
    def __init__(self, cedula_nit, nombre, apellidos, telefono, correo, direccion):
        self.cedula_nit = cedula_nit
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

def guardar(Cliente):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO Clientes (cedula_nit, nombre, apellidos, telefono, correo, direccion)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (Cliente.cedula_nit, Cliente.nombre, Cliente.apellidos, Cliente.telefono, Cliente.correo, Cliente.direccion))
    conexion.commit()
    conexion.close()

def listar():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM Clientes')
    clientes = cursor.fetchall()
    conexion.close()
    return clientes

def editar(datos_actualizados, id):
    conexion = conectar()
    cursor = conexion.cursor()
    columnas = ', '.join(f"{col} = ?" for col in datos_actualizados.keys())
    valores = list(datos_actualizados.values())
    valores.append(id)
    
    query = f"UPDATE Clientes SET {columnas} WHERE id = ?"
    
    cursor.execute(query, valores)
    conexion.commit()
    conexion.close()

def eliminar(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM Clientes WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
