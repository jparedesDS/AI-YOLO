import os
import shutil
import random

# Definir directorios
base_dir = 'CS2_CT_head_T_head/valid/new_data'

train_images_dir = os.path.join('CS2_CT_head_T_head/valid/images')
train_labels_dir = os.path.join('CS2_CT_head_T_head/valid/labels')
valid_images_dir = os.path.join('CS2_CT_head_T_head/valid/images')
valid_labels_dir = os.path.join('CS2_CT_head_T_head/valid/labels')

# Crear las carpetas de destino si no existen
os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(valid_images_dir, exist_ok=True)
os.makedirs(valid_labels_dir, exist_ok=True)

# Obtener lista de todos los archivos de la carpeta base
files = os.listdir(base_dir)

# Filtrar las imágenes y etiquetas
images = [f for f in files if f.endswith('.jpg')]
labels = [f for f in files if f.endswith('.txt')]

# Barajar la lista de imágenes
random.shuffle(images)

# Definir proporción de validación
valid_split = 0.2  # 20% de los datos para validación
valid_size = int(len(images) * valid_split)

# Dividir en conjuntos de validación y entrenamiento
valid_images = images[:valid_size]
train_images = images[valid_size:]


# Función para mover archivos correspondientes
def move_files(images_list, src_dir, dest_images_dir, dest_labels_dir):
    for image in images_list:
        # Mover la imagen
        shutil.move(os.path.join(src_dir, image), os.path.join(dest_images_dir, image))

        # Mover la etiqueta correspondiente
        label_file = image.replace('.jpg', '.txt')
        if label_file in files:
            shutil.move(os.path.join(src_dir, label_file), os.path.join(dest_labels_dir, label_file))


# Mover archivos de entrenamiento
move_files(train_images, base_dir, train_images_dir, train_labels_dir)

# Mover archivos de validación
move_files(valid_images, base_dir, valid_images_dir, valid_labels_dir)

print('Los datos han sido divididos y movidos correctamente.')
