# Aquí importas las clases y funciones necesarias
import tkinter as tk
from tkinter import messagebox
from model.Usuarios_dao import guardar, Usuario, verificar_credenciales, crear_tabla
from model.Login import LoginFrame
from model.Proveedores_dao import crear_tabla_proveedores
from model.Productos_dao import crear_tabla_productos
from model.Clientes_dao import crear_tabla_clientes
from model.Insumos_dao import crear_tabla_insumos

# Crear las tablas si no existe
crear_tabla()
crear_tabla_productos()
crear_tabla_proveedores()
crear_tabla_clientes()
crear_tabla_insumos()

# Creas la ventana de inicio de sesión
#root = tk.Tk()
#root.title("Instand Power")
#root.geometry("300x180")

# Inicias la aplicación con la ventana de inicio de sesión
app = LoginFrame()
app.mainloop()
