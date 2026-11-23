# Palanca de velocidades

La palanca se acciona con un **mecanismo articulado** que respeta el recorrido de la transmisión original del tractor. Ya está construida e integrada al sistema.

- **Controlador:** Raspberry Pi Pico #2
- **Driver:** dedicado, alimentado a 24 V desde el [tablero](tablero.md)
- **Retroalimentación:** línea DATA del mecanismo a su Pico

---

## Funcionamiento

```mermaid
flowchart LR
    ROS[ROS 2] --> PICO[Pico palanca]
    PICO -->|señal de control| DRV[Driver]
    DRV -->|24 V| ACT[Actuador]
    ACT --> MEC[Mecanismo articulado]
    MEC --> PAL[Palanca de velocidades]
    MEC -. DATA .-> PICO
```

El mecanismo es no invasivo: se monta por fuera con abrazaderas y acoples rápidos, igual que el resto del kit.

### Velocidades medidas

Las velocidades del tractor se cronometraron en un tramo de 50 m:

| Acelerador | Tiempo en 50 m | Velocidad |
|---|---|---|
| Mínimo | 150 s | 0.33 m/s (1.2 km/h) |
| Máximo | 60 s | 0.83 m/s (3 km/h) |

---

## Componentes

| Componente | Modelo | Notas |
|---|---|---|
| Microcontrolador | Raspberry Pi Pico | |
| Driver | *Por completar* | 24 V |
| Actuador | *Por completar* | |
| Mecanismo | Articulado, impreso en 3D | |

!!! note "Por completar"
    El reporte todavía no trae los cálculos ni los resultados de la palanca: posiciones (velocidades) que acciona, fuerza requerida, recorrido, actuador y driver.

---

## Conexiones

| Pico (GPIO) | Conecta a | Señal |
|---|---|---|
| | | |

## Código

```cpp
// Firmware de la Pico de la palanca
```

## Fotos

<!-- docs/recursos/ -->
