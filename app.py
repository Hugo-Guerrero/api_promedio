from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    # Recibir datos en formato JSON
    datos = request.get_json()

    # Extraer nombre y lista de calificaciones
    nombre = datos.get('nombre')
    calificaciones = datos.get('calificaciones', [])

    # Validar que haya calificaciones
    if not calificaciones or not isinstance(calificaciones, list):
        return jsonify({
            "error": "Debes proporcionar una lista de calificaciones válida."
        }), 400

    # Calcular promedio
    promedio = sum(calificaciones) / len(calificaciones)

    # Respuesta en formato JSON
    return jsonify({
        "estudiante": nombre,
        "promedio": promedio
    })

if __name__ == '__main__':
    app.run(debug=True)
