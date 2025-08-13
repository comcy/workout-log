from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"


def load_data():
    """Lädt die Trainingslogs aus der JSON-Datei."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_data(data):
    """Speichert die Trainingslogs in die JSON-Datei."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.route("/api/log", methods=["POST"])
def add_log():
    entry = request.get_json()

    if not entry or not all(k in entry for k in ("date", "exercise", "weight", "reps")):
        return jsonify({"error": "Invalid data"}), 400

    data = load_data()
    data.append(entry)
    save_data(data)
    return jsonify({"status": "success"}), 201


@app.route("/api/logs", methods=["GET"])
def get_logs():
    data = load_data()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
