import os
from pathlib import Path

# Directorios de imágenes y etiquetas
directorio_imagenes = r'C:\Users\alejandro.berzal\Desktop\CS2_04-03-2025\valid\images'
directorio_labels = r'C:\Users\alejandro.berzal\Desktop\CS2_04-03-2025\valid\labels'

# Inicializar los contadores para cada clase y los fondos
class_count = {}
background_count = 0

# Procesar todas las imágenes y etiquetas
for imagen_file in os.listdir(directorio_imagenes):
    if imagen_file.endswith(('.jpg', '.png')):  # Puedes ajustar según el formato de tus imágenes
        # Ruta de la imagen y de la etiqueta correspondiente
        img_path = os.path.join(directorio_imagenes, imagen_file)
        label_path = os.path.join(directorio_labels, Path(imagen_file).stem + '.txt')

        if os.path.exists(label_path):
            # Leer el archivo de etiquetas
            with open(label_path, 'r') as f:
                lines = f.readlines()
                if lines:
                    # Contar las instancias de cada clase
                    for line in lines:
                        class_id = int(line.split()[0])
                        if class_id in class_count:
                            class_count[class_id] += 1
                        else:
                            class_count[class_id] = 1
                else:
                    # Si el archivo de etiquetas está vacío, considerarlo como fondo
                    background_count += 1
        else:
            # Si no hay archivo de etiqueta, contar la imagen como fondo
            background_count += 1

# Imprimir los resultados
for class_id, count in class_count.items():
    print(f'Clase {class_id}: {count} instancias')

print(f'Fondos (imágenes sin etiquetas): {background_count} instancias')