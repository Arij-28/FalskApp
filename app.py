from flask import Flask, jsonify

app = Flask(__name__)

# Page d'accueil
@app.route("/")
def home():
    return "Bienvenue sur mon application Flask ! 🚀"

# Endpoint d'API (exemple)
@app.route("/api", methods=["GET"])
def api():
    return jsonify({
        "message": "Ceci est une API Flask simple.",
        "status": "success"
    })

# Endpoint avec paramètre
@app.route("/greet/<name>")
def greet(name):
    return f"Salut, {name}! Bienvenue sur Flask."

if __name__ == "__main__":
    # Lancer l'application Flask sur le port 5000
    app.run(host="0.0.0.0", port=5000)
