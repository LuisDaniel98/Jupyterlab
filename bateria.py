import os
import platform
import time
import psutil

def play_sound():
    # Diferente comando según el sistema operativo
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 10000)  # Frecuencia: 1000 Hz, Duración: 1000 ms
    elif platform.system() == "Linux":
        os.system("echo -e '\a'")  # Hace un beep en terminal Linux
    else:
        print("Sonido no soportado en este sistema operativo.")

def check_battery():
    while True:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            charging = battery.power_plugged
            
            print(f"Nivel de batería: {percent}%, Cargando: {'Sí' if charging else 'No'}")
            
            if charging and percent >= 98:
                print("¡Batería al 95%! Emitiendo sonido...")
                play_sound()
                print("esperando desconexiòn")
                while battery.power_plugged:
                    time.sleep(10)
                    battery=psutil.sensors_battery()
                print("cargador desconectado")
                break
        else:
            print("No se pudo acceder a la información de la batería.")
            break
        time.sleep(60)  # Verificar cada 60 segundos

if __name__ == "__main__":
    check_battery()
