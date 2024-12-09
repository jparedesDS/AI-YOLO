# AI-YOLO  
**All my YOLO-based models for various applications**  

## Table of Contents  
- [Overview](#overview)  
- [Metallurgical Applications](#metallurgical-applications)  
- [Counter-Strike 2 Object Detection](#counter-strike-2-object-detection)  
- [Valorant Object Detection](#valorant-object-detection)  
- [Deadlock Object Detection](#deadlock-object-detection)  
- [Overwatch 2 Object Detection](#overwatch-2-object-detection)
- [Fortnite Object Detection](#fortnite-object-detection) 
- [How to Use the Models](#how-to-use-the-models)  
- [All Models](#all-models)  

---

## Overview  
This repository showcases my YOLO models, customized for diverse applications, including industrial, gaming, and general object detection tasks. From metallurgical inspections to in-game object detection, these models leverage cutting-edge deep learning to achieve high precision.  

---

## Metallurgical Applications  
### Fluorescent Penetrant Inspection  
- **Model**: YOLO11l  
- **Details**: Optimized for detecting defects in fluorescent penetrant inspections.  
- [Access Model on Hugging Face](https://huggingface.co/jparedesDS/fluorescent-penetrant-inspection)  

### Welding Defects Detection  
- **Model**: YOLO11x  
- **Details**: Designed to identify welding defects with high accuracy.  
- [Access Model on Hugging Face](https://huggingface.co/jparedesDS/welding-defects-detection)  

---

## Counter-Strike 2 Object Detection  
YOLO models tailored for detecting objects and events in Counter-Strike 2.  

- **YOLOv9c**: [Hugging Face Link](https://huggingface.co/jparedesDS/cs2-yolov9c)  
- **YOLOv10s**: [Hugging Face Link](https://huggingface.co/jparedesDS/cs2-yolov10s)  
- **YOLOv10m**: [Hugging Face Link](https://huggingface.co/jparedesDS/cs2-yolov10m)  
- **YOLOv10b**: [Hugging Face Link](https://huggingface.co/jparedesDS/cs2-yolov10b)  

---

## Valorant Object Detection  
Models designed to detect in-game objects in Valorant.  

- **YOLOv10b**: [Hugging Face Link](https://huggingface.co/jparedesDS/valorant-yolov10b)  
- **YOLO11m**: [Hugging Face Link](https://huggingface.co/jparedesDS/valorant-yolo11m)  

---

## Deadlock Object Detection  
Custom YOLO models for detecting objects in **Deadlock**.  

- **YOLO11l**: [Hugging Face Link](https://huggingface.co/jparedesDS/deadlock-yolo11l)  

---

## Overwatch 2 Object Detection  
Advanced object detection for Overwatch 2.  

- **YOLO11m**: [Hugging Face Link](https://huggingface.co/jparedesDS/ow2-yolo11m)  

---

## Fortnite Object Detection  
Advanced object detection for Fortnite.  

- **YOLO11m**: [Hugging Face Link](https://huggingface.co/jparedesDS/fortnite-yolo11m)

---

## How to Use the Models  
Easily integrate the models into your projects using the `ultralytics` library.  

```python  
from ultralytics import YOLO  

# Load a pretrained YOLO model  
model = YOLO(r'your_model.pt')  

# Run inference on an image  
model.predict(  
    'image.png',  
    save=True,  
    device=0  
)  
```

## All Models
You can find all my models on Hugging Face:
https://huggingface.co/jparedesDS

## Contributing
If you'd like to contribute, feel free to open an issue or submit a pull request.

## License
This repository is licensed under the MIT License. See the LICENSE file for details.
