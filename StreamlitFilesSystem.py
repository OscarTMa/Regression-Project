import os

def tree(directory, level=0):
    files = os.listdir(directory)
    for file in files:
        path = os.path.join(directory, file)
        print("  " * level + f"|-- {file}")
        if os.path.isdir(path):
            tree(path, level + 1)

# Especifica el directorio a explorar (por ejemplo, raíz del usuario)
print("Estructura del directorio principal:")
tree(os.path.expanduser("~"))
