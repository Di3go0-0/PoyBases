import tkinter as tk
from tkinter import ttk, messagebox
from Controllers.Construccion_dao import crear_tabla_construccion, borrar_tabla, Construccion, guardar, listar, eliminar, editar
class ConstruccionFrame(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.title("Gestión de Construcción de Productos")
        self.geometry("1000x450")
        self.setup_ui()
        self.tabla_construccion()
        self.selected_construccion = None
        self.edit_mode = False  # Añadir este atributo
        self.habilitar_campos()  # Deshabilitar campos al inicio

    def setup_ui(self):
        self.label_producto_id = tk.Label(self, text='ID Producto:')
        self.label_producto_id.config(font=('Arial', 12, 'bold'))
        self.label_producto_id.grid(row=0, column=0, padx=10, pady=10)
        self.mi_producto_id = tk.StringVar()
        self.entry_producto_id = tk.Entry(self, textvariable=self.mi_producto_id)
        self.entry_producto_id.config(width=30, font=('Arial', 12))
        self.entry_producto_id.grid(row=0, column=1, padx=10, pady=10)

        self.label_insumo_id = tk.Label(self, text='ID Insumo:')
        self.label_insumo_id.config(font=('Arial', 12, 'bold'))
        self.label_insumo_id.grid(row=1, column=0, padx=10, pady=10)
        self.mi_insumo_id = tk.StringVar()
        self.entry_insumo_id = tk.Entry(self, textvariable=self.mi_insumo_id)
        self.entry_insumo_id.config(width=30, font=('Arial', 12))
        self.entry_insumo_id.grid(row=1, column=1, padx=10, pady=10)

        # Agregar botón "Nuevo"
        self.button_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.button_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#4D857E', cursor='hand2', activebackground='#81D6CC')
        self.button_nuevo.grid(row=2, column=0, padx=10, pady=10)

        self.button_guardar = tk.Button(self, text='Guardar', command=self.guardar_construccion, state='disabled')  # Deshabilitar el botón guardar
        self.button_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#6A9757', cursor='hand2', activebackground='#A0DA89')
        self.button_guardar.grid(row=2, column=1, padx=10, pady=10)

        self.button_editar = tk.Button(self, text='Editar', command=self.editar_construccion, state='disabled')  # Deshabilitar el botón editar
        self.button_editar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#4D857E', cursor='hand2', activebackground='#81D6CC')
        self.button_editar.grid(row=2, column=2, padx=10, pady=10)

        self.button_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_construccion, state='disabled')  # Deshabilitar el botón eliminar
        self.button_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')
        self.button_eliminar.grid(row=2, column=3, padx=10, pady=10)

        self.tabla = ttk.Treeview(self, columns=('Producto ID', 'Insumo ID'))
        self.tabla.grid(row=3, column=0, columnspan=4, sticky='nsew')
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=3, column=4, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='Producto ID')
        self.tabla.heading('#1', text='Insumo ID')

        self.button_salir = tk.Button(self, text='Salir', command=self.destroy)
        self.button_salir.config(width=20, font=('Arial', 12, 'bold'), fg='white', bg='#9E6262', cursor='hand2', activebackground='#E38B8B')
        self.button_salir.grid(row=4, column=0, columnspan=4, padx=10, pady=10)



    def habilitar_campos(self):
        self.entry_producto_id.config(state='normal')  # Habilitar los campos
        self.entry_insumo_id.config(state='normal')
        self.button_guardar.config(state='normal')  # Habilitar los botones
        self.button_editar.config(state='normal')
        self.button_eliminar.config(state='normal')

        self.mi_producto_id.set('')
        self.mi_insumo_id.set('')
        self.edit_mode = False

    # Resto del código...

    def validar_datos(self):
        producto_id = self.mi_producto_id.get()
        insumo_id = self.mi_insumo_id.get()

        try:
            int(producto_id)
            int(insumo_id)
            return True
        except ValueError:
            messagebox.showerror("Error de Validación", "Ambos campos deben ser enteros.")
            return False

    def guardar_construccion(self):
        if not self.validar_datos():
            return

        construccion = Construccion(
            int(self.mi_producto_id.get()),
            int(self.mi_insumo_id.get())
        )
        if self.edit_mode:
            editar({'producto_id': construccion.producto_id, 'insumo_id': construccion.insumo_id}, *self.selected_construccion)
        else:
            guardar(construccion)
        self.tabla_construccion()

    def tabla_construccion(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        construcciones = listar()
        for construccion in construcciones:
            self.tabla.insert('', 'end', values=(construccion[0], construccion[1]))
    def eliminar_construccion(self):
        try:
            selected_item = self.tabla.selection()[0]
            values = self.tabla.item(selected_item, 'values')
            eliminar(int(values[0]), int(values[1]))
            self.tabla_construccion()
        except IndexError:
            messagebox.showerror("Error", "Seleccione un registro para eliminar")

    def editar_construccion(self):
        try:
            selected_item = self.tabla.selection()[0]
            values = self.tabla.item(selected_item, 'values')
            self.mi_producto_id.set(values[0])
            self.mi_insumo_id.set(values[1])
            self.edit_mode = True
            self.selected_construccion = (int(values[0]), int(values[1]))  # Guardar el producto_id y insumo_id originales
        except IndexError:
            messagebox.showerror("Error", "Seleccione un registro para editar")
    



