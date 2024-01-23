from app import app

@app.route("/test")
def test_route():
    return "Esta es una ruta de prueba"