import threading
import time
import random
import numpy as np
import re

# RL Module
class AdaptivePlanner:
    def run(self):
        while True:
            state = random.choice(["low traffic", "high energy use", "balanced"])
            action = f"Plan for {state}"
            reward = random.uniform(0, 1)
            print(f"[RL] State: {state}, Action: {action}, Reward: {reward:.2f}")
            time.sleep(5)

# NLP Module
class CitizenEngagement:
    def run(self):
        feedback_samples = [
            "We need more parks.",
            "Traffic is terrible downtown.",
            "Recycling bins are missing.",
            "Great job on the new bike lanes!"
        ]
        while True:
            feedback = random.choice(feedback_samples)
            keywords = set(re.findall(r'\b\w+\b', feedback.lower()))
            print(f"[NLP] Feedback: \"{feedback}\" → Keywords: {keywords}")
            time.sleep(4)

# CV Module
class EnvironmentalMonitor:
    def run(self):
        while True:
            image = np.random.randint(0, 255, (100, 100), dtype=np.uint8)
            mean_intensity = np.mean(image)
            status = "pollution_detected" if mean_intensity < 100 else "environment_clear"
            print(f"[CV] Mean Intensity: {mean_intensity:.2f} → Status: {status}")
            time.sleep(6)

# Federated Learning Module
class FederatedClient:
    def run(self):
        while True:
            local_data = [random.uniform(1, 5) for _ in range(5)]
            update = sum(local_data) / len(local_data)
            print(f"[FL] Client Update: {update:.2f}")
            time.sleep(7)

# Launch all modules in threads
def start_civicmind_simulation():
    modules = [
        AdaptivePlanner(),
        CitizenEngagement(),
        EnvironmentalMonitor(),
        FederatedClient()
    ]
    threads = [threading.Thread(target=mod.run) for mod in modules]
    for t in threads:
        t.start()

if __name__ == "__main__":
    start_civicmind_simulation()
