# 📂 File Organizer Pro (Python Utility)

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Este es un script de automatización desarrollado en **Python** diseñado para organizar directorios saturados de forma instantánea. Es ideal para mantener carpetas como "Descargas" o "Escritorio" perfectamente ordenadas mediante una clasificación jerárquica.



## 🚀 Funcionalidades Principales

- **Clasificación Multicapa:** No solo agrupa por tipo (Documentos, Imágenes), sino que crea subcarpetas específicas para cada extensión (PDF, JPG, PNG).
- **Compatibilidad con Ejecutables:** Preparado para funcionar como script `.py` o como archivo `.exe` (detecta la ruta base incluso si está compilado).
- **Seguridad de Archivos:** Incluye una lógica de exclusión para no mover el propio script o carpetas ya existentes.
- **Manejo de Errores:** Sistema de excepciones para evitar interrupciones si un archivo está en uso o tiene permisos restringidos.

## 🛠️ Estructura de Organización

El script organiza los archivos siguiendo este patrón de directorios:
`Categoría Principal / EXTENSIÓN EN MAYÚSCULAS / archivo.ext`

| Categoría | Extensiones Soportadas (Ejemplos) |
| :--- | :--- |
| **Documentos** | .pdf, .docx, .xlsx, .txt, .pptx |
| **Imágenes** | .jpg, .png, .raw, .cr2, .nef (Fotografía Profesional) |
| **Programación** | .py, .js, .html, .json, .sql, .csv |
| **Multimedia** | .mp4, .mkv, .mp3, .wav, .flac |
| **Otros** | Cualquier extensión no definida en el diccionario |

## 📦 Instalación y Uso

1. **Requisitos:** Tener instalado [Python 3.x](https://www.python.org/).
2. **Descarga:** Clona este repositorio o descarga el archivo `organizador.py`.
3. **Ejecución:**
   ```bash
   python organizador.py
