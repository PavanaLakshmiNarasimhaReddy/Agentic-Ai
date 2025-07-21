import numpy as np

class EnvironmentalMonitor:
    def analyze_image(self, image_array):
        mean_intensity = np.mean(image_array)
        return "pollution_detected" if mean_intensity < 100 else "environment_clear"
