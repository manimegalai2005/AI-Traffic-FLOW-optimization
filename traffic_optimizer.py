import numpy as np

def analyze_traffic(image_gray):
    """
    Analyzes grayscale traffic image and returns signal decision.
    """
    traffic_density = np.mean(image_gray)

    if traffic_density < 0.3:
        return "Green Light – Low Traffic"
    elif traffic_density < 0.6:
        return "Yellow Light – Moderate Traffic"
    else:
        return "Red Light – High Traffic"
