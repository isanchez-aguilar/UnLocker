CREATE TABLE locker (
	numero serial PRIMARY KEY,
	estado bool
);

CREATE TABLE alumno (
	nombre varchar (30),
	correo varchar (50),
	telefono varchar (15),
	boleta int PRIMARY KEY,
	primerApellido varchar (30),
	segundoApellido varchar (30)
);

CREATE TABLE lista (
	lugar serial not null,
	fechaRegistro timestamp not null,
	alumno int REFERENCES alumno (boleta) ON DELETE CASCADE,
	PRIMARY KEY (alumno)
);

CREATE TABLE alumno_locker (
	alumno int REFERENCES alumno(boleta) ON DELETE CASCADE,
	locker int REFERENCES locker(numero) ON DELETE CASCADE,
	semestre char (5),
	PRIMARY KEY (alumno, semestre)
);


CREATE TABLE admin (
	usuario varchar (20) PRIMARY KEY,
	clave varchar (20) not null
);

INSERT INTO admin(usuario, clave) VALUES('admin', 'admin');

INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
INSERT INTO locker(estado) values(true);
