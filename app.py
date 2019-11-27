# pip install flask
# pip install psycopg2
# pip install Flask-Session

from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, make_response, session
from BaseDatos import *
import hashlib

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # Para los mensajes flash.

def obtenerToken(cadena):
	return hashlib.sha224(cadena.encode('UTF-8')).hexdigest()


def estaEnSesion():
	ip = request.remote_addr
	token = obtenerToken(ip)

	return token in session and session[token] != None

def contraseniaCorrecta(contrasenia):
	ip = request.remote_addr
	token = obtenerToken(ip)

	usuario = session[token]

	return esUsuario(usuario, contrasenia)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/menuAlumno")
def menuAlumno():
	return render_template('menuAlumno.html')



@app.route("/fichaLista")
def fichaLista():
	return render_template('fichaLista.html')



@app.route('/solicitarInformacion/<boleta>')
def solicitarInformacion(boleta):

	lugar = obtenerLugarBoleta(boleta)

	informacion = make_response(jsonify({
		'boleta': boleta,
		'lugar': lugar,
	}), 200)

	return informacion

@app.route("/solicitud")
def solicitud():
	aviso = ''

	if 'aviso' in request.args:
		if request.args['aviso'] == 'True':
			aviso = 'verde'
		else:
			aviso = 'rojo'

	return render_template('solicitudLocker.html', aviso=aviso)


@app.route("/enviarSolicitud", methods=['POST', 'GET'])
def enviarSolicitud():
	print(request.form)
	# Obteniendo informacion del formulario recibido.
	nombre = request.form['nombres']
	primerApellido = request.form['primerApellido']
	segundoApellido = request.form['segundoApellido']
	boleta = request.form['boleta']
	correo = request.form['correo']
	telefono = request.form['telefono']

	aviso = ''
	resultado =	insertarAlumno(boleta, nombre, primerApellido, segundoApellido, correo, telefono)

	if resultado is None:
		aviso = False
		resultado = 'No se pudo registrar'
	else:
		aviso = True
		resultado = 'Registro exitoso'

	flash(resultado)
	return redirect(url_for('solicitud', aviso=aviso))


@app.route("/login")
def login():
	if estaEnSesion():
		return redirect(url_for('solicitudes'))

	return render_template('loginAdmin.html')

@app.route("/autentificar", methods=['POST', 'GET'])
def autentificar():
	if estaEnSesion():
		return redirect(url_for('solicitudes'))

	usuario = request.form['usuario']
	clave = request.form['contrasenia']

	if loginAdmin(usuario, clave):
		ip = request.remote_addr
		token = obtenerToken(ip)
		session[token] = usuario
		return redirect(url_for('solicitudes'))
	
	return redirect(url_for('login'))



@app.route("/cerrarSesion")
def cerrarSesion():
	ip = request.remote_addr
	token = obtenerToken(ip)
	
	session.pop(token, None)
	
	return redirect(url_for('index'))

@app.route("/solicitudes")
def solicitudes():
	if estaEnSesion():
		if hayRenovaciones():
			return redirect(url_for('confirmarEliminacion'))

		solicitudes = seleccionarSolicitudes()
		return render_template('solicitudes.html', solicitudes=solicitudes)
	
	return redirect(url_for('login'))

@app.route("/confirmarEliminacion")
def confirmarEliminacion():
	if estaEnSesion():
		return render_template('confirmacionEliminacion.html')
	
	return redirect(url_for('login'))


@app.route("/eliminarRenovaciones", methods=['POST'])
def eliminarRenovaciones():
	if estaEnSesion():
		contrasenia = request.form['contrasenia']

		if contraseniaCorrecta(contrasenia):
			print('Limpiar')
			limpiarRenovaciones()
			return redirect(url_for('solicitudes'))
	
	return redirect(url_for('login'))


@app.route('/aceptarSolicitud/<boleta>')
def aceptarSolicitud(boleta):
	if estaEnSesion():
		registrarLocker(boleta)

	return redirect(url_for('solicitudes'))

@app.route('/renovacion')
def renovacion():
	if estaEnSesion():
		solicitudes = seleccionarRenovaciones()
		return render_template('renovacion.html', solicitudes=solicitudes)
	
	return redirect(url_for('login'))


@app.route('/renovarSolicitud/<boleta>')
def renovarSolicitud(boleta):
	if estaEnSesion():
		renovar(boleta)
		return redirect(url_for('renovacion'))

	return redirect(url_for('login'))

@app.route('/listaLockers')
def listaLockers():
	if estaEnSesion():
		solicitudes = seleccionarAlumnosLocker()
		return render_template('listaAlumnoLocker.html', solicitudes=solicitudes)
	
	return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True, port=3000)