# Práctica 3 — 5 LEDs secuenciales (Digital) con Raspberry Pi 3B+

**Materia:** Sistemas Embebidos aplicados a móviles  
**Alumno:** Miguel Angel Galicia Murrieta  
**Profesor:** Romero Gonzalez Gustavo Moises  
**Institución:** Tecnológico de Estudios Superiores Oriente del Estado de México  
**Fecha:** 12/04/2026

---

## Descripción

Control secuencial de 5 LEDs mediante salidas digitales GPIO. El encendido recorre los LEDs de izquierda a derecha (LED 0 → LED 4) y el apagado en sentido inverso (LED 4 → LED 0), con un retardo configurable entre cada LED.

---

## Hardware requerido

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

## Instalación de dependencias

```bash
# RPi.GPIO viene preinstalada en Raspberry Pi OS
# Si no está disponible:
pip install RPi.GPIO
```

---

## Uso

```bash
python3 leds_secuencial.py
```

Presiona `Ctrl+C` para interrumpir antes de completar los ciclos. El GPIO se libera automáticamente.

---

## Parámetros configurables

| Variable | Valor por defecto | Descripción |
|---|---|---|
| `PINES_LED` | `[17, 27, 22, 23, 24]` | Vector de pines en orden de encendido |
| `RETARDO_ENCENDIDO` | `0.3 s` | Retardo entre LEDs al encender |
| `RETARDO_APAGADO` | `0.3 s` | Retardo entre LEDs al apagar |
| `RETARDO_CICLO` | `1.0 s` | Pausa entre ciclos completos |
| `TOTAL_CICLOS` | `5` | Número de ciclos (`0` = infinito) |

---

## Salida en terminal

```
GPIO inicializado | Pines: [17, 27, 22, 23, 24]

── Ciclo 1/5 ──
  Encendiendo: LED[0](GPIO 17) ▶ LED[1](GPIO 27) ▶ ... OK
  Apagando:    LED[4](GPIO 24) ◀ LED[3](GPIO 23) ◀ ... OK
```

---

## Estructura del proyecto

```
leds_secuencial/
├── leds_secuencial.py
└── README.md
```
