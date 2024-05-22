# Aquí importas las clases y funciones necesarias
import tkinter as tk
from tkinter import messagebox
from Controllers.Usuarios_dao import guardar, Usuario, verificar_credenciales, crear_tabla, agregar_usuario_default
from Views.Login import LoginFrame
from Controllers.Proveedores_dao import crear_tabla_proveedores
from Controllers.Productos_dao import crear_tabla_productos
from Controllers.Clientes_dao import crear_tabla_clientes
from Controllers.Insumos_dao import crear_tabla_insumos
from Controllers.Construccion_dao import crear_tabla_construccion


# Crear las tablas si no existe
crear_tabla()
crear_tabla_productos()
crear_tabla_proveedores()
crear_tabla_clientes()
crear_tabla_insumos()
crear_tabla_construccion()
agregar_usuario_default()

# Creas la ventana de inicio de sesión
#root = tk.Tk()
#root.title("Instand Power")
#root.geometry("300x180")

# Inicias la aplicación con la ventana de inicio de sesión
app = LoginFrame()
app.mainloop()
