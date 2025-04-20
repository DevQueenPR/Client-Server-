from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info
@app.route('/info', methods=['GET'])
def get_info():
    return jsonify({
        "nombre": "Servidor Capstone",
        "descripcion": "API REST"
    })

# Ruta POST /mensaje
@app.route('/mensaje', methods=['GET', 'POST'])
def recibir_mensaje():
    print("Método recibido:", request.method)  # <-- Agregado

    if request.method == 'POST':
        data = request.get_json()
        nombre = data.get('nombre', 'invitado')
        mensaje = data.get('mensaje', '')
        return jsonify({
            "respuesta": f"Hola, {nombre}. Recibí tu mensaje: '{mensaje}'"
        })
    else:
        return jsonify({"mensaje": "Usa el método POST para enviar un mensaje."})


if __name__ == '__main__':
    app.run(debug=True)
