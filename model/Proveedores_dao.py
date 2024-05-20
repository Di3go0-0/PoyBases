import sqlite3

def conectar():
    return sqlite3.connect("base_datos.db")

def crear_tabla_proveedores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Proveedores (
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
    cursor.execute('DROP TABLE IF EXISTS Proveedores')
    conexion.commit()
    conexion.close()

class Proveedor:
    def __init__(self, cedula_nit, nombre, apellidos, telefono, correo, direccion):
        self.cedula_nit = cedula_nit
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

def guardar(proveedor):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO Proveedores (cedula_nit, nombre, apellidos, telefono, correo, direccion)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (proveedor.cedula_nit, proveedor.nombre, proveedor.apellidos, proveedor.telefono, proveedor.correo, proveedor.direccion))
    conexion.commit()
    conexion.close()

def listar():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM Proveedores')
    proveedores = cursor.fetchall()
    conexion.close()
    return proveedores

def editar(datos_actualizados, id):
    conexion = conectar()
    cursor = conexion.cursor()
    columnas = ', '.join(f"{col} = ?" for col in datos_actualizados.keys())
    valores = list(datos_actualizados.values())
    valores.append(id)
    
    query = f"UPDATE Proveedores SET {columnas} WHERE id = ?"
    
    cursor.execute(query, valores)
    conexion.commit()
    conexion.close()

def eliminar(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM Proveedores WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
