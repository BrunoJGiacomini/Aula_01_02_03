from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def route():
    return "Vai Corinthians!"

@app.route("/sobre", methods=["GET"])
def sobre():
    return "Este é o meu site em Flask!"

@app.route("/nova-rota", methods=["GET"])
def nova_rota():
    return "Nova rota criada com sucesso!"

@app.route("/nova-rota2", methods=["GET"])
def nova_rota2():
    return "FATEC - ID"

if __name__ == "__main__":
    app.run(debug=True)