import RPi.GPIO as GPIO
import time, os
GPIO.setmode(GPIO.BCM)
boton_pin = 17
GPIO.setup(boton_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        # Leer el estado del botón (si está presionado o no)
        if GPIO.input(boton_pin) == GPIO.HIGH:
            print("¡Botón presionado! Ejecutando el comando...")
            # Ejecutar el comando deseado, por ejemplo, apagar
            os.system('sudo shutdown now')
            time.sleep(0.5)  # Para evitar múltiples detecciones al mantener presionado
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programa interrumpido")

finally:
    GPIO.cleanup()
