# AI-YOLO

#### ALL my models YOLO11 for Metallurgical Companies
- YOLO11l: https://huggingface.co/jparedesDS/fluorescent-penetrant-inspection
- YOLO11x: https://huggingface.co/jparedesDS/welding-defects-detection

#### ALL my models YOLOv10 & YOLOv9 for Counter Strike 2 Object Detection
- YOLOv9c: https://huggingface.co/jparedesDS/cs2-yolov9c
- YOLOv10s: https://huggingface.co/jparedesDS/cs2-yolov10s
- YOLOv10m: https://huggingface.co/jparedesDS/cs2-yolov10m
- YOLOv10b: https://huggingface.co/jparedesDS/cs2-yolov10b
- 

#### ALL my models YOLOv10 & YOLO11 for Valorant Object Detection
- YOLOv10b: https://huggingface.co/jparedesDS/valorant-yolov10b
- YOLO11m: https://huggingface.co/jparedesDS/valorant-yolo11m
  
#### ALL my models YOLO11 for Deadlock Object Detection
- YOLO11l: https://huggingface.co/jparedesDS/deadlock-yolo11l

#### ALL my models YOLO11 for Overwatch 2 Object Detection
- YOLO11l: https://huggingface.co/jparedesDS/ow2-yolo11m

#### How to use
```
from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO(r'your_model.pt')

# Run inference on 'image.png' with arguments
model.predict(
    'image.png',
    save=True,
    device=0
    )
```
#### ALL models
https://huggingface.co/jparedesDS
