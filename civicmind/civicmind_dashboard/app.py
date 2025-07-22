import threading
import time
import random
import numpy as np
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Shared data dictionary
data = {
    "rl": "Initializing...",
    "nlp": "Initializing...",
    "cv": "Initializing...",
    "fl": "Initializing..."
}

def rl_thread():
    while True:
        state = random.choice(["low traffic", "high energy use", "balanced"])
        action = f"Plan for {state}"
        reward = random.uniform(0, 1)
        data["rl"] = f"State: {state}, Action: {action}, Reward: {reward:.2f}"
        time.sleep(5)

def nlp_thread():
    feedback_samples = [
        "We need more parks.",
        "Traffic is terrible downtown.",
        "Recycling bins are missing.",
        "Great job on the new bike lanes!"
    ]
    while True:
        feedback = random.choice(feedback_samples)
        keywords = set(feedback.lower().split())
        data["nlp"] = f"Feedback: '{feedback}' → Keywords: {keywords}"
        time.sleep(4)

def cv_thread():
    while True:
        image = np.random.randint(0, 255, (100, 100), dtype=np.uint8)
        mean_intensity = np.mean(image)
        status = "pollution_detected" if mean_intensity < 100 else "environment_clear"
        data["cv"] = f"Mean Intensity: {mean_intensity:.2f} → Status: {status}"
        time.sleep(6)

def fl_thread():
    while True:
        local_data = [random.uniform(1, 5) for _ in range(5)]
        update = sum(local_data) / len(local_data)
        data["fl"] = f"Client Update: {update:.2f}"
        time.sleep(7)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/updates")
def updates():
    return jsonify(data)

if __name__ == "__main__":
    threading.Thread(target=rl_thread, daemon=True).start()
    threading.Thread(target=nlp_thread, daemon=True).start()
    threading.Thread(target=cv_thread, daemon=True).start()
    threading.Thread(target=fl_thread, daemon=True).start()
    app.run(debug=True)
