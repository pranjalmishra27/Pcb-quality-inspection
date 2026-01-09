
## Automated PCB Quality Inspection System

This project implements an automated visual inspection system
to detect and classify PCB defects using a YOLOv8 model.

### Defect Types
- Missing Hole
- Short Circuit
- Open Circuit

### Features
- Defect detection and localization
- Confidence score for each defect
- Pixel-level defect center coordinates
- Severity estimation

### Model
- YOLOv8 (Ultralytics)
- PCB Defect Dataset (Kaggle)

## Training Results (Quick Summary – 1 Minute Read)

| Metric    | Value  | Meaning |
|-----------|--------|---------|
| Precision | 98.6%  | Very few false detections |
| Recall    | 98.7%  | Almost all defects detected |
| mAP@50    | 99.3%  | Industry-grade accuracy |
| Classes   | 3      | Task requirement satisfied |
| Model     | YOLOv8n | Lightweight & fast |

These results demonstrate that the trained model achieves
high accuracy and reliability for PCB defect inspection.

### How to Run
```bash
python detect.py
