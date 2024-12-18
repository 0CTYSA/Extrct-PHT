# Extractor de Paths desde URLs

Este script en Python permite procesar un archivo de Excel que contiene columnas con nombres de empresas (Company) y URLs, para extraer las rutas (paths) de las URLs y organizarlas por empresa en un archivo de texto de salida. Además, incluye un conteo de los paths únicos detectados por cada empresa.

## Características

- **Lectura desde Excel**: Permite seleccionar un archivo de Excel con las columnas `Company` y `URL`.
- **Extracción de paths**: Extrae los paths de las URLs proporcionadas.
- **Organización por empresa**: Agrupa los paths extraídos por cada empresa.
- **Eliminación de duplicados**: Asegura que los paths listados sean únicos.
- **Resultados claros**: Genera un archivo de texto con un formato amigable que incluye:
  - Nombre de la empresa.
  - Cantidad de paths únicos detectados.
  - Lista de paths.

## Requisitos

1. Python 3.x instalado.
2. Librerías necesarias:
   - `pandas`
   - `openpyxl`
   - `tkinter` (incluida por defecto en Python).

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install pandas openpyxl
```

## Archivos incluidos

- **script.py**: Contiene el código principal del proyecto.
- **results.txt**: Archivo de salida generado con los resultados procesados.

## Formato esperado del archivo Excel

El archivo de Excel debe contener las siguientes columnas:

| Company  | URL                              |
| -------- | -------------------------------- |
| EmpresaA | https://example.com/folder1/page |
| EmpresaB | https://site.com/path1/path2     |
| EmpresaA | https://example.com/folder2      |
| EmpresaB | https://site.com/anotherpath     |

## Cómo usar el script

1. Ejecuta el script `path_extract.py`.
2. Aparecerá una ventana para seleccionar un archivo Excel. Escoge el archivo que deseas analizar.
3. El script procesará las URLs y generará un archivo `results.txt` con los resultados.

### Formato del archivo de salida

El archivo de salida tiene el siguiente formato:

```
Company: EmpresaA
Count path: 2
List of Path:
- folder1
- folder2

Company: EmpresaB
Count path: 3
List of Path:
- path1
- path2
- anotherpath
```

## Personalización

Si deseas cambiar el nombre del archivo de salida, puedes modificar el parámetro `output_txt` en el script:

```python
output_txt = "nuevo_nombre.txt"
```

## Errores comunes

1. **El archivo Excel no contiene las columnas esperadas**:

   - Asegúrate de que el archivo tenga las columnas `Company` y `URL`.

2. **Error al leer el archivo Excel**:

   - Verifica que el archivo tenga formato válido (`.xlsx` o `.xls`).

3. **No se seleccionó un archivo**:
   - Si cierras la ventana sin seleccionar un archivo, el script mostrará un mensaje y finalizará.

## Licencia

Este proyecto es de uso libre y está distribuido bajo la licencia MIT. Puedes modificarlo y adaptarlo según tus necesidades.

## Contribuciones

Si tienes sugerencias o mejoras, no dudes en abrir un pull request o reportar un issue. ¡Todas las contribuciones son bienvenidas!
