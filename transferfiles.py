import cv2
import os
from pathlib import Path
import shutil

"""# Directorio de imágenes y etiquetas
directorio_imagenes = 'dataset/train/new_data'  # Carpeta de imágenes
directorio_labels = 'dataset/train/new_labels'  # Carpeta de etiquetas
directorio_sin_label = 'dataset/train/nolabelsinlabel/'  # Carpeta para imágenes y etiquetas sin labels

# Crear la carpeta 'nolabels' si no existe
os.makedirs(directorio_sin_label, exist_ok=True)

# Procesar todas las imágenes y etiquetas
for archivo_imagen in os.listdir(directorio_imagenes):
    img_path = os.path.join(directorio_imagenes, archivo_imagen)
    label_path = os.path.join(directorio_labels, Path(archivo_imagen).stem + '.txt')

    # Verificar si el archivo de etiqueta existe
    if os.path.exists(label_path):
        # Leer el archivo de etiqueta
        with open(label_path, 'r') as f:
            labels = f.readlines()

        # Si el archivo de etiqueta está vacío o no contiene etiquetas, mover imagen y label
        if len(labels) == 0:
            print(f"Moviéndo {archivo_imagen} y su label correspondiente a la carpeta 'nolabels'")
            shutil.move(img_path, os.path.join(directorio_sin_label, archivo_imagen))
            shutil.move(label_path, os.path.join(directorio_sin_label, Path(label_path).name))
    else:
        # Si no existe el archivo de etiqueta, mover solo la imagen
        print(f"No se encontró el label para {archivo_imagen}, moviendo a la carpeta 'nolabels'")
        shutil.move(img_path, os.path.join(directorio_sin_label, archivo_imagen))

print("Proceso completo. Las imágenes y etiquetas sin labels han sido movidas a la carpeta 'nolabels'.")
"""

import os
import shutil

# Directorio de origen que contiene los archivos .txt
directorio_origen = 'data/valid/new_data'

# Directorio de destino para los archivos .txt
directorio_destino = 'data/valid/labels'

# Crear el directorio de destino si no existe
os.makedirs(directorio_destino, exist_ok=True)

# Mover archivos .txt de la carpeta de origen a la carpeta de destino
for archivo in os.listdir(directorio_origen):
    if archivo.endswith('.txt'):
        origen = os.path.join(directorio_origen, archivo)
        destino = os.path.join(directorio_destino, archivo)
        shutil.move(origen, destino)
        print(f'Movido: {origen} a {destino}')

print("Todos los archivos .txt han sido movidos.")
