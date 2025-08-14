from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import uuid
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"
EXERCISE_FILE = "exercises.json"


# --- Hilfsfunktionen ---
def load_json(file):
    if not os.path.exists(file):
        return []
    with open(file, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_json(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# --- Exercises Endpoints ---
@app.route("/api/exercises", methods=["GET"])
def get_exercises():
    return jsonify(load_json(EXERCISE_FILE))


@app.route("/api/exercises", methods=["POST"])
def add_exercise():
    body = request.get_json()
    if not body or "name" not in body:
        return jsonify({"error": "Exercise name required"}), 400

    exercises = load_json(EXERCISE_FILE)
    # Prüfen ob Name schon existiert
    if any(e["name"].lower() == body["name"].lower() for e in exercises):
        return jsonify({"error": "Exercise already exists"}), 400

    new_exercise = {
        "id": str(uuid.uuid4()),
        "name": body["name"]
    }
    exercises.append(new_exercise)
    save_json(EXERCISE_FILE, exercises)
    return jsonify(new_exercise), 201


# --- Logs Endpoints ---
@app.route("/api/log", methods=["POST"])
def add_log():
    body = request.get_json()
    required = ("date", "exercise_id", "weight", "reps")
    if not body or not all(k in body for k in required):
        return jsonify({"error": "Invalid data"}), 400

    # Validierung: existiert Übung?
    exercises = load_json(EXERCISE_FILE)
    if not any(e["id"] == body["exercise_id"] for e in exercises):
        return jsonify({"error": "Exercise ID not found"}), 404

    logs = load_json(DATA_FILE)
    logs.append(body)
    save_json(DATA_FILE, logs)
    return jsonify({"status": "success"}), 201


@app.route("/api/logs", methods=["GET"])
def get_logs():
    logs = load_json(DATA_FILE)

    # optional: nach Übung filtern
    exercise_id = request.args.get("exercise_id")
    if exercise_id:
        logs = [l for l in logs if l.get("exercise_id") == exercise_id]

    # optional: nach Zeitraum filtern
    start_date = request.args.get("start")
    end_date = request.args.get("end")

    def parse_date(d):
        return datetime.strptime(d, "%Y-%m-%d")

    if start_date:
        logs = [l for l in logs if parse_date(l["date"]) >= parse_date(start_date)]
    if end_date:
        logs = [l for l in logs if parse_date(l["date"]) <= parse_date(end_date)]

    return jsonify(logs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
