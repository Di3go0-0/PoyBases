CREATE TABLE IF NOT EXISTS Insumos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    proveedor INTEGER,
    Codigo INTEGER,
    Nombre TEXT NOT NULL,
    Precio INTEGER,
    Cantidad TEXT NOT NULL,
    FOREIGN KEY (proveedor) REFERENCES Proveedores(id)
);

CREATE TABLE IF NOT EXISTS Proveedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cedula_nit TEXT NOT NULL,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    telefono TEXT NOT NULL,
    correo TEXT NOT NULL,
    direccion TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Usuarios (
    Username TEXT UNIQUE,
    Password TEXT
);

CREATE TABLE IF NOT EXISTS construccion (
    producto_id INTEGER,
    insumo_id INTEGER,
    PRIMARY KEY (producto_id, insumo_id),
    FOREIGN KEY (producto_id) REFERENCES Productos(id),
    FOREIGN KEY (insumo_id) REFERENCES Insumos(id)
);