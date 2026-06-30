from flask import Flask, render_template, request
app = Flask(__name__)

LIMITES = {
    "BBVA": 50000,
    "Banorte": 40000,
    "Santander": 45000,
    "HSBC": 35000,
    "Citibanamex": 60000
}

@app.route("/", methods=["GET","POST"])
def index():
    reporte = None
    if request.method == "POST":
        banco = request.form["banco"]
        monto = float(request.form["monto"])
        limite = LIMITES[banco]

        riesgo = "BAJO"
        if monto > limite:
            riesgo = "ALTO"

        reporte = {
            "banco": banco,
            "monto": monto,
            "limite": limite,
            "riesgo": riesgo
        }

    return render_template("index.html", reporte=reporte, limites=LIMITES)

if __name__ == "__main__":
    app.run(debug=True)
