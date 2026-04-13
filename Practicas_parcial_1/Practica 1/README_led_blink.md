# Práctica 1 — LED Blink con Raspberry Pi 3B+

**Materia:** Sistemas Embebidos aplicados a móviles  
**Alumno:** Miguel Angel Galicia Murrieta  
**Profesor:** Romero Gonzalez Gustavo Moises  
**Institución:** Tecnológico de Estudios Superiores Oriente del Estado de México  
**Fecha:** 12/04/2026

---

## Descripción

Control básico de un LED mediante salida digital GPIO en una Raspberry Pi 3B+. El LED parpadea con un período de 2 segundos (1 s encendido / 1 s apagado).

---

## Hardware requerido

| Componente | Cantidad |
|---|---|
| Raspberry Pi 3B+ | 1 |
| LED (azul) | 1 |
| Resistencia 220 Ω | 1 |
| Protoboard | 1 |
| Cables jumper macho-hembra | 2 |

---

## Conexión

| Señal | GPIO (BCM) | Pin físico |
|---|---|---|
| LED ánodo (+ resistencia) | GPIO 18 | Pin 12 |
| LED cátodo | GND | Pin 6 |

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
python3 led_blink.py
```

Presiona `Ctrl+C` para detener el programa. El GPIO se libera automáticamente.

---

## Parámetros configurables

| Variable | Valor por defecto | Descripción |
|---|---|---|
| `LED_PIN` | `18` | Pin GPIO en modo BCM |

---

## Estructura del proyecto

```
led_blink/
├── led_blink.py
└── README.md
```
