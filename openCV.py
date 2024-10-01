import os
import cv2
import numpy as np
from pathlib import Path

# Directorios
directorio_imagenes = 'data/train/images'
directorio_modificado = 'data/train/new_data'

# Crear directorio si no existe
if not os.path.exists(directorio_modificado):
    os.makedirs(directorio_modificado)

# Función para ajustar brillo
def ajustar_brillo(imagen, valor_brillo):
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, valor_brillo)
    v = np.clip(v, 0, 255)
    imagen_brillante = cv2.merge((h, s, v))
    return cv2.cvtColor(imagen_brillante, cv2.COLOR_HSV2BGR)

# Función para ajustar contraste
def ajustar_contraste(imagen, factor_contraste):
    return cv2.convertScaleAbs(imagen, alpha=factor_contraste, beta=0)

# Procesar todas las imágenes
for archivo_imagen in os.listdir(directorio_imagenes):
    img_path = os.path.join(directorio_imagenes, archivo_imagen)
    imagen = cv2.imread(img_path)

    if imagen is None:
        print(f"No se pudo cargar la imagen {archivo_imagen}.")
        continue

    # Ajuste de contraste + Gaussian Blur
    for contraste in [0.5, 2]:
        # Aplicar ajuste de contraste
        imagen_contraste = ajustar_contraste(imagen, contraste)
        # Aplicar Gaussian Blur a la imagen con contraste ajustado
        imagen_contraste_blur = cv2.GaussianBlur(imagen_contraste, (5, 5), 0)
        output_img_path = os.path.join(directorio_modificado, f"{Path(archivo_imagen).stem}_contraste{contraste}_gaussianBlur.jpg")
        cv2.imwrite(output_img_path, imagen_contraste_blur)

    # Volteo horizontal
    #imagen_volteada_h = cv2.flip(imagen, 1)
    #cv2.imwrite(os.path.join(directorio_modificado, f"{Path(archivo_imagen).stem}_flipH.jpg"), imagen_volteada_h)

    # Gaussian Blur sin contraste (opcional)
    #imagen_gaussian = cv2.GaussianBlur(imagen, (5, 5), 0)
    #cv2.imwrite(os.path.join(directorio_modificado, f"{Path(archivo_imagen).stem}_gaussianBlur.jpg"), imagen_gaussian)

    print(f"Imagen modificada: {archivo_imagen}... YOLOTIME!!!")

print(f"ÉXITO")
