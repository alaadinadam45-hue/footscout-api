import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

TRIALS = [
    {
        "club": "Guiseley AFC",
        "date": "2026-05-15",
        "time": "18:00",
        "location": "Nethermoor Park",
        "distance": "8 km",
        "score": 90
    }
]

@app.route("/")
def home():
    return {"message": "API is running"}

@app.route("/trials")
def trials():
    return jsonify(TRIALS)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
