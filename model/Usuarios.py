import tkinter as tk
from tkinter import messagebox
from .Usuarios_dao import guardar, Usuario, verificar_credenciales, crear_tabla

class RegistroWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Registro de Nuevo Usuario")
        self.geometry("300x180")
        self.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        self.label_username = tk.Label(self, text="Nombre de usuario:")
        self.label_username.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_username = tk.Entry(self)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)

        self.label_password = tk.Label(self, text="Contraseña:")
        self.label_password.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)

        self.label_confirm_password = tk.Label(self, text="Confirmar Contraseña:")
        self.label_confirm_password.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_confirm_password = tk.Entry(self, show="*")
        self.entry_confirm_password.grid(row=2, column=1, padx=10, pady=5)

        self.button_register = tk.Button(self, text="Registrarse", command=self.registrarse)
        self.button_register.grid(row=3, column=0, columnspan=2, pady=5)

    def registrarse(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
        else:
            usuario = Usuario(username, password)
            guardar(usuario)
            self.destroy()