from ultralytics import YOLO
import cv2

model = YOLO("best.pt")

results = model.predict(
    source="sample_images",
    conf=0.4,
    save=True
)

class_names = {
    0: "missing_hole",
    1: "short",
    2: "open_circuit"
}

for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])

        x1, y1, x2, y2 = box.xyxy[0]
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        area = (x2 - x1) * (y2 - y1)
        severity = "High" if area > 8000 else "Low"

        print(
            f"Defect: {class_names[cls_id]} | "
            f"Confidence: {conf:.2f} | "
            f"Center: ({cx}, {cy}) | "
            f"Severity: {severity}"
        )
