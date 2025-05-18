import cv2
import numpy as np

def analyze_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    traffic_density = np.mean(gray)
    
    if traffic_density < 80:
        return "Green"
    elif traffic_density < 150:
        return "Yellow"
    else:
        return "Red"

cap = cv2.VideoCapture(0)  # Use 0 for webcam; replace with path to a video file if needed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    decision = analyze_frame(frame)
    cv2.putText(frame, f"Traffic Light: {decision}", (30, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Traffic Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
