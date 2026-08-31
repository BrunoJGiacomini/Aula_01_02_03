from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def route():
    return "Vai Corinthians!"

@app.route("/sobre", methods=["GET"])
def sobre():
    return "Este é o meu site em Flask!"

if __name__ == "__main__":
    app.run(debug=True)