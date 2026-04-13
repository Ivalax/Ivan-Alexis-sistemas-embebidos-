#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

PINES_LED = [17, 27, 22, 23, 24]
RETARDO_ENCENDIDO = 0.3
RETARDO_APAGADO   = 0.3
RETARDO_CICLO     = 1.0
TOTAL_CICLOS      = 5

def inicializar_gpio(pines):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in pines:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    print(f"GPIO inicializado | Pines: {pines}\n")

def liberar_gpio(pines):
    for pin in pines:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()
    print("\nGPIO liberado. Programa terminado.")

def encender_secuencial(pines, retardo):
    print("  Encendiendo: ", end="", flush=True)
    for i in range(len(pines)):
        GPIO.output(pines[i], GPIO.HIGH)
        print(f"LED[{i}](GPIO {pines[i]}) ▶ ", end="", flush=True)
        time.sleep(retardo)
    print("OK")

def apagar_secuencial_inverso(pines, retardo):
    print("  Apagando:    ", end="", flush=True)
    for i in range(len(pines) - 1, -1, -1):
        GPIO.output(pines[i], GPIO.LOW)
        print(f"LED[{i}](GPIO {pines[i]}) ◀ ", end="", flush=True)
        time.sleep(retardo)
    print("OK")

def ejecutar_ciclos(pines, total_ciclos):
    ciclo = 0
    infinito = (total_ciclos == 0)
    while infinito or ciclo < total_ciclos:
        ciclo += 1
        print(f"── Ciclo {ciclo}{' (∞)' if infinito else f'/{total_ciclos}'} ──")
        encender_secuencial(pines, RETARDO_ENCENDIDO)
        time.sleep(RETARDO_CICLO)
        apagar_secuencial_inverso(pines, RETARDO_APAGADO)
        time.sleep(RETARDO_CICLO)

def main():
    inicializar_gpio(PINES_LED)
    try:
        ejecutar_ciclos(PINES_LED, TOTAL_CICLOS)
    except KeyboardInterrupt:
        print("\n[!] Interrupción por usuario.")
    finally:
        liberar_gpio(PINES_LED)

if __name__ == "__main__":
    main()