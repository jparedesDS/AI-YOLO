import os

# Directorio que contiene los archivos .txt con las etiquetas
dir_path = r"C:\Users\alejandro.berzal\Desktop\last\train\labels"

# Mapea los labels originales a los nuevos labels
label_map = {0: 0, 1: 1, 2: 0, 3: 1}

# Itera sobre cada archivo en el directorio
for filename in os.listdir(dir_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(dir_path, filename)

        # Lista para almacenar las nuevas líneas
        new_lines = []

        # Abre el archivo y procesa las etiquetas
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split()
                label = int(parts[0])

                # Filtra los labels que deseas eliminar (0 y 2)
                if label in label_map:
                    # Reasigna el label y guarda la línea actualizada
                    new_label = label_map[label]
                    new_line = f"{new_label} " + " ".join(parts[1:]) + "\n"
                    new_lines.append(new_line)

        # Sobrescribe el archivo con las nuevas etiquetas
        with open(file_path, "w") as file:
            file.writelines(new_lines)
