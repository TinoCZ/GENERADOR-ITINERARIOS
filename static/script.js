async function generarItinerario() {
  const destino = document.getElementById('destino').value.trim();
  const respuesta = document.getElementById('respuesta');

  if (!destino) {
    respuesta.textContent = 'Por favor, ingresa un destino.';
    return;
  }

  respuesta.textContent = 'Generando itinerario...';

  try {
    const res = await fetch('/gemini', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ destination: destino })
    });

    const data = await res.json();
    respuesta.textContent = data.response || 'No se pudo generar el itinerario.';
  } catch (error) {
    console.error(error);
    respuesta.textContent = 'Ocurrió un error al generar el itinerario.';
  }
}


// El archivo JavaScript contiene la función generarItinerario(), que se encarga de manejar la interacción
// del usuario con la página. Esta función es asincrónica, lo que significa que puede realizar tareas que 
// toman tiempo (como hacer una solicitud al servidor) sin bloquear el resto de la página.

// Primero, obtiene el valor ingresado por el usuario en el campo de texto usando 
// document.getElementById('destino').value.trim(). El .trim() elimina cualquier espacio
//  en blanco al principio o al final del texto.

// Luego, verifica si el usuario escribió algo. Si el campo está vacío, muestra un mensaje pidiendo que se ingrese 
// un destino y termina la ejecución con return.

// Si el destino fue ingresado correctamente, el texto "Generando itinerario..." aparece en pantalla para informar que
//  el sistema está trabajando.

// A continuación, se hace una solicitud fetch al backend, específicamente al endpoint /gemini, enviando el destino como
// un objeto JSON con método POST. Se especifica también que el tipo de contenido es JSON (Content-Type: application/json).

// Una vez que el servidor responde, el contenido de la respuesta se convierte a JSON y se muestra en pantalla usando
// respuesta.textContent = data.response. Si por alguna razón no se puede obtener una respuesta válida, se muestra un
// mensaje de error alternativo.

// Por último, si ocurre cualquier error durante el proceso (por ejemplo, si el servidor no responde o hay un problema
//  de red), el error se captura con catch y se muestra un mensaje de error al usuario en pantalla.