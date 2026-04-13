# Práctica 2 — Semáforo simple con Raspberry Pi 3B+

**Materia:** Sistemas Embebidos aplicados a móviles  
**Alumno:** Miguel Angel Galicia Murrieta  
**Profesor:** Romero Gonzalez Gustavo Moises  
**Institución:** Tecnológico de Estudios Superiores Oriente del Estado de México  
**Fecha:** 12/04/2026

---

## Descripción

Simulación de un semáforo de tres fases (rojo, amarillo, verde) mediante control secuencial de tres LEDs con salidas digitales GPIO en una Raspberry Pi 3B+.

---

## Hardware requerido

| Componente | Cantidad |
|---|---|
| Raspberry Pi 3B+ | 1 |
| LED rojo | 1 |
| LED amarillo | 1 |
| LED verde | 1 |
| Resistencia 220 Ω | 3 |
| Protoboard | 1 |
| Cables jumper macho-hembra | 6 |

---

## Conexión

| LED | GPIO (BCM) | Pin físico | GND |
|---|---|---|---|
| Rojo | GPIO 17 | Pin 11 | Pin 6 |
| Amarillo | GPIO 27 | Pin 13 | Pin 6 |
| Verde | GPIO 22 | Pin 15 | Pin 6 |

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
python3 semaforo.py
```

Presiona `Ctrl+C` para detener el programa. El GPIO se libera automáticamente.

---

## Parámetros configurables

| Variable | Valor por defecto | Descripción |
|---|---|---|
| `RED_PIN` | `17` | Pin GPIO del LED rojo |
| `YELLOW_PIN` | `27` | Pin GPIO del LED amarillo |
| `GREEN_PIN` | `22` | Pin GPIO del LED verde |

Los tiempos de cada fase se modifican directamente en los `time.sleep()` del bucle principal:

| Fase | Duración |
|---|---|
| Rojo | 5 s |
| Amarillo | 2 s |
| Verde | 5 s |

---

## Ciclo de operación

```
ROJO (5s) → AMARILLO (2s) → VERDE (5s) → AMARILLO (2s) → repetir
```

Duración total del ciclo: **14 segundos**.

---

## Estructura del proyecto

```
semaforo/
├── semaforo.py
└── README.md
```
