from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar los datos
datos = []

@app.route('/')
def index():
    return render_template('index.html', datos=datos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form.get('nombre')
    edad = request.form.get('edad')
    if nombre and edad:
        datos.append({'nombre': nombre, 'edad': edad})
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
