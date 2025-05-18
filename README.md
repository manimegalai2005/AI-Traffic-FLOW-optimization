# 🚦 AI Traffic Flow Optimization

An AI-based traffic flow optimization system using Python. This project uses computer vision and basic object detection to analyze traffic and suggest real-time signal control decisions.

---

## 🧠 Features

- Static image-based traffic density analysis
- Real-time video processing via webcam or video file
- Vehicle detection using YOLOv8 (Ultralytics)
- Python-only implementation (no external frameworks)

---

## 📂 Project Structure

ai_traffic_optimization/
├── main.py # Analyze a static traffic image
├── real_time.py # Real-time video-based traffic analysis
├── yolo_vehicle_detect.py # YOLOv8 vehicle detection from video
├── traffic_optimizer.py # Traffic signal decision logic
├── data/
│ ├── traffic_sample.jpg # Sample traffic image
│ └── traffic_video.mp4 # Sample traffic video
└── README.md # Project overview

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Install Dependencies

Run this to install required Python libraries:

```bash
pip install opencv-python scikit-image scikit-learn ultralytics numpy
Make sure you're using Python 3.12 or 3.13.

▶️ How to Run
Static Image Analysis
bash
Copy
Edit
python main.py
Real-Time Video Analysis
bash
Copy
Edit
python real_time.py
YOLO Vehicle Detection
bash
Copy
Edit
python yolo_vehicle_detect.py
Press Q to quit the video window.

🖼️ Sample Media
Place your files like this:

data/traffic_sample.jpg — any road image

data/traffic_video.mp4 — traffic or intersection video

You can download free media from Pexels or Pixabay.

📌 Notes
YOLOv8 model (yolov8n.pt) is auto-downloaded by Ultralytics when first used.

All code is written in pure Python — no Flask, Django, or external GUIs.

👨‍💻 Author
Created by [G.Rishika]
[ GitHub Profile: Rishika112023243026]

📄 License
Open-source project available under the MIT License.

yaml
Copy
Edit

---

Let me know if you'd like:
- A new `requirements.txt` auto-generated from your environment
- A PDF report, PowerPoint presentation, or GUI app version of this project