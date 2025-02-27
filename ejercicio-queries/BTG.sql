DROP TABLE IF EXISTS visitan;
DROP TABLE IF EXISTS disponibilidad;
DROP TABLE IF EXISTS inscripcion;
DROP TABLE IF EXISTS producto;
DROP TABLE IF EXISTS sucursal;
DROP TABLE IF EXISTS cliente;

CREATE TABLE cliente(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	apellidos VARCHAR(60) NOT NULL,
	ciudad VARCHAR(40) NOT NULL
);

CREATE TABLE sucursal(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(50) NOT NULL,
	ciudad VARCHAR(40) NOT NULL
);

CREATE TABLE producto(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(80) NOT NULL,
	tipo_producto VARCHAR(80) NOT NULL 
);

CREATE TABLE inscripcion(
	id_producto INT REFERENCES producto (id) NOT NULL,
	id_cliente INT REFERENCES cliente (id) NOT NULL,
	PRIMARY KEY (id_producto, id_cliente)
);

CREATE TABLE disponibilidad (
	id_sucursal INT REFERENCES sucursal (id) NOT NULL,
	id_producto INT REFERENCES producto (id) NOT NULL,
	PRIMARY KEY (id_sucursal, id_producto)
);

CREATE TABLE visitan (
	id_sucursal INT REFERENCES sucursal (id) NOT NULL,
	id_cliente INT REFERENCES cliente (id) NOT NULL,
	fecha_visita TIMESTAMP NOT NULL,
	PRIMARY KEY (id_sucursal, id_cliente)
);

