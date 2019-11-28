import psycopg2
from datetime import datetime
from configparser import ConfigParser

semestreAnterior = '21-1'
semestreActual = '21-2'

def configurarBase(archivoConfiguracion='configuracionBase.ini', section='postgresql'):
	parser = ConfigParser()
	parser.read(archivoConfiguracion)

	baseDatos = {}
	
	if parser.has_section(section):
		params = parser.items(section)
		for param in params:
			baseDatos[param[0]] = param[1]
	else:
		raise Exception('Section {0} not found in the {1} file'.format(section, archivoConfiguracion))

	return baseDatos

def insertarEnBase(consulta, datos=()):
	conexion = None
	informacion = None

	try:
		# Configuración de base
		params = configurarBase()
		# Conexión a base de datos PostgreSQL
		conexion = psycopg2.connect(**params)
		# Crear nuevo cursor
		cur = conexion.cursor()
	
		# Ejecutar sql
		cur.execute(consulta, datos)
		# Obtener boleta
		# Subir cambios a la base de datos
		conexion.commit()
		# Cerrar comunicación de la base
		cur.close()
		informacion = True
	except (Exception, psycopg2.DatabaseError) as error:
		print(f"Error al insertar informacion: {error}")
	finally:
		if conexion is not None:
			conexion.close()
	
	return informacion

def insertarAlumno(boleta, nombre, primerApellido, segundoApellido, correo, telefono):
	consulta = '''
		SELECT * FROM alumno where boleta=%s
	'''%(boleta)

	alumno = None
	
	if len(selectEnBase(consulta)) == 0:
		sqlInsertarRegistro = '''
			INSERT INTO alumno(boleta, nombre, primerApellido, segundoApellido, correo, telefono)
			VALUES(%s, %s, %s, %s, %s, %s);
		'''

		sqlInsertarLista = '''
			INSERT INTO lista(fechaRegistro, alumno)
			VALUES(%s, %s);
		'''


		fecha = datetime.now()
		datos = (boleta, nombre, primerApellido, segundoApellido, correo, telefono)		
		# Ejecutar sql
		alumno = insertarEnBase(sqlInsertarRegistro, datos)
		
		datos = (fecha, boleta)
		alumno = insertarEnBase(sqlInsertarLista, datos)
	
	return alumno

def selectEnBase(consulta):
	conexion = None
	resultados = []

	try:
		params = configurarBase()
		conexion = psycopg2.connect(**params)
		cur = conexion.cursor()
		cur.execute(consulta)

		row = cur.fetchone()

		while row is not None:
			resultados.append(row)
			row = cur.fetchone()

		cur.close()

	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conexion is not None:
			conexion.close()
	

	return resultados

def seleccionarSolicitudes():
	consulta = '''
		SELECT a.nombre, a.primerApellido, a.segundoApellido, a.boleta, l.fechaRegistro FROM lista AS l
		INNER JOIN alumno AS a ON l.alumno=a.boleta ORDER BY l.fechaRegistro ASC
	'''

	consultaDisponibles = '''
		SELECT count(numero) FROM locker
		EXCEPT
		SELECT l.numero FROM alumno_locker AS a
		INNER JOIN locker AS l ON l.numero=a.locker;
	'''

	alumnos = []
	solicitudes = selectEnBase(consulta)
	disponibles = selectEnBase(consultaDisponibles)[0][0]

	for informacionAlumno in solicitudes:
		if disponibles <= len(alumnos):
			break

		alumno = {
			'nombre': informacionAlumno[0],
			'primerApellido': informacionAlumno[1],
			'segundoApellido': informacionAlumno[2],
			'boleta': informacionAlumno[3],
			'fecha': informacionAlumno[4]
		}
		
		alumnos.append(alumno)

	return alumnos

def seleccionarRenovaciones():
	consulta = '''
		SELECT a.nombre, a.primerApellido, a.segundoApellido, a.boleta, l.locker FROM alumno_locker AS l
		INNER JOIN alumno AS a ON l.alumno=a.boleta AND l.semestre='%s' ORDER BY l.locker ASC;
	'''%(semestreAnterior)

	alumnos = []
	solicitudes = selectEnBase(consulta)

	for informacionAlumno in solicitudes:

		alumno = {
			'nombre': informacionAlumno[0],
			'primerApellido': informacionAlumno[1],
			'segundoApellido': informacionAlumno[2],
			'boleta': informacionAlumno[3],
			'locker': informacionAlumno[4]
		}
		
		alumnos.append(alumno)


	return alumnos

def seleccionarAlumnosLocker():
	consulta = '''
		SELECT a.nombre, a.primerApellido, a.segundoApellido, a.boleta, l.locker, a.correo FROM alumno_locker AS l
		INNER JOIN alumno AS a ON l.alumno=a.boleta ORDER BY l.locker ASC
	'''

	alumnos = []
	solicitudes = selectEnBase(consulta)

	for informacionAlumno in solicitudes:

		alumno = {
			'nombre': informacionAlumno[0],
			'primerApellido': informacionAlumno[1],
			'segundoApellido': informacionAlumno[2],
			'boleta': informacionAlumno[3],
			'locker': informacionAlumno[4],
			'correo': informacionAlumno[5]
		}
		
		alumnos.append(alumno)


	return alumnos	

def obtenerLugarBoleta(boleta):
	lugar = None
	consulta = f"SELECT lugar FROM lista WHERE alumno={boleta}"

	resultados = selectEnBase(consulta)

	if len(resultados) > 0:
		lugar = resultados[0][0]

	return lugar

def loginAdmin(usuario, clave):
	consulta = f"SELECT * from admin WHERE usuario='{usuario}' AND clave='{clave}'"
	resultados = selectEnBase(consulta)
	
	return len(resultados) == 1

def registrarLocker(boleta):
	consulta = '''
		SELECT numero FROM locker WHERE estado = true ORDER BY numero ASC
	'''
	
	locker = selectEnBase(consulta)

	if len(locker) > 0:
		locker = locker[0][0]

		consulta = '''
			INSERT INTO alumno_locker(alumno, locker, semestre)
			VALUES(%s, %s, %s);
			
			UPDATE locker SET estado = false
			WHERE numero = %s;

			DELETE FROM lista
			WHERE alumno = %s;
		'''
		datos = (boleta, locker, semestreActual, locker, boleta)

		insertarEnBase(consulta, datos)

	return


def renovar(boleta):
	consulta = '''
		UPDATE alumno_locker SET semestre = %s
		WHERE alumno = %s	
	'''
	datos = (semestreActual, boleta)

	insertarEnBase(consulta, datos)

	return

def hayRenovaciones():
	consulta = '''
		SELECT * FROM alumno_locker
		WHERE semestre='%s';
	'''%(semestreAnterior)

	resultado = len(selectEnBase(consulta)) > 0

	return resultado

def esUsuario(usuario, clave):
	consulta = '''
		SELECT * FROM admin WHERE usuario = '%s' AND clave = '%s'
	'''%(usuario, clave)

	resultados = selectEnBase(consulta)

	return len(resultados) > 0

def limpiarRenovaciones():
	consulta = '''
		UPDATE locker SET estado = true
		WHERE numero IN (SELECT locker FROM alumno_locker where semestre = '%s');
		
		DELETE FROM alumno
		WHERE boleta IN (
			SELECT boleta  FROM alumno AS a
			INNER JOIN alumno_locker AS l
			on(a.boleta = l.alumno and l.semestre = '%s')
		);

		DELETE FROM alumno_locker
		WHERE semestre = '%s';
	'''%(semestreAnterior, semestreAnterior, semestreAnterior)

	insertarEnBase(consulta)

	return