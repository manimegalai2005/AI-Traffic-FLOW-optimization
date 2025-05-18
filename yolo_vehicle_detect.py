from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Download automatically

cap = cv2.VideoCapture("data/traffic_video.mp4")  # Replace with your file or 0 for webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    vehicles = [d for d in results[0].boxes.cls.tolist() if int(d) in [2, 3, 5, 7]]  # Car, Motorcycle, Bus, Truck
    vehicle_count = len(vehicles)

    decision = "Green" if vehicle_count < 5 else "Yellow" if vehicle_count < 10 else "Red"

    cv2.putText(frame, f"Vehicles: {vehicle_count} | Signal: {decision}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("YOLO Traffic Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
