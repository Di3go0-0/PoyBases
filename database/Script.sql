CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cedula_nit TEXT NOT NULL,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT NOT NULL,
    direccion TEXT NOT NULL
);  

CREATE TABLE Insumos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Codigo INTEGER,
    Nombre TEXT NOT NULL,
    Precio INTEGER,
    Cantidad TEXT NOT NULL
);

CREATE TABLE Proveedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cedula_nit TEXT NOT NULL,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT NOT NULL,
    direccion TEXT NOT NULL
);

CREATE TABLE Usuarios (
    Username TEXT UNIQUE,
    Password TEXT
);

CREATE TABLE construcción (
    producto_id INTEGER,
    insumo_id INTEGER,
    PRIMARY KEY (producto_id, insumo_id),
    FOREIGN KEY (producto_id) REFERENCES producto(id),
    FOREIGN KEY (insumo_id) REFERENCES insumo(id)
);