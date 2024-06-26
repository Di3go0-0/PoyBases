import tkinter as tk
from tkinter import ttk, messagebox
from Controllers.Proveedores_dao import crear_tabla_proveedores, borrar_tabla, Proveedor, guardar, listar, editar, eliminar

class ProveedoresFrame(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("Gestión de Proveedores")
        self.geometry("1420x600")
        self.setup_ui()
        self.tabla_proveedores()
        self.deshabilitar_campos()

    def setup_ui(self):
        self.label_cedula_nit = tk.Label(self, text='Cedula o Nit:')
        self.label_cedula_nit.config(font=('Arial', 12, 'bold'))
        self.label_cedula_nit.grid(row=0, column=0, padx=10, pady=10)
        self.mi_cedula_nit = tk.StringVar()
        self.entry_cedula_nit = tk.Entry(self, textvariable = self.mi_cedula_nit)
        self.entry_cedula_nit.config(width=50, font=('Arial', 12))
        self.entry_cedula_nit.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.label_nombre = tk.Label(self, text='Nombres:')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row = 1, column = 1, padx=10, pady=10, columnspan=2)

        self.label_apellidos = tk.Label(self, text='Apellidos:')
        self.label_apellidos.config(font=('Arial', 12, 'bold'))
        self.label_apellidos.grid(row=2, column=0, padx=10, pady=10)
        self.mi_apellidos = tk.StringVar()
        self.entry_apellidos = tk.Entry(self, textvariable = self.mi_apellidos)
        self.entry_apellidos.config(width=50, font=('Arial', 12))
        self.entry_apellidos.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        self.label_telefono = tk.Label(self, text='Teléfono:')
        self.label_telefono.config(font=('Arial', 12, 'bold'))
        self.label_telefono.grid(row=3, column=0, padx=10, pady=10)
        self.mi_telefono = tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable = self.mi_telefono)
        self.entry_telefono.config(width=50, font=('Arial', 12))
        self.entry_telefono.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

        self.label_correo = tk.Label(self, text='Correo:')
        self.label_correo.config(font=('Arial', 12, 'bold'))
        self.label_correo.grid(row=4, column=0, padx=10, pady=10)
        self.mi_correo = tk.StringVar()
        self.entry_correo = tk.Entry(self, textvariable = self.mi_correo)
        self.entry_correo.config(width=50, font=('Arial', 12))
        self.entry_correo.grid(row=4, column=1, padx=10, pady=10, columnspan=2)

        self.label_direccion = tk.Label(self, text='Dirección:')
        self.label_direccion.config(font=('Arial', 12, 'bold'))
        self.label_direccion.grid(row=5, column=0, padx=10, pady=10)
        self.mi_direccion = tk.StringVar()
        self.entry_direccion = tk.Entry(self, textvariable = self.mi_direccion)
        self.entry_direccion.config(width=50, font=('Arial', 12))
        self.entry_direccion.grid(row=5, column=1, padx=10, pady=10, columnspan=2)

        #botones

        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#4D857E', cursor='hand2', activebackground='#81D6CC')
        self.button_nuevo.grid(row=6, column=0, padx=10, pady=10)

        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.button_guardar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#6A9757', cursor='hand2', activebackground='#A0DA89')
        self.button_guardar.grid(row=6, column=1, padx=10, pady=10)

        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.button_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')        
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
        self.button_editar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#4D857E', cursor='hand2', activebackground='#81D6CC')
        self.button_editar.grid(row=8, column=0, padx=10, pady=10)

        self.button_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.button_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')
        self.button_eliminar.grid(row=8, column=1, padx=10, pady=10)

        self.button_salir = tk.Button(self, text='Salir', command=self.destroy)
        self.button_salir.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')
        self.button_salir.grid(row=8, column=2, padx=10, pady=10)

    def habilitar_campos(self):
        self.mi_cedula_nit.set('')
        self.mi_nombre.set('')
        self.mi_apellidos.set('')
        self.mi_telefono.set('')
        self.mi_correo.set('')
        self.mi_direccion.set('')

        self.entry_cedula_nit.config(state='normal')
        self.entry_nombre.config(state='normal')
        self.entry_apellidos.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_correo.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.button_guardar.config(state='normal')
        self.button_cancelar.config(state='normal')

    def deshabilitar_campos(self):
        self.mi_cedula_nit.set('')
        self.mi_nombre.set('')
        self.mi_apellidos.set('')
        self.mi_telefono.set('')
        self.mi_correo.set('')
        self.mi_direccion.set('')

        self.entry_cedula_nit.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.entry_apellidos.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_correo.config(state='disabled')
        self.entry_direccion.config(state='disabled')
        self.button_guardar.config(state='disabled')
        self.button_cancelar.config(state='disabled')

    def validar_datos(self):
        cedula_nit = self.mi_cedula_nit.get()
        nombre = self.mi_nombre.get()
        apellidos = self.mi_apellidos.get()
        telefono = self.mi_telefono.get()
        correo = self.mi_correo.get()
        direccion = self.mi_direccion.get()

        # Validar que la cédula sea un entero
        try:
            int(cedula_nit)
        except ValueError:
            messagebox.showerror("Error de Validación", "La cédula o NIT debe ser un número entero.")
            return False
        
        # Validar que el nombre sea una cadena de caracteres
        if not nombre.isalpha():
            messagebox.showerror("Error de Validación", "El nombre debe contener solo letras.")
            return False
        
        # Validar que el apellido sea una cadena de caracteres
        if not apellidos.isalpha():
            messagebox.showerror("Error de Validación", "Los apellidos deben contener solo letras.")
            return False
        
        # Validar que el teléfono sea un entero
        try:
            int(telefono)
        except ValueError:
            messagebox.showerror("Error de Validación", "El teléfono debe ser un número entero.")
            return False

        # Validar el formato del correo electrónico
        if not "@" in correo or not "." in correo:
            messagebox.showerror("Error de Validación", "El correo electrónico no tiene un formato válido.")
            return False

        # Validar que la dirección sea una cadena de strings
        if not isinstance(direccion, str):
            messagebox.showerror("Error de Validación", "La dirección debe ser una cadena de caracteres.")
            return False

        return True

    def guardar_datos(self):
        if not self.validar_datos():
            return

        proveedor = Proveedor(
            self.mi_cedula_nit.get(),
            self.mi_nombre.get(),
            self.mi_apellidos.get(),
            self.mi_telefono.get(),
            self.mi_correo.get(),
            self.mi_direccion.get(),
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
            
            # Guardar el id del proveedor
            self.selected_proveedor_id = self.tabla.item(selected_item, 'text')
            
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

            self.button_guardar.config(state='normal', command=lambda: self.actualizar_datos(selected_item, values))
            self.button_cancelar.config(state='normal')
        except IndexError:
            messagebox.showerror("Error", "Seleccione un registro para editar")

    def actualizar_datos(self, item, old_values):
        # Recolectar los nuevos valores ingresados por el usuario
        nuevos_valores = {
            'cedula_nit': self.entry_cedula_nit.get(),
            'nombre': self.entry_nombre.get(),
            'apellidos': self.entry_apellidos.get(),
            'telefono': self.entry_telefono.get(),
            'correo': self.entry_correo.get(),
            'direccion': self.entry_direccion.get()
        }
        
        # Solo actualizar los campos que han cambiado
        datos_actualizados = {}
        campos = ['cedula_nit', 'nombre', 'apellidos', 'telefono', 'correo', 'direccion']
        for i, campo in enumerate(campos):
            if nuevos_valores[campo] != old_values[i]:
                datos_actualizados[campo] = nuevos_valores[campo]
        
        if datos_actualizados:
            editar(datos_actualizados, self.selected_proveedor_id)
        
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
