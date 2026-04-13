import RPi.GPIO as GPIO
import time

RED_PIN    = 17
YELLOW_PIN = 27
GREEN_PIN  = 22

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED_PIN,    GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(GREEN_PIN,  GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        GPIO.output(RED_PIN, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(RED_PIN, GPIO.LOW)

        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(YELLOW_PIN, GPIO.LOW)

        GPIO.output(GREEN_PIN, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(GREEN_PIN, GPIO.LOW)

        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(YELLOW_PIN, GPIO.LOW)

except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario")
finally:
    GPIO.cleanup()
    print("GPIO limpiado. Programa finalizado.")