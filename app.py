from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
app = Flask(__name__)

# Reemplazá por tu API key
genai.configure(api_key="AIzaSyBfXocqkQtHBqmoo8d55laDQ5DKznxCMpI")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gemini', methods=['POST'])
def generar_itinerario():
    data = request.get_json()
    destino = data.get('destination')

    if not destino:
        return jsonify({'response': 'No se proporcionó un destino'}), 400

    prompt = f"""
    Eres un guía turístico. Necesito que me armes un itinerario de un viaje a {destino}. 
    El viaje debe durar una semana. Haz una lista de actividades, lugares para visitar, 
    lugares para comer y consejos útiles.
    """

    try:
        model = genai.GenerativeModel('models/gemini-2.0-flash')
        response = model.generate_content(prompt)
        # Agregamos separación entre los días reemplazando "Día X:" por "Día X:\n\n"
        texto_limpio = response.text.replace("**", "").replace("*", "").replace("\n", " ")
        texto_limpio = " ".join(texto_limpio.split())  # Elimina espacios extra
        texto_limpio = texto_limpio.replace("Día", "\n\nDía").replace("Consejos Útiles", "\n\nConsejos Útiles").replace("Idioma", "\n\nIdioma").replace("Ropa", "\n\nRopa").replace("Moneda", "\n\nMoneda").replace("Comer Adicionales", "\n\nComer Adicionales")

        return jsonify({'response': texto_limpio})
    except Exception as e:
        print('Error:', e)
        return jsonify({'response': 'Hubo un error al generar el itinerario.'}), 500

if __name__ == '__main__':
    app.run(debug=True)




# El archivo app.py es el corazón de una aplicación web creada con Flask, que se conecta a la inteligencia artificial 
# de Gemini para generar un itinerario de viaje en función de un destino que el usuario proporciona.

# Primero, se importan las librerías necesarias: Flask para construir el servidor web, request y jsonify para manejar
# datos enviados desde el navegador, y render_template para mostrar archivos HTML. También se importa la librería 
# google.generativeai, que permite conectarse con el modelo Gemini.

# Luego se crea una instancia de Flask, lo cual da origen a la aplicación web. A continuación, se configura la API Key
# de Gemini, que permite autenticar al usuario y acceder a los modelos de IA.

# La aplicación define dos rutas: la primera (/) es la ruta principal. Al acceder a ella, el servidor devuelve el archivo
# index.html, que contiene la interfaz visual donde el usuario puede escribir un destino.

# La segunda ruta (/gemini) es accesible solo mediante solicitudes POST. Cuando el usuario envía un destino, este llega
# en formato JSON. El servidor extrae el valor del destino enviado y valida que se haya recibido correctamente. 
# Si no se envió nada, responde con un mensaje de error y un código HTTP 400.

# Si el destino fue proporcionado, se crea un "prompt", es decir, un mensaje que se le envía al modelo Gemini para 
# pedirle que actúe como un guía turístico y que cree un itinerario de una semana para ese lugar, 
# incluyendo actividades, lugares para visitar, lugares para comer y consejos útiles.

# El modelo usado es gemini-2.0-flash, una versión rápida ideal para respuestas breves. Se genera contenido con ese
#  prompt, y luego se realiza una limpieza del texto para eliminar símbolos innecesarios como asteriscos, espacios
#  repetidos y para agregar saltos de línea que ayuden a que el texto se vea más ordenado en pantalla.

# Después de la limpieza, el texto resultante se devuelve al navegador como un JSON, que será mostrado al usuario
# mediante JavaScript.

# Si ocurre un error en cualquier momento del proceso, como un fallo en la conexión o un error de la API, se captura
#  con un bloque try-except. En ese caso, se imprime el error en la consola y se devuelve un mensaje indicando que hubo
#  un problema, con un código de error HTTP 500.

# Finalmente, el archivo termina con una condición que permite ejecutar la aplicación directamente desde la consola.
# Si se hace así, el servidor se ejecuta en modo debug, lo que permite ver errores detallados y reinicia automáticamente
# cuando se realizan cambios en el código.