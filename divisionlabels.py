import os
import shutil
import random

# Rutas
base_path = r"C:\Users\alejandro.berzal\Desktop\last\train"
images_path = os.path.join(base_path, "images")
labels_path = os.path.join(base_path, "labels")

# Crear carpetas para validación
valid_images = os.path.join(base_path, "valid", "images")
valid_labels = os.path.join(base_path, "valid", "labels")
os.makedirs(valid_images, exist_ok=True)
os.makedirs(valid_labels, exist_ok=True)

# Parámetro: porcentaje de imágenes para validación
valid_ratio = 0.20  # 15% para valid

# Obtener lista de imágenes y etiquetas
images = sorted([f for f in os.listdir(images_path) if f.endswith((".jpg", ".png"))])
labels = sorted([f for f in os.listdir(labels_path) if f.endswith(".txt")])

# Asegurar que cada imagen tenga su etiqueta correspondiente
paired_data = [(img, img.replace(".jpg", ".txt").replace(".png", ".txt")) for img in images if img.replace(".jpg", ".txt").replace(".png", ".txt") in labels]

# Mezclar aleatoriamente y seleccionar el porcentaje para validación
random.shuffle(paired_data)
num_valid = int(len(paired_data) * valid_ratio)
valid_samples = paired_data[:num_valid]  # Extraer muestras para validación

# Mover archivos seleccionados a valid/
for img, lbl in valid_samples:
    shutil.move(os.path.join(images_path, img), os.path.join(valid_images, img))
    shutil.move(os.path.join(labels_path, lbl), os.path.join(valid_labels, lbl))

print(f"✅ Se movieron {num_valid} imágenes a validación.")
print(f"Train ahora tiene {len(paired_data) - num_valid} imágenes.")
