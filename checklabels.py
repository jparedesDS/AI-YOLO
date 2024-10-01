import os
import cv2
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# Directorios de imágenes y etiquetas
directorio_imagenes = 'test/images'
directorio_labels = 'test/labels'

# Diccionario para las clases (ajústalo según tus clases)
clases = {0:'CT_head', 1:'T_head'}  # Ajusta esto según tus clases

def visualizar_labels_en_imagen(imagen_path, label_path):
    # Leer la imagen
    img = cv2.imread(imagen_path)
    if img is None:
        print(f"No se pudo cargar la imagen: {imagen_path}")
        return

    img_height, img_width = img.shape[:2]

    # Leer el archivo de etiquetas
    with open(label_path, 'r') as f:
        labels = f.readlines()

    if not labels:
        print(f"No hay etiquetas en el archivo: {label_path}")
        return

    # Dibujar cada etiqueta en la imagen
    for label in labels:
        try:
            clase_id, x_centro, y_centro, ancho, alto = map(float, label.split())

            # Desnormalizar las coordenadas y dimensiones (convertir a píxeles)
            x_centro *= img_width
            y_centro *= img_height
            ancho *= img_width
            alto *= img_height

            # Obtener las esquinas del bounding box
            x1 = int(x_centro - ancho / 2)
            y1 = int(y_centro - alto / 2)
            x2 = int(x_centro + ancho / 2)
            y2 = int(y_centro + alto / 2)

            # Dibujar el bounding box en la imagen
            color = (0, 255, 0)  # Verde
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

            # Añadir el nombre de la clase
            text = clases[int(clase_id)]
            cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        except ValueError:
            print(f"Error al leer una etiqueta en el archivo: {label_path}")
            continue

    # Mostrar la imagen con los bounding boxes usando matplotlib
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Imagen con Labels")
    plt.axis('off')
    plt.show()

# Procesar todas las imágenes y etiquetas
for archivo in os.listdir(directorio_imagenes):
    if archivo.endswith(('.jpg', '.png')):  # Puedes ajustar según el formato de tus imágenes
        img_path = os.path.join(directorio_imagenes, archivo)
        label_path = os.path.join(directorio_labels, Path(archivo).stem + '.txt')

        if os.path.exists(label_path):
            visualizar_labels_en_imagen(img_path, label_path)
        else:
            print(f"No se encontró etiqueta para {archivo}")


"""
import os
import cv2
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# Directorio de imágenes y etiquetas (misma carpeta)
directorio = 'CS2_CT_head_T_head/valid/new_data'

# Diccionario para las clases (ajústalo según tus clases)
clases = {0: 'CT_head', 1: 'T_head'}  # Ajusta esto según tus clases

def visualizar_labels_en_imagen(imagen_path, label_path):
    img = cv2.imread(imagen_path)
    img_height, img_width = img.shape[:2]

    # Leer el archivo de etiquetas
    with open(label_path, 'r') as f:
        labels = f.readlines()

    # Dibujar cada etiqueta en la imagen
    for label in labels:
        clase_id, x_centro, y_centro, ancho, alto = map(float, label.split())

        # Desnormalizar las coordenadas y dimensiones (convertir a píxeles)
        x_centro *= img_width
        y_centro *= img_height
        ancho *= img_width
        alto *= img_height

        # Obtener las esquinas del bounding box
        x1 = int(x_centro - ancho / 2)
        y1 = int(y_centro - alto / 2)
        x2 = int(x_centro + ancho / 2)
        y2 = int(y_centro + alto / 2)

        # Dibujar el bounding box en la imagen
        color = (0, 255, 0)  # Verde
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

        # Añadir el nombre de la clase
        text = clases[int(clase_id)]
        cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Mostrar la imagen con los bounding boxes usando matplotlib
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Imagen con Labels")
    plt.axis('off')
    plt.show()

# Procesar todas las imágenes y etiquetas
for archivo in os.listdir(directorio):
    if archivo.endswith('.jpg') or archivo.endswith('.png'):  # Puedes ajustar según el formato de tus imágenes
        img_path = os.path.join(directorio, archivo)
        label_path = os.path.join(directorio, Path(archivo).stem + '.txt')

        if os.path.exists(label_path):
            visualizar_labels_en_imagen(img_path, label_path)
        else:
            print(f"No se encontró etiqueta para {archivo}")"""