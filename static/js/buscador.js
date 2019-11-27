let input = null;
let boton = null;
let lugar = null;
let mensaje = null;

window.onload = () => {
	input = document.querySelector('#boleta');
	boton = document.querySelector('#buscar');
	lugar = document.querySelector('#lugar-boleta');
	mensaje = document.querySelector('#mensaje');

	boton.onclick = () => {
		const boleta = input.value;
		fetch(`http://127.0.0.1:3000/solicitarInformacion/${boleta}`).then(
			respuesta => respuesta.json()
		).then(informacion => {
			let textoMensaje = '';
			console.log(informacion);
		
			if (informacion.lugar) 
				lugar.innerHTML = informacion.lugar;
			else {
				lugar.innerHTML = '';
				textoMensaje = 'No se encontro ficha.';
			}

			mensaje.innerHTML = textoMensaje;
		})
		.catch(error => {
			console.log(error);
		});

		console.log(`Buscar ficha de boleta ${boleta}`);
	}
};