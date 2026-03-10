# 📊 API de Promedio con Flask

Esta es una **API sencilla desarrollada con Python y Flask** que permite calcular el **promedio de calificaciones de un estudiante** a partir de datos enviados en formato JSON.

El proyecto fue probado utilizando **Postman** para enviar solicitudes HTTP y verificar el funcionamiento de la API.

---

# 🚀 Tecnologías utilizadas

- 🐍 Python
- 🌐 Flask
- 📬 Postman
- 📦 JSON

---

# 📂 Estructura del proyecto

```
api_promedio/
│
├── app.py
├── img/
│   └── Captura de pantalla 2026-03-10 145123.png
└── README.md
```

---

# ⚙️ Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/api_promedio.git
cd api_promedio
```

### 2️⃣ Instalar dependencias

```bash
pip install flask
```

### 3️⃣ Ejecutar la API

```bash
python app.py
```

El servidor iniciará en:

```
http://127.0.0.1:5000
```

---

# 📡 Endpoint disponible

## POST /promedio

Calcula el promedio de un estudiante a partir de una lista de calificaciones.

### URL

```
http://127.0.0.1:5000/promedio
```

### Body (JSON)

```json
{
  "nombre": "Juan Perez",
  "calificaciones": [90, 85, 88, 95]
}
```

### Respuesta

```json
{
  "estudiante": "Juan Perez",
  "promedio": 89.5
}
```

### Error si no se envían calificaciones

```json
{
  "error": "Debes proporcionar una lista de calificaciones válida."
}
```

---

# 🧪 Prueba en Postman

Para probar la API se utilizó **Postman** enviando una solicitud **POST** con datos en formato JSON.

Pasos:

1. Seleccionar método **POST**
2. Usar la URL:

```
http://127.0.0.1:5000/promedio
```

3. Ir a **Body**
4. Seleccionar **raw**
5. Elegir formato **JSON**
6. Enviar los datos del estudiante

---

# 📷 Ejemplo de prueba en Postman

![Prueba en Postman](img/Captura%20de%20pantalla%202026-03-10%20145123.png)

---

# 📘 Código principal

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    datos = request.get_json()

    nombre = datos.get('nombre')
    calificaciones = datos.get('calificaciones', [])

    if not calificaciones or not isinstance(calificaciones, list):
        return jsonify({
            "error": "Debes proporcionar una lista de calificaciones válida."
        }), 400

    promedio = sum(calificaciones) / len(calificaciones)

    return jsonify({
        "estudiante": nombre,
        "promedio": promedio
    })

if __name__ == '__main__':
    app.run(debug=True)
```

---

# 👨‍💻 Autor
Hugo Guerrero

Desarrollado como práctica de creación de **APIs con Flask** y pruebas con **Postman**.
