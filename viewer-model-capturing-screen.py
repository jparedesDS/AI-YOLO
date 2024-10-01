import cv2
import numpy as np
import pyautogui
from ultralytics import YOLO

model = YOLO('hsxhito_1200epoch_withparams.pt')

x = (1920 - 640) // 2
y = (1080 - 640) // 2

def detect_objects(frame):
    copyframe = frame[y:y+640, x:x+640, :]
    results = model(copyframe)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            class_id = box.cls[0]
            class_name = model.names[int(class_id)]
            confidence = box.conf
            confidence_str = str(confidence.item())

            if class_name == "enemyBody" or class_name == "enemyHead":
            #or class_name == "CT_head" or class_name == "T_head" or class_name == "head":
            #if class_name != "none":
                coordinates = (box.xyxy).tolist()[0]
                left, top, right, bottom = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
                cv2.rectangle(frame, (int(left+x), int(top+y) ), (int(right+x), int(bottom+y)), (255, 0, 0) if class_name == "t_head" else (0, 255, 0), 2)
                cv2.putText(frame, class_name + " " + confidence_str, (int(left+x), int(top+y)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)
                cv2.imshow('window', frame)

    return frame

def capture_screen():
    # Capture the screen
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame


while True:
    frame = capture_screen()
    frame = detect_objects(frame)
    cv2.imshow("window", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
