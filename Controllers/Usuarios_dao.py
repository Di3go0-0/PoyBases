from database.conexion_db import ConexionDB
from tkinter import messagebox

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def crear_tabla():
    conexion = ConexionDB('Usuarios')
    sql = '''
    CREATE TABLE IF NOT EXISTS Usuarios (
        Username VARCHAR(50) UNIQUE,
        Password VARCHAR(100)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        #messagebox.showinfo("Crear Registro", "Se creó la tabla en la base de datos.")
    except Exception as e:
        messagebox.showwarning("Crear Registro", f"Error al crear la tabla: {e}")
    finally:
        conexion.cerrar()

def guardar(usuario):
    conexion = ConexionDB('Usuarios')
    sql = f"INSERT INTO Usuarios (Username, Password) VALUES (?, ?)"
    try:
        conexion.cursor.execute(sql, (usuario.username, usuario.password))
        messagebox.showinfo("Registro", "Usuario registrado exitosamente")
    except Exception as e:
        messagebox.showerror("Guardar Registro", f"Error al guardar el usuario en la base de datos: {e}")
    finally:
        conexion.cerrar()

def verificar_credenciales(username, password):
    conexion = ConexionDB('Usuarios')
    sql = "SELECT * FROM Usuarios WHERE Username = ? AND Password = ?"
    try:
        conexion.cursor.execute(sql, (username, password))
        usuario = conexion.cursor.fetchone()
        return usuario is not None
    except Exception as e:
        messagebox.showerror("Error de Autenticación", f"Error al verificar las credenciales de inicio de sesión: {e}")
        return False
    finally:
        conexion.cerrar()

def agregar_usuario_default():
    if not verificar_existencia_usuario('diego'):
        usuario_default = Usuario('diego', '1234')
        guardar(usuario_default)



def verificar_existencia_usuario(username):
    conexion = ConexionDB('Usuarios')
    sql = "SELECT * FROM Usuarios WHERE Username = ?"
    try:
        conexion.cursor.execute(sql, (username,))
        usuario = conexion.cursor.fetchone()
        return usuario is not None
    except Exception as e:
        # messagebox.showerror("Error de Verificación", f"Error al verificar la existencia del usuario: {e}")
        return False
    finally:
        conexion.cerrar()


