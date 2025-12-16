import os
import shutil
import sys

def organizar_aqui():
    # 1. Obtener la ruta donde se encuentra el ejecutable o script
    if getattr(sys, 'frozen', False):
        # Si es un ejecutable (.exe)
        ruta_actual = os.path.dirname(sys.executable)
    else:
        # Si es un script (.py)
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Nombre de este archivo para no moverlo
    nombre_este_archivo = os.path.basename(sys.executable if getattr(sys, 'frozen', False) else __file__)

    # 2. Diccionario extendido (el mismo que ya teníamos)
    categorias = {
        # --- Microsoft Office y Documentos ---
        ".pdf": "Documentos",
        ".doc": "Documentos",
        ".docx": "Documentos",
        ".ppt": "Documentos",
        ".pptx": "Documentos",
        ".xls": "Documentos",
        ".xlsx": "Documentos",
        ".odt": "Documentos", # OpenDocument Text
        ".ods": "Documentos", # OpenDocument Spreadsheet
        ".txt": "Documentos",
        ".rtf": "Documentos",
        
        
        # --- Imagenes y Fotografía ---
        ".jpg": "Imagenes",
        ".jpeg": "Imagenes",
        ".png": "Imagenes",
        ".gif": "Imagenes",
        ".webp": "Imagenes",
        ".svg": "Imagenes",
        ".ico": "Imagenes",
        ".tiff": "Imagenes",
        ".raw": "Imagenes", # Archivos de cámara sin procesar
        ".cr2": "Imagenes", # Canon RAW
        ".nef": "Imagenes", # Nikon RAW
        ".dng": "Imagenes",
        ".bmp": "Imagenes",
        
        # --- Videos ---
        ".mp4": "Videos",
        ".mov": "Videos",
        ".avi": "Videos",
        ".mkv": "Videos",
        ".wmv": "Videos",
        ".flv": "Videos",
        
        # --- Audio ---
        ".mp3": "Audio",
        ".wav": "Audio",
        ".flac": "Audio",
        ".aac": "Audio",
        ".ogg": "Audio",
        
        # --- Comprimidos y Ejecutables ---
        ".zip": "Comprimidos",
        ".rar": "Comprimidos",
        ".7z": "Comprimidos",
        ".iso": "Instaladores",
        ".exe": "Instaladores",
        ".msi": "Instaladores",
        ".dmg": "Instaladores", # Instaladores de Mac
        
        # --- Datos y Programación ---
        ".csv": "Datos y Programacion",
        ".json": "Datos y Programacion",
        ".xml": "Datos y Programacion",
        ".html": "Datos y Programacion",
        ".css": "Datos y Programacion",
        ".js": "Datos y Programacion",
        ".py": "Datos y Programacion",
        ".log": "Datos y Programacion",
        ".sql": "Datos y Programacion"
    }

    os.chdir(ruta_actual)

    for archivo in os.listdir(ruta_actual):
        # Evitar mover carpetas o este mismo script/ejecutable
        if os.path.isdir(archivo) or archivo == nombre_este_archivo:
            continue

        nombre, extension = os.path.splitext(archivo)
        ext_limpia = extension.lower()

        if ext_limpia: # Solo si tiene extensión
            categoria_principal = categorias.get(ext_limpia, "Otros")
            subcarpeta = ext_limpia.replace(".", "").upper()
            ruta_destino = os.path.join(categoria_principal, subcarpeta)

            os.makedirs(ruta_destino, exist_ok=True)
            
            try:
                shutil.move(archivo, os.path.join(ruta_destino, archivo))
                print(f"✅ Movido: {archivo}")
            except Exception as e:
                print(f"❌ Error moviendo {archivo}: {e}")

    print("\n✨ Carpeta organizada con éxito.")

if __name__ == "__main__":
    organizar_aqui()