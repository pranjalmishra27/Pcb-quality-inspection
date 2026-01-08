
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

### How to Run
```bash
python detect.py
