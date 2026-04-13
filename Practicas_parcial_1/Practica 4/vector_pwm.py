#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

PINES_LED = [17, 27, 22, 23, 24]
FRECUENCIA_PWM = 1000
PASO           = 5
RETARDO_PASO   = 0.01
RETARDO_LED    = 0.05
RETARDO_CICLO  = 0.8
TOTAL_CICLOS   = 5

def inicializar_pwm(pines):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    canales = []
    for pin in pines:
        GPIO.setup(pin, GPIO.OUT)
        pwm = GPIO.PWM(pin, FRECUENCIA_PWM)
        pwm.start(0)
        canales.append(pwm)
    print(f"PWM inicializado | Pines: {pines} | Frecuencia: {FRECUENCIA_PWM} Hz\n")
    return canales

def liberar_pwm(canales, pines):
    for canal in canales:
        canal.stop()
    GPIO.cleanup()
    print("\nPWM liberado. Programa terminado.")

def fade_in(canal, paso, retardo):
    for dc in range(0, 101, paso):
        canal.ChangeDutyCycle(dc)
        time.sleep(retardo)

def fade_out(canal, paso, retardo):
    for dc in range(100, -1, -paso):
        canal.ChangeDutyCycle(dc)
        time.sleep(retardo)

def encender_secuencial_pwm(canales, paso, retardo_paso, retardo_led):
    print("  Fade in:  ", end="", flush=True)
    for i, canal in enumerate(canales):
        fade_in(canal, paso, retardo_paso)
        print(f"LED[{i}] ▶ ", end="", flush=True)
        time.sleep(retardo_led)
    print("OK")

def apagar_secuencial_inverso_pwm(canales, paso, retardo_paso, retardo_led):
    print("  Fade out: ", end="", flush=True)
    for i in range(len(canales) - 1, -1, -1):
        fade_out(canales[i], paso, retardo_paso)
        print(f"LED[{i}] ◀ ", end="", flush=True)
        time.sleep(retardo_led)
    print("OK")

def ejecutar_ciclos(canales, total_ciclos):
    ciclo = 0
    infinito = (total_ciclos == 0)
    while infinito or ciclo < total_ciclos:
        ciclo += 1
        print(f"── Ciclo {ciclo}{' (∞)' if infinito else f'/{total_ciclos}'} ──")
        encender_secuencial_pwm(canales, PASO, RETARDO_PASO, RETARDO_LED)
        time.sleep(RETARDO_CICLO)
        apagar_secuencial_inverso_pwm(canales, PASO, RETARDO_PASO, RETARDO_LED)
        time.sleep(RETARDO_CICLO)

def main():
    canales = inicializar_pwm(PINES_LED)
    try:
        ejecutar_ciclos(canales, TOTAL_CICLOS)
    except KeyboardInterrupt:
        print("\n[!] Interrupción por usuario.")
    finally:
        liberar_pwm(canales, PINES_LED)

if __name__ == "__main__":
    main()