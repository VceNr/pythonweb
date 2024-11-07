from flask import Flask, render_template
import requests

app = Flask(__name__)

# IP del ESP32
ESP32_IP = "http://192.168.1.145:8080"  # Cambia esto por la IP de tu ESP32

@app.route('/')
def index():
    try:
        # Realiza una solicitud al ESP32 con un tiempo de espera
        response = requests.get(f"{ESP32_IP}/")
        response.raise_for_status()  # Verifica si hubo un error HTTP
        # Suponiendo que el ESP32 devuelve un JSON con la información que queremos
        data = response.json()  # Esperamos que el ESP32 devuelva JSON
        return render_template('index.html', data=data)  # Pasa los datos al template
    except requests.exceptions.Timeout:
        return "Error: Tiempo de espera agotado al intentar conectar con el ESP32"
    except requests.exceptions.RequestException as e:
        return f"Error al conectar con el ESP32: {e}"

if __name__ == '__main__':
    app.run(debug=True)
