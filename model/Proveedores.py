import tkinter as tk
from tkinter import ttk, messagebox
from .Proveedores_dao import crear_tabla_proveedores, borrar_tabla, Proveedor, guardar, listar, editar, eliminar

class ProveedoresFrame(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("Gestión de Proveedores")
        self.geometry("800x600")
        self.setup_ui()
        self.tabla_proveedores()
        self.deshabilitar_campos()

    def setup_ui(self):
        self.label_cedula_nit = tk.Label(self, text='Cedula o Nit:')
        self.label_cedula_nit.grid(row=0, column=0, padx=10, pady=10)
        self.entry_cedula_nit = tk.Entry(self)
        self.entry_cedula_nit.grid(row=0, column=1, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text='Nombres:')
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.label_apellidos = tk.Label(self, text='Apellidos:')
        self.label_apellidos.grid(row=2, column=0, padx=10, pady=10)
        self.entry_apellidos = tk.Entry(self)
        self.entry_apellidos.grid(row=2, column=1, padx=10, pady=10)

        self.label_telefono = tk.Label(self, text='Teléfono:')
        self.label_telefono.grid(row=3, column=0, padx=10, pady=10)
        self.entry_telefono = tk.Entry(self)
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=10)

        self.label_correo = tk.Label(self, text='Correo:')
        self.label_correo.grid(row=4, column=0, padx=10, pady=10)
        self.entry_correo = tk.Entry(self)
        self.entry_correo.grid(row=4, column=1, padx=10, pady=10)

        self.label_direccion = tk.Label(self, text='Dirección:')
        self.label_direccion.grid(row=5, column=0, padx=10, pady=10)
        self.entry_direccion = tk.Entry(self)
        self.entry_direccion.grid(row=5, column=1, padx=10, pady=10)

        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.grid(row=6, column=0, padx=10, pady=10)

        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.button_guardar.grid(row=6, column=1, padx=10, pady=10)

        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.button_cancelar.grid(row=6, column=2, padx=10, pady=10)

        self.tabla = ttk.Treeview(self, columns=('CedulaoNit', 'Nombre', 'Apellido', 'Telefono', 'Correo', 'Direccion'))
        self.tabla.grid(row=7, column=0, columnspan=4, sticky='nsew')
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=7, column=4, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='#')
        self.tabla.heading('#1', text='Cedula o Nit')
        self.tabla.heading('#2', text='Nombre')
        self.tabla.heading('#3', text='Apellido')
        self.tabla.heading('#4', text='Telefono')
        self.tabla.heading('#5', text='Correo')
        self.tabla.heading('#6', text='Direccion')

        self.button_editar = tk.Button(self, text='Editar', command=self.editar_datos)
        self.button_editar.grid(row=8, column=0, padx=10, pady=10)

        self.button_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.button_eliminar.grid(row=8, column=1, padx=10, pady=10)

    def habilitar_campos(self):
        self.entry_cedula_nit.config(state='normal')
        self.entry_nombre.config(state='normal')
        self.entry_apellidos.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_correo.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.button_guardar.config(state='normal')
        self.button_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.entry_cedula_nit.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.entry_apellidos.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_correo.config(state='disabled')
        self.entry_direccion.config(state='disabled')
        self.button_guardar.config(state='disabled')
        self.button_cancelar.config(state='disabled')

    def guardar_datos(self):
        proveedor = Proveedor(
            self.entry_cedula_nit.get(),
            self.entry_nombre.get(),
            self.entry_apellidos.get(),
            self.entry_telefono.get(),
            self.entry_correo.get(),
            self.entry_direccion.get(),
        )
        guardar(proveedor)
        self.tabla_proveedores()
        self.deshabilitar_campos()

    def tabla_proveedores(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        proveedores = listar()
        for p in proveedores:
            self.tabla.insert('', 'end', text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6]))

    def editar_datos(self):
        try:
            selected_item = self.tabla.selection()[0]
            values = self.tabla.item(selected_item, 'values')
            self.entry_cedula_nit.config(state='normal')
            self.entry_nombre.config(state='normal')
            self.entry_apellidos.config(state='normal')
            self.entry_telefono.config(state='normal')
            self.entry_correo.config(state='normal')
            self.entry_direccion.config(state='normal')

            self.entry_cedula_nit.delete(0, tk.END)
            self.entry_cedula_nit.insert(0, values[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, values[1])
            self.entry_apellidos.delete(0, tk.END)
            self.entry_apellidos.insert(0, values[2])
            self.entry_telefono.delete(0, tk.END)
            self.entry_telefono.insert(0, values[3])
            self.entry_correo.delete(0, tk.END)
            self.entry_correo.insert(0, values[4])
            self.entry_direccion.delete(0, tk.END)
            self.entry_direccion.insert(0, values[5])

            self.button_guardar.config(command=lambda: self.actualizar_datos(selected_item))
        except IndexError:
            messagebox.showerror("Error", "Seleccione un registro para editar")

    def actualizar_datos(self, item):
        proveedor = Proveedor(
            self.entry_cedula_nit.get(),
            self.entry_nombre.get(),
            self.entry_apellidos.get(),
            self.entry_telefono.get(),
            self.entry_correo.get(),
            self.entry_direccion.get(),
        )
        editar(proveedor, self.tabla.item(item, 'text'))
        self.tabla_proveedores()
        self.deshabilitar_campos()
        self.button_guardar.config(command=self.guardar_datos)

    def eliminar_datos(self):
        try:
            selected_item = self.tabla.selection()[0]
            eliminar(self.tabla.item(selected_item, 'text'))
            self.tabla_proveedores()
        except IndexError:
            messagebox.showerror("Error", "Seleccione un registro para eliminar")
