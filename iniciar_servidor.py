import os
import subprocess
import webbrowser
import time

def iniciar_servidor():
    ruta_directorio = r'C:\Users\COMPRAS\Desktop\Control Tonners'

    try:
        os.chdir(ruta_directorio)
        
        print("Actualizando el repositorio Git...")
        subprocess.run('git pull', shell=True, check=True)
        
        time.sleep(2)
        
        print("Iniciando el servidor Django...")
        subprocess.Popen('python manage.py runserver', shell=True)
        
        time.sleep(2)
        
        print("Abriendo el navegador web...")
        webbrowser.open('http://127.0.0.1:8000')
    
    except FileNotFoundError:
        print("Error: No se encontró el directorio especificado.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    iniciar_servidor()
