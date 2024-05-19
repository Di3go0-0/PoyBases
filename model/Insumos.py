import tkinter as tk
from tkinter import ttk, messagebox
from .Insumos_dao import crear_tabla_insumos, borrar_tabla, Insumo, guardar, listar, editar, eliminar

class InsumosFrame(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("Gestión de Insumos")
        self.geometry("800x600")
        self.setup_ui()
        self.tabla_insumos()
        self.deshabilitar_campos()

    def setup_ui(self):
        self.label_codigo = tk.Label(self, text='Codigo:')
        self.label_codigo.grid(row=0, column=0, padx=10, pady=10)
        self.entry_codigo = tk.Entry(self)
        self.entry_codigo.grid(row=0, column=1, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text='Nombre:')
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.label_precio = tk.Label(self, text='Precio:')
        self.label_precio.grid(row=2, column=0, padx=10, pady=10)
        self.entry_precio = tk.Entry(self)
        self.entry_precio.grid(row=2, column=1, padx=10, pady=10)

        self.label_cantidad = tk.Label(self, text='Cantidad:')
        self.label_cantidad.grid(row=3, column=0, padx=10, pady=10)
        self.entry_cantidad = tk.Entry(self)
        self.entry_cantidad.grid(row=3, column=1, padx=10, pady=10)

        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.grid(row=4, column=0, padx=10, pady=10)

        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.button_guardar.grid(row=4, column=1, padx=10, pady=10)

        self.button_cancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar_campos)
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
        self.button_editar.grid(row=8, column=0, padx=10, pady=10)

        self.button_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_datos)
        self.button_eliminar.grid(row=8, column=1, padx=10, pady=10)

    def habilitar_campos(self):
        self.entry_codigo.config(state='normal')
        self.entry_nombre.config(state='normal')
        self.entry_precio.config(state='normal')
        self.entry_cantidad.config(state='normal')

    def deshabilitar_campos(self):
        self.entry_codigo.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.entry_precio.config(state='disabled')
        self.entry_cantidad.config(state='disabled')
        self.button_guardar.config(state='disabled')
        self.button_cancelar.config(state='disabled')

    def guardar_datos(self):
        Insumo = Insumo(
            self.entry_codigo.get(),
            self.entry_nombre.get(),
            self.entry_precio.get(),
            self.entry_cantidad.get(),
        )
        guardar(Insumo)
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

            self.button_guardar.config(command=lambda: self.actualizar_datos(selected_item))
        except IndexError:
            messagebox.showerror("Error", "Seleccione un registro para editar")

    def actualizar_datos(self, item):
        Insumo = Insumo(
            self.entry_codigo.get(),
            self.entry_nombre.get(),
            self.entry_precio.get(),
            self.entry_cantidad.get(),
        )
        editar(Insumo, self.tabla.item(item, 'text'))
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
