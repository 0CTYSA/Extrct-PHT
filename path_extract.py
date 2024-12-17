import pandas as pd
from urllib.parse import urlparse
from tkinter import Tk, filedialog

# Función para extraer el path de una URL


def extract_path_from_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    folders = [folder for folder in path.split(
        "/") if folder]  # Solo carpetas no vacías
    return folders

# Función principal


def process_urls_from_excel(output_txt):
    # Ventana para seleccionar archivo
    Tk().withdraw()  # Ocultar la ventana principal de tkinter
    input_excel = filedialog.askopenfilename(
        title="Selecciona el archivo Excel",
        filetypes=[("Excel files", "*.xlsx *.xls")]
    )

    if not input_excel:
        print("No se seleccionó ningún archivo. Saliendo...")
        return

    print(f"Archivo seleccionado: {input_excel}")

    # Leer el archivo Excel
    try:
        df = pd.read_excel(input_excel)
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return

    # Verificar que las columnas necesarias existan
    if "Company" not in df.columns or "URL" not in df.columns:
        print("El archivo Excel debe contener las columnas 'Company' y 'URL'.")
        return

    # Crear un diccionario para almacenar resultados por compañía
    results = {}

    # Iterar sobre cada fila
    for _, row in df.iterrows():
        company = row["Company"]
        url = row["URL"]

        # Extraer el path
        paths = extract_path_from_url(url)

        # Añadir los paths al diccionario
        if company not in results:
            results[company] = []
        results[company].extend(paths)

    # Escribir los resultados en un archivo de texto
    with open(output_txt, "w") as file:
        for company, paths in results.items():
            unique_paths = list(set(paths))  # Evitar duplicados
            file.write(f"Company: {company}\n")
            file.write(f"Count path: {len(unique_paths)}\n")
            file.write("List of Path:\n")
            for path in unique_paths:
                file.write(f"- {path}\n")
            file.write("\n")

    print(f"Resultados guardados en '{output_txt}'.")


# Parámetro de salida
output_txt = "results.txt"  # Archivo de salida

# Ejecutar el procesamiento
process_urls_from_excel(output_txt)
