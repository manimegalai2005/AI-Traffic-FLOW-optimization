from skimage import io, color
import numpy as np
from traffic_optimizer import analyze_traffic

# Load traffic image (use a grayscale or convert it)
image_path = 'data/traffic_sample.jpg'
image = io.imread(image_path)
gray_image = color.rgb2gray(image)

# Analyze traffic
decision = analyze_traffic(gray_image)
print(f"Traffic Control Decision: {decision}")
