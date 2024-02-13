# Importar el módulo os para interactuar con el sistema operativo
import os

# Importar el módulo sys para interactuar con el intérprete de Python
import sys

# Obtener el valor del proyecto desde la plantilla usando cookiecutter
project_slug = "{{ cookiecutter.project_slug }}"

# Código de escape ANSI para establecer el color del texto siguiente en rojo
ERROR_COLOR = "\x1b[31m"

# Código de escape ANSI para establecer el color del texto siguiente en azul
MESSAGE_COLOR = "\x1b[34m"

# Código de escape ANSI para restablecer todos los formatos de texto a los valores predeterminados
RESET_ALL = "\x1b[0m"

# Verificar si el nombre del proyecto comienza con "x"
if project_slug.startswith("x"):
    # Imprimir un mensaje de error en rojo y salir del script con código de error 1
    print(f"{ERROR_COLOR}ERROR: {project_slug=} no es un nombre válido para esta plantilla.{RESET_ALL}")
    sys.exit(1)

# Imprimir un mensaje en azul alentando al usuario y mostrando el directorio de trabajo actual
print(f"{MESSAGE_COLOR}¡Vamos allá! ¡Estás a punto de crear algo increíble!")
print(f"Creando el proyecto en { os.getcwd() }{RESET_ALL}")
