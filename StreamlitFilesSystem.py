import os
import streamlit as st

def list_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

st.title("Explorando el sistema de archivos en Streamlit Cloud")

root_dir = os.path.expanduser("~")
st.write(f"Estructura de directorios bajo: {root_dir}")
files = list_files(root_dir)
st.write("\n".join(files))
