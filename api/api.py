from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
from datetime import datetime

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


CSV_FILE = 'training_data.csv'

@app.route("/api/log", methods=["POST"])
def log_training():
    data = request.get_json()
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            data.get("date", datetime.now().isoformat()),
            data["exercise"],
            data["weight"],
            data["reps"]
        ])
    return jsonify({"status": "ok"}), 200

@app.route("/api/logs", methods=["GET"])
def get_logs():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            logs = [
                {"date": row[0], "exercise": row[1], "weight": row[2], "reps": row[3]}
                for row in reader
            ]
        return jsonify(logs)
    except FileNotFoundError:
        return jsonify([])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

