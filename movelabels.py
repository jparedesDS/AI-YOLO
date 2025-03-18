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
