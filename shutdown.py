import RPi.GPIO as GPIO
import time, os
GPIO.setmode(GPIO.BCM)
boton_pin = 17
GPIO.setup(boton_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        if GPIO.input(boton_pin) == GPIO.HIGH:
            print("Botón presionado")
            #os.system('sudo shutdown now')
            time.sleep(0.5)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programa interrumpido")

finally:
    GPIO.cleanup()
