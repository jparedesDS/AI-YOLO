import os
import cv2
import numpy as np
from pathlib import Path
import shutil

# Directorios
directorio_imagenes = 'CS2_CT_head_T_head/valid/images'
directorio_labels = 'CS2_CT_head_T_head/valid/labels'
directorio_modificado = 'CS2_CT_head_T_head/valid/new_data'
directorio_sin_etiquetas = 'CS2_CT_head_T_head/valid/nolabels'

# Crear directorios si no existen
if not os.path.exists(directorio_modificado):
    os.makedirs(directorio_modificado)
if not os.path.exists(directorio_sin_etiquetas):
    os.makedirs(directorio_sin_etiquetas)


# Función para ajustar contraste
def ajustar_contraste(imagen, factor_contraste):
    return cv2.convertScaleAbs(imagen, alpha=factor_contraste, beta=0)


# Leer etiquetas desde un archivo
def leer_etiquetas(ruta_etiqueta):
    etiquetas = []
    with open(ruta_etiqueta, 'r') as file:
        for linea in file:
            # Ignorar líneas vacías
            if not linea.strip():
                continue
            # Intentar descomponer la línea
            partes = linea.strip().split()
            if len(partes) != 5:
                print(f"Formato incorrecto en la línea: {linea.strip()}. Se ignorará.")
                continue
            clase, x, y, w, h = map(float, partes)
            etiquetas.append([int(clase), x, y, w, h])
    return etiquetas


# Escribir etiquetas a un archivo
def escribir_etiquetas(ruta_etiqueta, etiquetas):
    with open(ruta_etiqueta, 'w') as file:
        for etiqueta in etiquetas:
            file.write(f"{etiqueta[0]} {etiqueta[1]:.6f} {etiqueta[2]:.6f} {etiqueta[3]:.6f} {etiqueta[4]:.6f}\n")


# Procesar todas las imágenes
for archivo_imagen in os.listdir(directorio_imagenes):
    img_path = os.path.join(directorio_imagenes, archivo_imagen)
    label_path = os.path.join(directorio_labels, f"{Path(archivo_imagen).stem}.txt")

    if not os.path.exists(label_path):
        print(f"No se encontró la etiqueta correspondiente para la imagen {archivo_imagen}. Moviendo a nolabels.")
        shutil.move(img_path, os.path.join(directorio_sin_etiquetas, archivo_imagen))
        continue

    imagen = cv2.imread(img_path)
    if imagen is None:
        print(f"No se pudo cargar la imagen {archivo_imagen}.")
        continue

    etiquetas = leer_etiquetas(label_path)
    print(f"Procesando imagen: {archivo_imagen}")

    # Ajuste de contraste y volteo vertical
    for contraste in [0.5, 1.0, 1.7]:
        # Ajustar contraste
        imagen_contraste = ajustar_contraste(imagen, contraste)

        # Aplicar flip vertical
        imagen_volteada_h = cv2.flip(imagen_contraste, 1)
        etiquetas_volteadas_h = [[clase, 1 - x, y, w, h] for clase, x, y, w, h in etiquetas]

        # Guardar imagen modificada y etiquetas
        output_img_path = os.path.join(directorio_modificado,
                                       f"{Path(archivo_imagen).stem}_contraste{contraste}_flipH.jpg")
        output_label_path = os.path.join(directorio_modificado,
                                         f"{Path(archivo_imagen).stem}_contraste{contraste}_flipH.txt")
        cv2.imwrite(output_img_path, imagen_volteada_h)
        escribir_etiquetas(output_label_path, etiquetas_volteadas_h)

    print("YOLO! (¡Guardada con éxito!)")

print("EXITO.")








"""import os
import cv2
import numpy as np
from pathlib import Path
import shutil

# Directorios
directorio_imagenes = 'zz data_v1_old/00datasets/99zip/CS2_CV/valid/images'
directorio_labels = 'zz data_v1_old/00datasets/99zip/CS2_CV/valid/labels'
directorio_modificado = 'zz data_v1_old/00datasets/99zip/CS2_CV/valid/new_data'
directorio_sin_etiquetas = 'zz data_v1_old/00datasets/99zip/CS2_CV/valid/nolabels'

# Crear directorios si no existen
os.makedirs(directorio_modificado, exist_ok=True)
os.makedirs(directorio_sin_etiquetas, exist_ok=True)

# Función para ajustar contraste
def ajustar_contraste(imagen, factor_contraste):
    return cv2.convertScaleAbs(imagen, alpha=factor_contraste, beta=0)

# Función para aplicar desenfoque
def aplicar_desenfoque(imagen, tipo='gaussian', nivel=5):
    if tipo == 'gaussian':
        return cv2.GaussianBlur(imagen, (nivel, nivel), 0)

# Leer etiquetas desde un archivo
def leer_etiquetas(ruta_etiqueta):
    etiquetas = []
    with open(ruta_etiqueta, 'r') as file:
        for linea in file:
            # Ignorar líneas vacías
            if not linea.strip():
                continue
            # Intentar descomponer la línea
            partes = linea.strip().split()
            if len(partes) != 5:
                print(f"Formato incorrecto en la línea: {linea.strip()}. Se ignorará.")
                continue
            clase, x, y, w, h = map(float, partes)
            etiquetas.append([int(clase), x, y, w, h])
    return etiquetas

# Escribir etiquetas a un archivo
def escribir_etiquetas(ruta_etiqueta, etiquetas):
    with open(ruta_etiqueta, 'w') as file:
        for etiqueta in etiquetas:
            file.write(f"{etiqueta[0]} {etiqueta[1]:.6f} {etiqueta[2]:.6f} {etiqueta[3]:.6f} {etiqueta[4]:.6f}\n")

# Procesar todas las imágenes
for archivo_imagen in os.listdir(directorio_imagenes):
    img_path = os.path.join(directorio_imagenes, archivo_imagen)
    label_path = os.path.join(directorio_labels, f"{Path(archivo_imagen).stem}.txt")

    if not os.path.exists(label_path):
        print(f"No se encontró la etiqueta correspondiente para la imagen {archivo_imagen}. Moviendo a nolabels.")
        shutil.move(img_path, os.path.join(directorio_sin_etiquetas, archivo_imagen))
        continue

    imagen = cv2.imread(img_path)
    if imagen is None:
        print(f"No se pudo cargar la imagen {archivo_imagen}.")
        continue

    etiquetas = leer_etiquetas(label_path)
    print(f"Procesando imagen: {archivo_imagen}")

    # Ajuste de contraste y flip
    for contraste in [0.5, 1.7]:
        # Ajustar contraste
        imagen_contraste = ajustar_contraste(imagen, contraste)

        # Aplicar flip vertical y horizontal
        for flip, direccion in [(0, 'V'), (1, 'H')]:
            imagen_volteada = cv2.flip(imagen_contraste, flip)
            if flip == 0:  # Flip vertical
                etiquetas_volteadas = [[clase, x, 1 - y, w, h] for clase, x, y, w, h in etiquetas]
            else:  # Flip horizontal
                etiquetas_volteadas = [[clase, 1 - x, y, w, h] for clase, x, y, w, h in etiquetas]

            # Guardar imagen modificada y etiquetas
            output_img_path = os.path.join(directorio_modificado,
                                            f"{Path(archivo_imagen).stem}_contraste{contraste}_flip{direccion}.jpg")
            output_label_path = os.path.join(directorio_modificado,
                                              f"{Path(archivo_imagen).stem}_contraste{contraste}_flip{direccion}.txt")
            cv2.imwrite(output_img_path, imagen_volteada)
            escribir_etiquetas(output_label_path, etiquetas_volteadas)

        # Aplicar desenfoque
        for nivel in [5, 9]:  # Diferentes niveles de desenfoque
            imagen_desenfocada = aplicar_desenfoque(imagen_contraste, 'gaussian', nivel)
            output_img_path_blur = os.path.join(directorio_modificado,
                                                 f"{Path(archivo_imagen).stem}_contraste{contraste}_blur{nivel}.jpg")
            output_label_path_blur = os.path.join(directorio_modificado,
                                                   f"{Path(archivo_imagen).stem}_contraste{contraste}_blur{nivel}.txt")
            cv2.imwrite(output_img_path_blur, imagen_desenfocada)
            escribir_etiquetas(output_label_path_blur, etiquetas)

    print("YOLO! (¡Guardada con éxito!)")

print("EXITO.")
"""