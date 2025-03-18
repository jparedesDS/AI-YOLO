import os
import shutil
import cv2
import numpy as np
from pathlib import Path
from ultralytics import YOLO

# Cargar tu propio modelo YOLO
model = YOLO('cs2-cv-yolo11l-1200epoch.pt')  # Reemplaza con tu modelo

# Ruta a las imágenes no etiquetadas:
directorio_imagenes = 'data-tf2/train/images'
# Directorio de salida para imágenes con nuevos labels
directorio_salida = 'data-tf2/train/labels'
os.makedirs(directorio_salida, exist_ok=True)
# Directorio de salida para imágenes sin labels
directorio_sin_labels = 'data-tf2/train/images_SINLABELS'
os.makedirs(directorio_sin_labels, exist_ok=True)
# Directorio de salida para etiquetas vacías
directorio_labels_sin_labels = 'data-tf2/train/labels_SINLABELS'
os.makedirs(directorio_labels_sin_labels, exist_ok=True)

# Función para guardar las pseudo-labels en formato YOLO
def guardar_labels_yolo(imagen, predicciones, directorio_salida):
    nombre_imagen = Path(imagen).stem
    with open(f"{directorio_salida}/{nombre_imagen}.txt", 'w') as f:
        for x1, y1, x2, y2, conf, clase in predicciones:
            if conf > 0.52:  # Solo guardar predicciones con alta confianza
                # Convertir las coordenadas a formato YOLO (normalizado)
                x_centro = (x1 + x2) / 2.0
                y_centro = (y1 + y2) / 2.0
                ancho = x2 - x1
                alto = y2 - y1

                # Normalizar usando el tamaño de la imagen
                img = cv2.imread(imagen)
                img_width = img.shape[1]
                img_height = img.shape[0]
                x_centro /= img_width
                y_centro /= img_height
                ancho /= img_width
                alto /= img_height

                # Guardar en formato YOLO .txt
                f.write(f"{int(clase)} {x_centro} {y_centro} {ancho} {alto}\n")

# Realizar inferencia en todas las imágenes no etiquetadas
for archivo_imagen in os.listdir(directorio_imagenes):
    img_path = os.path.join(directorio_imagenes, archivo_imagen)
    img = cv2.imread(img_path)

    # Realizar inferencia con el modelo YOLOvX
    resultados = model(img)

    # Extraer los valores de las cajas, confianza y clases
    boxes = resultados[0].boxes  # Obtenemos las cajas de predicción
    predicciones = []

    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()  # Coordenadas de la caja
        conf = box.conf.cpu().numpy()[0]  # Confianza de la predicción
        clase = box.cls.cpu().numpy()[0]  # Clase predicha
        predicciones.append([x1, y1, x2, y2, conf, clase])

    if len(predicciones) > 0:  # Si hay predicciones, guardamos las labels
        guardar_labels_yolo(img_path, predicciones, directorio_salida)
    else:  # Si no hay predicciones, movemos la imagen a la carpeta de imágenes sin labels
        shutil.move(img_path, os.path.join(directorio_sin_labels, archivo_imagen))

        # Crear un archivo .txt vacío y moverlo a la carpeta de labels sin labels
        nombre_imagen = Path(img_path).stem
        empty_label_path = os.path.join(directorio_labels_sin_labels, f"{nombre_imagen}.txt")
        open(empty_label_path, 'w').close()

print(f"Proceso completado. Imágenes sin labels movidas a {directorio_sin_labels}. Labels generados y guardados en {directorio_salida}.")