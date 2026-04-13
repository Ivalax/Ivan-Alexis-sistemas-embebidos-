# Práctica 4 — 5 LEDs secuenciales (PWM) con Raspberry Pi 3B+

**Materia:** Sistemas Embebidos aplicados a móviles  
**Alumno:** Miguel Angel Galicia Murrieta  
**Profesor:** Romero Gonzalez Gustavo Moises  
**Institución:** Tecnológico de Estudios Superiores Oriente del Estado de México  
**Fecha:** 12/04/2026

---

## Descripción

Variación PWM de la práctica de 5 LEDs secuenciales. En lugar de encendido/apagado instantáneo, cada LED realiza un **fade in** (0% → 100% brillo) al encender y un **fade out** (100% → 0%) al apagar, usando Modulación por Ancho de Pulso a 1000 Hz. El circuito físico es idéntico a la práctica anterior.

---

## Hardware requerido

Idéntico a la Práctica 3 — mismo circuito, sin cambios de hardware.

| Componente | Cantidad |
|---|---|
| Raspberry Pi 3B+ | 1 |
| LED | 5 |
| Resistencia 220 Ω | 5 |
| Protoboard | 1 |
| Cables jumper macho-hembra | 10 |

---

## Conexión

| LED | GPIO (BCM) | Pin físico |
|---|---|---|
| LED 0 | GPIO 17 | Pin 11 |
| LED 1 | GPIO 27 | Pin 13 |
| LED 2 | GPIO 22 | Pin 15 |
| LED 3 | GPIO 23 | Pin 16 |
| LED 4 | GPIO 24 | Pin 18 |

GND común en pin físico 6. Cada LED conectado en serie con una resistencia de 220 Ω.

---

## Diferencia respecto a la versión digital

| Aspecto | Digital (Práctica 3) | PWM (Práctica 4) |
|---|---|---|
| Estado del pin | HIGH / LOW | Duty cycle 0–100% |
| Control de brillo | No | Sí |
| Función principal | `GPIO.output()` | `GPIO.PWM.ChangeDutyCycle()` |
| Frecuencia | — | 1000 Hz |
| Efecto visual | Encendido instantáneo | Fade in / Fade out |

---

## Instalación de dependencias

```bash
# RPi.GPIO viene preinstalada en Raspberry Pi OS
# Si no está disponible:
pip install RPi.GPIO
```

---

## Uso

```bash
python3 leds_pwm.py
```

Presiona `Ctrl+C` para interrumpir. Todos los canales PWM se detienen y el GPIO se libera automáticamente.

---

## Parámetros configurables

| Variable | Valor por defecto | Descripción |
|---|---|---|
| `PINES_LED` | `[17, 27, 22, 23, 24]` | Vector de pines en orden de encendido |
| `FRECUENCIA_PWM` | `1000 Hz` | Frecuencia de la señal PWM |
| `PASO` | `5` | Incremento de duty cycle por paso (%) |
| `RETARDO_PASO` | `0.01 s` | Retardo entre cada paso del fade |
| `RETARDO_LED` | `0.05 s` | Pausa entre LEDs consecutivos |
| `RETARDO_CICLO` | `0.8 s` | Pausa entre ciclos completos |
| `TOTAL_CICLOS` | `5` | Número de ciclos (`0` = infinito) |

Reducir `PASO` o `RETARDO_PASO` ajusta la suavidad y velocidad del efecto.

---

## Salida en terminal

```
PWM inicializado | Pines: [17, 27, 22, 23, 24] | Frecuencia: 1000 Hz

── Ciclo 1/5 ──
  Fade in:  LED[0] ▶ LED[1] ▶ LED[2] ▶ LED[3] ▶ LED[4] ▶ OK
  Fade out: LED[4] ◀ LED[3] ◀ LED[2] ◀ LED[1] ◀ LED[0] ◀ OK
```

---

## Estructura del proyecto

```
leds_pwm/
├── leds_pwm.py
└── README.md
```
