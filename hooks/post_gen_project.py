# Importar el módulo subprocess para ejecutar comandos de shell
import subprocess

# Código de escape ANSI para establecer el color del texto siguiente en azul
MESSAGE_COLOR = "\x1b[34m"

# Código de escape ANSI para restablecer todos los formatos de texto a los valores predeterminados
RESET_ALL = "\x1b[0m"

# Imprimir un mensaje en azul indicando el progreso
print(f"{MESSAGE_COLOR}¡Casi terminado!")

# Imprimir un mensaje indicando la inicialización de un repositorio git
print(f"Inicializando un repositorio git...{RESET_ALL}")

# Ejecutar el comando 'git init' para inicializar un nuevo repositorio Git
subprocess.call(['git', 'init'])

# Ejecutar el comando 'git add *' para agregar todos los archivos al área de preparación
subprocess.call(['git', 'add', '*'])

# Ejecutar el comando 'git commit -m "Initial commit"' para realizar un commit inicial
subprocess.call(['git', 'commit', '-m', 'Commit inicial'])

# Imprimir un mensaje en azul indicando la finalización y alentando al usuario
print(f"{MESSAGE_COLOR}¡La estructura de tu proyecto esta definido! ¡Crea y diviértete!{RESET_ALL}")

