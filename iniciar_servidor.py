import os
import subprocess
import webbrowser
import time

def iniciar_servidor():
    ruta_directorio = r'C:\Users\COMPRAS\Desktop\Control Tonners'
    
    try:
        os.chdir(ruta_directorio)
        
        while True:
            print("Actualizando el repositorio Git...")
            try:
                subprocess.run('git pull', shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error al ejecutar el comando git pull: {e}")
            
            time.sleep(2)
            
            print("Iniciando el servidor Django...")
            servidor = subprocess.Popen('python manage.py runserver', shell=True)
            
            time.sleep(10)
            
            print("Abriendo el navegador web...")
            webbrowser.open('http://127.0.0.1:8000')
            
            # Esperar un tiempo antes de la próxima actualización
            tiempo_espera = 60 * 5  # 5 minutos
            for _ in range(tiempo_espera):
                time.sleep(1)
                
                # Comprobar si el servidor aún está en ejecución
                if servidor.poll() is not None:
                    print("El servidor Django se detuvo. Reiniciando...")
                    break

            # Si el servidor sigue en ejecución, terminarlo
            if servidor.poll() is None:
                servidor.terminate()
                try:
                    servidor.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    servidor.kill()

    except FileNotFoundError:
        print("Error: No se encontró el directorio especificado.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    iniciar_servidor()