from flask import Flask, jsonify
import main  # importa tu función principal que ya tenés

app = Flask(__name__)

@app.route("/")
def recomendar():
    resultado = main.main({})
    return jsonify(resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
