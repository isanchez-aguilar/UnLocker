-- Listado de solicitudes
SELECT alumno.boleta, alumno.nombre, lista.fechasolicitud
	FROM alumno alumno JOIN lista lista
		ON alumno.boleta = lista.alumno;

-- Lugar en la lista
SELECT lugar FROM lista WHERE alumno = $BOLETA;

-- Registro
INSERT INTO alumno(boleta, nombre, primerApellido, segundoApellido, correo, telefono) VALUES(
	$BOLETA,
	$NOMBRE,
	$PRIMER APELLIDO,
	$SEGUNDO APELLIDO,
	$CORREO,
	$TELEFONO
);

INSERT INTO lista VALUES(
	$LASTID+1,
	$BOLETA,
	$TODAY);

-- Solicitud aceptada
INSERT INTO alumno_locker VALUES(
	$BOLETA,
	$LOCKER,
	$SEMESTRE_ACTUAL);
UPDATE locker
	SET estado = true
	WHERE numero = $LOCKER;

SELECT a.nombre, a.primerApellido, a.segundoApellido, a.boleta, l.fechaRegistro FROM lista AS l
INNER JOIN alumno AS a ON l.alumno=a.boleta ORDER BY l.fechaRegistro ASC;

SELECT a.nombre, a.primerApellido, a.segundoApellido, a.boleta, l.locker FROM alumno_locker AS l
INNER JOIN alumno AS a ON l.alumno=a.boleta AND l.semestre='21-1' ORDER BY l.locker ASC;

SELECT count(numero) FROM locker
EXCEPT
SELECT l.numero FROM alumno_locker AS a
INNER JOIN locker AS l ON l.numero=a.locker;

SELECT * FROM alumno_locker
WHERE semestre='21-1';

SELECT * FROM admin WHERE usuario = 'admin' AND clave = 'admin';
INSERT INTO admin(usuario, clave) VALUES('admin', 'admin');

UPDATE locker SET estado=false
WHERE numero IN (SELECT locker FROM alumno_locker where semestre='21-1');