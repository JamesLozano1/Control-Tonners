import os
import subprocess
import webbrowser
import time

def iniciar_servidor():
    ruta_directorio = r'c:\Users\COMPRAS\Documents\Control-Tonners'
    
    try:
        os.chdir(ruta_directorio)
        navegador_abierto = False  # Bandera para controlar si el navegador ya se abrió

        print("Actualizando el repositorio Git...")
        try:
            subprocess.run('git pull', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el comando git pull: {e}")
        
        time.sleep(2)
        
        print("Iniciando el servidor Django...")
        servidor = subprocess.Popen('python manage.py runserver', shell=True)
        
        time.sleep(10)
        
        # Abrir el navegador solo si no se ha abierto antes
        if not navegador_abierto:
            print("Abriendo el navegador web...")
            webbrowser.open('http://127.0.0.1:8000')
            navegador_abierto = True
        
        # Esperar un tiempo antes de la próxima actualización
        tiempo_espera = 60 * 5  # 5 minutos
        for _ in range(tiempo_espera):
            time.sleep(1)

    except FileNotFoundError:
        print("Error: No se encontró el directorio especificado.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    iniciar_servidor()

# Comando para crear arranque de aplicación
# pyinstaller --onefile Nombre_Archivo_Python.py
# pyinstaller iniciar_servidor.spec

