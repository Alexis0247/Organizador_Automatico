import os
import shutil
import sys

def organizar_aqui():
    """
    La aplicación ejecutable se encuentra en la carpeta "/dist"

    
    Función principal para organizar los archivos en el directorio actual.

    Clasifica los archivos por tipo de extensión y los mueve a una estructura
    de carpetas jerárquica: 'Categoria_Principal/Subcarpeta_Extension/archivo'.
    
    Ejemplo: un archivo 'informe.pdf' se movería a 'Documentos/PDF/informe.pdf'.
    """
    # 1. Obtener la ruta donde se encuentra el ejecutable o script
    if getattr(sys, 'frozen', False):
        # El atributo 'frozen' existe en el módulo 'sys' si el código se ha 
        # compilado en un ejecutable (ej. con PyInstaller, cx_Freeze).
        # En este caso, la ruta base es el directorio del ejecutable.
        # Si es un ejecutable (.exe)
        ruta_actual = os.path.dirname(sys.executable)
    else:
        # Si se ejecuta como un script (.py) normal, usamos la ruta del script.
        # os.path.abspath(__file__) obtiene la ruta completa del archivo actual.
        ruta_actual = os.path.dirname(os.path.abspath(__file__))
    
    # Nombre de este archivo para evitar moverlo.
    # Necesita lógica para script (.py) o ejecutable (.exe).
    nombre_este_archivo = os.path.basename(sys.executable if getattr(sys, 'frozen', False) else __file__)

    # 2. Definición del Diccionario de Categorías
    # Mapea las extensiones de archivo (claves) a las Categorías Principales (valores).
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

    # Cambiar el directorio de trabajo al directorio donde está el script/ejecutable.
    os.chdir(ruta_actual)

    # 3. Iteración y Movimiento de Archivos
    for archivo in os.listdir(ruta_actual):
        # Evitar mover carpetas o este mismo script/ejecutable
        if os.path.isdir(archivo) or archivo == nombre_este_archivo:
            continue


        # Separar nombre del archivo y su extensión.
        nombre, extension = os.path.splitext(archivo)
        # Normalizar la extensión a minúsculas para la búsqueda en el diccionario.
        ext_limpia = extension.lower()

        if ext_limpia: # Solo procesar archivos que tienen extensión (evita archivos sin nombre o con nombres extraños)
            # 4. Determinar Categoría y Ruta de Destino
            # .get(key, default) obtiene la Categoría Principal o "Otros" si no se encuentra.
            categoria_principal = categorias.get(ext_limpia, "Otros")

            # Subcarpeta será el nombre de la extensión en mayúsculas (ej: PDF, DOCX).
            subcarpeta = ext_limpia.replace(".", "").upper()

            # Construir la ruta completa de destino: 'Categoria_Principal/Subcarpeta_Extension'
            ruta_destino = os.path.join(categoria_principal, subcarpeta)

            # 5. Crear el Directorio de Destino
            # os.makedirs crea directorios recursivamente.
            # exist_ok=True evita errores si el directorio ya existe.
            os.makedirs(ruta_destino, exist_ok=True)
            
            # 6. Mover el Archivo
            try:
                # Mueve el archivo de la ruta actual a la ruta de destino.
                shutil.move(archivo, os.path.join(ruta_destino, archivo))
                print(f"✅ Movido: {archivo}")
            except Exception as e:
                # Manejo de errores (ej. permisos, archivo ya existe y no se puede sobrescribir)
                print(f"❌ Error moviendo {archivo}: {e}")

    print("\n✨ Carpeta organizada con éxito.")

if __name__ == "__main__":
    # Punto de entrada del script.
    organizar_aqui()