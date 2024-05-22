import sqlite3
from tkinter import messagebox
def conectar():
    return sqlite3.connect("database/DataBase.DB")

def crear_tabla_construccion():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS construccion (
            producto_id INTEGER,
            insumo_id INTEGER,
            PRIMARY KEY (producto_id, insumo_id),
            FOREIGN KEY (producto_id) REFERENCES Productos(id),
            FOREIGN KEY (insumo_id) REFERENCES Insumos(id)
        )
    ''')
    conexion.commit()
    conexion.close()

def borrar_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DROP TABLE IF EXISTS construccion')
    conexion.commit()
    conexion.close()

class Construccion:
    def __init__(self, producto_id, insumo_id):
        self.producto_id = producto_id
        self.insumo_id = insumo_id

def id_existe(tabla, id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(f'SELECT COUNT(*) FROM {tabla} WHERE id = ?', (id,))
    count = cursor.fetchone()[0]
    conexion.close()
    return count > 0

def guardar(Construccion):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        if not id_existe('Productos', Construccion.producto_id):
            messagebox.showerror("Error", "El ID del producto no existe.")
            return
        if not id_existe('Insumos', Construccion.insumo_id):
            messagebox.showerror("Error", "El ID del insumo no existe.")
            return
        cursor.execute('''
            INSERT INTO construccion (producto_id, insumo_id)
            VALUES (?, ?)
        ''', (Construccion.producto_id, Construccion.insumo_id))
        conexion.commit()
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "El registro ya existe en la base de datos.")
    finally:
        conexion.close()

def registro_existe(producto_id, insumo_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT COUNT(*) FROM construccion WHERE producto_id = ? AND insumo_id = ?', (producto_id, insumo_id,))
    count = cursor.fetchone()[0]
    conexion.close()
    return count > 0


def listar():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM construccion')
    construccion = cursor.fetchall()
    conexion.close()
    return construccion

def eliminar(producto_id, insumo_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM construccion WHERE producto_id = ? AND insumo_id = ?', (producto_id, insumo_id,))
    conexion.commit()
    conexion.close()

def editar(datos_actualizados, producto_id, insumo_id):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Primero, eliminamos el registro existente
    cursor.execute('DELETE FROM construccion WHERE producto_id = ? AND insumo_id = ?', (producto_id, insumo_id,))
    
    # Luego, insertamos un nuevo registro con los valores actualizados
    cursor.execute('''
        INSERT INTO construccion (producto_id, insumo_id)
        VALUES (?, ?)
    ''', (datos_actualizados['producto_id'], datos_actualizados['insumo_id']))
    
    conexion.commit()
    conexion.close()