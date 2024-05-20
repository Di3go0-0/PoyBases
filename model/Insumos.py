import tkinter as tk
from tkinter import ttk, messagebox
from .Insumos_dao import crear_tabla_insumos, borrar_tabla, Insumo, guardar, listar, editar, eliminar

class InsumosFrame(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("Gestión de Insumos")
        self.geometry("1020x600")
        self.setup_ui()
        self.tabla_insumos()
        self.deshabilitar_campos()
        self.selected_insumo_id = None

    def setup_ui(self):
        self.label_codigo = tk.Label(self, text='Codigo:')
        self.label_codigo.config(font=('Arial', 12, 'bold'))
        self.label_codigo.grid(row=0, column=0, padx=10, pady=10)
        self.mi_codigo = tk.StringVar()
        self.entry_codigo = tk.Entry(self, textvariable = self.mi_codigo)
        self.entry_codigo.config(width=50, font=('Arial', 12))
        self.entry_codigo.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.label_nombre = tk.Label(self, text='Nombre:')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row = 1, column = 1, padx=10, pady=10, columnspan=2)

        self.label_precio = tk.Label(self, text='Precio:')
        self.label_precio.config(font=('Arial', 12, 'bold'))
        self.label_precio.grid(row=2, column=0, padx=10, pady=10)
        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable = self.mi_precio)
        self.entry_precio.config(width=50, font=('Arial', 12))
        self.entry_precio.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        self.label_cantidad = tk.Label(self, text='Cantidad:')
        self.label_cantidad.config(font=('Arial', 12, 'bold'))
        self.label_cantidad.grid(row=3, column=0, padx=10, pady=10)
        self.mi_cantidad = tk.StringVar()
        self.entry_cantidad = tk.Entry(self, textvariable = self.mi_cantidad)
        self.entry_cantidad.config(width=50, font=('Arial', 12))
        self.entry_cantidad.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#4D857E', cursor='hand2', activebackground='#81D6CC')
        self.button_nuevo.grid(row=4, column=0, padx=10, pady=10)

        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.button_guardar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#6A9757', cursor='hand2', activebackground='#A0DA89')
        self.button_guardar.grid(row=4, column=1, padx=10, pady=10)

        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
        self.button_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')        
        self.button_cancelar.grid(row=4, column=2, padx=10, pady=10)

        self.tabla = ttk.Treeview(self, columns=('Codigo', 'Nombre', 'Precio', 'Cantidad'))
        self.tabla.grid(row=5, column=0, columnspan=4, sticky='nsew')
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=5, column=4, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='#')
        self.tabla.heading('#1', text='Codigo')
        self.tabla.heading('#2', text='Nombre')
        self.tabla.heading('#3', text='Precio')
        self.tabla.heading('#4', text='Cantidad')

        self.button_editar = tk.Button(self, text='Editar', command=self.editar_datos)
        self.button_editar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#4D857E', cursor='hand2', activebackground='#81D6CC')
        self.button_editar.grid(row=6, column=0, padx=10, pady=10)

        self.button_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.button_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg = 'white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')
        self.button_eliminar.grid(row=6, column=1, padx=10, pady=10)

        self.button_salir = tk.Button(self, text='Salir', command=self.destroy)
        self.button_salir.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')
        self.button_salir.grid(row=6, column=2, padx=10, pady=10)

    def habilitar_campos(self):

        self.mi_codigo.set('')
        self.mi_nombre.set('')
        self.mi_precio.set('')
        self.mi_cantidad.set('')

        self.entry_codigo.config(state='normal')
        self.entry_nombre.config(state='normal')
        self.entry_precio.config(state='normal')
        self.entry_cantidad.config(state='normal')
        self.button_guardar.config(state='normal')
        self.button_cancelar.config(state='normal')

    def deshabilitar_campos(self):

        self.mi_codigo.set('')
        self.mi_nombre.set('')
        self.mi_precio.set('')
        self.mi_cantidad.set('')

        self.entry_codigo.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.entry_precio.config(state='disabled')
        self.entry_cantidad.config(state='disabled')
        self.button_guardar.config(state='disabled')
        self.button_cancelar.config(state='disabled')

    def guardar_datos(self):
        insumo = Insumo(
            self.entry_codigo.get(),
            self.entry_nombre.get(),
            self.entry_precio.get(),
            self.entry_cantidad.get(),
        )
        guardar(insumo)
        self.tabla_insumos()
        self.deshabilitar_campos()

    def tabla_insumos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        Insumos = listar()
        for p in Insumos:
            self.tabla.insert('', 'end', text=p[0], values=(p[1], p[2], p[3], p[4]))

    def editar_datos(self):
        try:
            selected_item = self.tabla.selection()[0]
            values = self.tabla.item(selected_item, 'values')
            
            # Guardar el id del cliente
            self.selected_insumo_id = self.tabla.item(selected_item, 'text')
            
            self.entry_codigo.config(state='normal')
            self.entry_nombre.config(state='normal')
            self.entry_precio.config(state='normal')
            self.entry_cantidad.config(state='normal')

            self.entry_codigo.delete(0, tk.END)
            self.entry_codigo.insert(0, values[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, values[1])
            self.entry_precio.delete(0, tk.END)
            self.entry_precio.insert(0, values[2])
            self.entry_cantidad.delete(0, tk.END)
            self.entry_cantidad.insert(0, values[3])

            self.button_guardar.config(state='normal', command=lambda: self.actualizar_datos(selected_item, values))
            self.button_cancelar.config(state='normal')
        except IndexError:
            messagebox.showerror("Error", "Seleccione un registro para editar")

    def actualizar_datos(self, item, old_values):
        # Recolectar los nuevos valores ingresados por el usuario
        nuevos_valores = {
            'codigo': self.entry_codigo.get(),
            'nombre': self.entry_nombre.get(),
            'precio': self.entry_precio.get(),
            'cantidad': self.entry_cantidad.get(),
        }
        
        # Solo actualizar los campos que han cambiado
        datos_actualizados = {}
        campos = ['codigo', 'nombre', 'precio', 'cantidad']
        for i, campo in enumerate(campos):
            if nuevos_valores[campo] != old_values[i]:
                datos_actualizados[campo] = nuevos_valores[campo]
        
        if datos_actualizados:
            editar(datos_actualizados, self.selected_insumo_id)
        
        self.tabla_insumos()
        self.deshabilitar_campos()
        self.button_guardar.config(command=self.guardar_datos)

    def eliminar_datos(self):
        try:
            selected_item = self.tabla.selection()[0]
            eliminar(self.tabla.item(selected_item, 'text'))
            self.tabla_insumos()
        except IndexError:
            messagebox.showerror("Error", "Seleccione un registro para eliminar")
