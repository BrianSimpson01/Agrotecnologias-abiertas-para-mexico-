---
icon: material/arrow-expand-down
---

# Pistones (pedales)

Tres actuadores lineales empujan los pedales del tractor: **freno, embrague y acelerador**. Cada uno convierte el giro de un motor en empuje lineal con un **husillo** (tornillo de avance), con un driver por pistón.

- **Controladores:**
    - **Pico 2:** freno y embrague
    - **Pico 3:** acelerador (comparte la Pico con la [palanca](palanca.md))
- **Drivers:** 3 × DM860H (el mismo modelo que el volante), uno por pistón, alimentados a 24 V desde el [tablero](tablero.md)

---

## Empuje por husillo

Un torque pequeño produce un empuje grande, a cambio de avanzar despacio. La fuerza se calcula con la ecuación 14.4 de Norton:

**F = 2π · τ · η ÷ p**

| Símbolo | Significado | Valor |
|---|---|---|
| τ | Torque del motor | 2.80 N·m |
| p | Paso: avance de la tuerca por vuelta | 4 mm |
| η | Eficiencia | 0.9 |
| **F** | **Empuje disponible** | **3,958.4 N (≈ 403.6 kgf)** |

Entre más fino el paso, más fuerza y menos velocidad.

---

## Factor de seguridad

| Pedal | Fuerza requerida | Factor de seguridad |
|---|---|---|
| Freno | 600 N | 6.60 |
| Embrague | 600 N | 6.60 |
| Acelerador | 120 N | 32.99 |

Factor de seguridad = fuerza disponible ÷ fuerza requerida.

!!! warning "Estimado, no medido"
    Los 600 N son una estimación basada en pruebas de operación de maquinaria agrícola, no una medición propia (a diferencia del volante). El acelerador se tomó como el 20 % de ese valor. Con un factor de 6.6, el diseño aguanta aunque la fuerza real sea varias veces mayor.

---

## Componentes

| Componente | Modelo | Función |
|---|---|---|
| Motor (x3) | NEMA 23 (cara de 57 mm), a pasos | Gira en incrementos fijos: contar pulsos es contar ángulo |
| Husillo (x3) | Paso 4 mm, η = 0.9 | Convierte el giro del motor en empuje lineal sobre el pedal |
| Driver (x3) | DM860H | Amplificador entre el micro y el motor. Señales: Step, Direction, Enable |
| Encoder (x3) | AS5600 (efecto Hall, 12 bits) | Mide la orientación de un imán pegado al eje: 0–4095 por vuelta, 0.088° por cuenta |
| Lector del encoder (x3) | ATtiny412 | Lee el AS5600 por I2C y lo envía a la Pico |
| Controladores | Raspberry Pi Pico 2 y Pico 3 (micro-ROS) | Pico 2: freno y embrague · Pico 3: acelerador |
| Soportes | Impresos en 3D, con abrazaderas | Montaje no invasivo sobre los pedales |


```mermaid
flowchart LR
    JET[Jetson Nano<br/>ROS 2] --> P2[Pico 2]
    JET --> P3[Pico 3]
    P2 --> D1[Driver] --> F[Freno]
    P2 --> D2[Driver] --> E[Embrague]
    P3 --> D3[Driver] --> A[Acelerador]
    P3 -.-> PAL[Palanca]
```

!!! note "Por confirmar"
    - El reporte no escribe p = 4 mm ni η = 0.9; son los valores que dan 3,958.4 N. Confirmarlos.
    - El mismo motor aparece con 2.80 N·m aquí y con 3 N·m en el volante. Unificar el valor.
    - Posición segura ante falla: freno aplicado y acelerador en reposo.

---

## PCB

Cada pistón lleva su propia **PCB de actuador**, la misma placa que usan el volante y la palanca. Descargas y detalles en [Tablero → PCB de actuador](tablero.md#pcb-de-actuador).

---

## Conexiones

| Pico (GPIO) | Conecta a | Señal |
|---|---|---|
| | | |

## Código

```cpp
// Firmware de la Pico 2 (freno y embrague)
// El acelerador va en el firmware de la Pico 3, junto con la palanca
```

## Fotos

<!-- docs/recursos/ -->
