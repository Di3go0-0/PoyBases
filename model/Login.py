import tkinter as tk
from tkinter import messagebox
from .Usuarios_dao import guardar, Usuario, verificar_credenciales, crear_tabla
from .MenuPrincipal import FrameMenuPrincipal


crear_tabla()

class LoginFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de Sesión")
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

        self.button_login = tk.Button(self, text="Iniciar Sesión", command=self.login)
        self.button_login.grid(row=2, column=0, columnspan=2, pady=5)

        self.button_register = tk.Button(self, text="Registrarse", command=self.registro)
        self.button_register.grid(row=3, column=0, columnspan=2, pady=5)

        self.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if verificar_credenciales(username, password):
            messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso")
            self.mostrar_menu_principal()
        else:
            messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")

    def mostrar_menu_principal(self):
        self.destroy()
        root = tk.Tk()
        root.title("Instand Power 2000")
        root.geometry("950x300")
        menu_principal = FrameMenuPrincipal(root)
        menu_principal.grid(row=0, column=0)
        root.mainloop()

    def registro(self):
        registro_window = RegistroWindow(self)
        registro_window.grab_set()

    def cerrar_aplicacion(self):
        self.destroy()

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
