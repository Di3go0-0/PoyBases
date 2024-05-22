import tkinter as tk
from .Proveedores import ProveedoresFrame
from .Productos import ProductosFrame
from .clientes import ClientesFrame
from .Insumos import InsumosFrame
from .Usuarios import RegistroWindow
from .Construccion import ConstruccionFrame

class FrameMenuPrincipal(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.campos_menu_principal()

    def campos_menu_principal(self):
        self.boton_Proveedores = tk.Button(self, text="Proveedores", command=self.Proveedores)
        self.boton_Proveedores.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#4D857E', cursor='hand2', activebackground='#81D6CC')
        self.boton_Proveedores.grid(row=0, column=0, padx=10, pady=10)

        self.boton_Insumos = tk.Button(self, text="Insumos", command=self.Insumos)
        self.boton_Insumos.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#6A9757', cursor='hand2', activebackground='#A0DA89')
        self.boton_Insumos.grid(row=0, column=1, padx=10, pady=10)

        self.boton_Productos = tk.Button(self, text="Productos", command=self.Productos)
        self.boton_Productos.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')
        self.boton_Productos.grid(row=0, column=2, padx=10, pady=10)

        self.boton_Clientes = tk.Button(self, text="Construccion", command=self.Construccion)
        self.boton_Clientes.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#E1ED2E', cursor='hand2', activebackground='#F6FF74')
        self.boton_Clientes.grid(row=0, column=3, padx=10, pady=10)

        self.button_salir = tk.Button(self, text='Salir', command=self.root.quit)
        self.button_salir.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')
        self.button_salir.grid(row=8, column=2, padx=10, pady=10)

        self.button_register = tk.Button(self, text="Registrarse", command=self.registro)
        self.button_register.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#4D857E', cursor='hand2', activebackground='#81D6CC')
        self.button_register.grid(row=8, column=1, padx=10, pady=10)

    def Proveedores(self):
        proveedores_window = ProveedoresFrame(self.root)  # Crea una instancia de la ventana de proveedores
        proveedores_window.grab_set()
    
    def Productos(self):
        productos_window = ProductosFrame(self.root)  # Crea una instancia de la ventana de productos
        productos_window.grab_set()

    def Insumos(self):
        productos_window = InsumosFrame(self.root)  # Crea una instancia de la ventana de clientes
        productos_window.grab_set()

    def Construccion(self):
        productos_window = ConstruccionFrame(self.root)  # Crea una instancia de la ventana de clientes
        productos_window.grab_set()

    def registro(self):
        registro_window = RegistroWindow(self.root)  # Crea una instancia de la ventana de registro
        registro_window.grab_set()
