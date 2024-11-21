import os
import streamlit as st

def tree(directory, output_file, level=0):
    """
    Recorre recursivamente un directorio y guarda la estructura en un archivo.
    
    Args:
    - directory: Directorio raíz a explorar.
    - output_file: Archivo donde se almacenará la estructura.
    - level: Nivel actual de profundidad (usado internamente).
    """
    try:
        files = os.listdir(directory)
    except PermissionError:
        # Si no se tienen permisos para listar el directorio
        output_file.write("  " * level + f"|-- [Access Denied] {directory}\n")
        return

    for file in files:
        path = os.path.join(directory, file)
        output_file.write("  " * level + f"|-- {file}\n")
        if os.path.isdir(path):
            tree(path, output_file, level + 1)

# Archivo principal para ejecutar
if __name__ == "__main__":
    root_dir = os.path.expanduser("~")
    output_file_path = os.path.join(root_dir, "file_structure.txt")
    
    with open(output_file_path, "w") as f:
        f.write(f"Estructura de directorios bajo: {root_dir}\n")
        f.write("=" * 40 + "\n")
        tree(root_dir, f)
    
    print(f"Estructura guardada en: {output_file_path}")
 
    ########

    file_path = "/home/appuser/file_structure.txt"

    with open(file_path, "rb") as f:
         st.download_button(
             label="Descargar file_structure.txt",
             data=f,
             file_name="file_structure.txt",
             mime="text/plain",
         )

