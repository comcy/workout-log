from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "workouts.json"
EXERCISES_FILE = "exercises.json"

# ---- Hilfsfunktionen ----
def load_json(file, default=None):
    if not os.path.exists(file):
        return default if default is not None else []
    with open(file, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return default if default is not None else []

def save_json(file, data):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ---- Workouts Endpoints ----
@app.route("/workouts", methods=["GET"])
def get_entries():
    start = request.args.get("start")
    end = request.args.get("end")
    entries = load_json(DATA_FILE, [])

    if start and end:
        entries = [e for e in entries if start <= e["date"] <= end]

    return jsonify(entries)

@app.route("/workouts/add", methods=["POST"])
def add_entry():
    data = request.json
    entries = load_json(DATA_FILE, [])
    entries.append(data)
    save_json(DATA_FILE, entries)
    return jsonify({"status": "success", "entry": data}), 201

# ---- Exercises Endpoints ----
@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = load_json(EXERCISES_FILE, [])
    return jsonify(exercises)

@app.route("/exercises/add", methods=["POST"])
def add_exercise():
    data = request.json
    exercises = load_json(EXERCISES_FILE, [])

    # Automatische ID Vergabe
    if exercises:
        max_id = max(ex["id"] for ex in exercises)
    else:
        max_id = 0
    data["id"] = max_id + 1

    exercises.append(data)
    save_json(EXERCISES_FILE, exercises)

    return jsonify({"status": "success", "exercise": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
