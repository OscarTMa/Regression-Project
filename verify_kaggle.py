import os

kaggle_config_path = os.path.expanduser("~/.config/kaggle")
if os.path.exists(kaggle_config_path):
    print("Contenido de ~/.config/kaggle:", os.listdir(kaggle_config_path))
else:
    print("No existe el directorio ~/.config/kaggle.")
