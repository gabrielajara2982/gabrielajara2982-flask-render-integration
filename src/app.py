import os
import flask
from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)

# Obtener la ruta base del archivo app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta relativa al modelo dentro de la carpeta models
model_path = os.path.join(BASE_DIR, "../models/decision_tree_classifier.pkl")

# Cargar el modelo
model = load(open(model_path, "rb"))

# Diccionario de clases
class_dict = {
    "0": "No Diabetes",
    "1": "Con Diabetes"
}

@app.route("/", methods=["GET", "POST"])
def index():
    pred_class = None
    if request.method == "POST":
        try:
            val1 = float(request.form["val1"])
            val2 = float(request.form["val2"])
            val3 = float(request.form["val3"])
            val4 = float(request.form["val4"])
            val5 = float(request.form["val5"])
            val6 = float(request.form["val6"])
            val7 = float(request.form["val7"])

            data = [[val1, val2, val3, val4, val5, val6, val7]]
            prediction = str(model.predict(data)[0])
            pred_class = class_dict[prediction]
        except Exception as e:
            pred_class = f"Error en la predicción: {e}"

    return render_template("index.html", prediction=pred_class)

if __name__ == "__main__":
    # Usar el puerto que Render le asigna
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

    