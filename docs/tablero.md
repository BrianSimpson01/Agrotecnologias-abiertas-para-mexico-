# Tablero de control

El tablero es el **gabinete que concentra la electrónica del kit** (no es el tablero de instrumentos del tractor). Se alimenta de la batería de 12 V del motor del tractor, eleva esa tensión a 24 V y entrega tres salidas reguladas (3.3 V, 5 V y 24 V) a tres Raspberry Pi Pico y a sus drivers. Las tres Pico se conectan a una **Jetson Nano**, que corre ROS 2. Las **antenas van montadas encima** de la caja.

El gabinete es una estructura de perfil de aluminio con placa de montaje perforada. Contiene la etapa de potencia, tres microcontroladores y cinco drivers de motor.

---

## Arquitectura

El tablero se divide en una **etapa de potencia** (batería → elevador → salidas reguladas) y **tres canales de control independientes**: Pico 1 para el volante, Pico 2 para los pistones de freno y embrague, y Pico 3 para la palanca y el pistón del acelerador. Cada Pico gobierna solo a sus drivers.

```mermaid
flowchart LR
    BAT[Batería del tractor<br/>12 V DC] --> BOOST[Elevador boost DC-DC<br/>12 → 24 V]
    BOOST --> V24[Salida 24 V]
    BOOST --> V5[Salida 5 V]
    BOOST --> V33[Salida 3.3 V]
    V5 & V33 --> PICOS[3 Raspberry Pi Pico]
    JET[Jetson Nano<br/>ROS 2] <--> PICOS
    ANT[Antenas] --> JET
    V24 --> DRV[5 drivers]
    PICOS -->|señal de control| DRV
    DRV -->|potencia 24 V| MEC[Volante · Freno · Embrague<br/>Palanca · Acelerador]
    MEC -->|DATA: retroalimentación| PICOS
```

La separación en canales **aísla fallas**: si un canal se detiene, los otros dos conservan su control.

!!! tip "Regla fácil"
    **Cada mecanismo tiene su propio driver, y cada Pico solo maneja los suyos.** Si falla el volante, revisa solo la Pico 1 y su driver; si fallan freno o embrague, la Pico 2; si fallan palanca o acelerador, la Pico 3. El driver más pequeño es siempre el de la palanca; el volante y los pistones usan el mismo modelo (DM860H).

---

## Componentes

| Bloque | Componente | Función | Tensión / señal |
|---|---|---|---|
| Entrada | Batería del motor del tractor | Fuente primaria de energía | 12 V DC |
| Potencia | Convertidor elevador (boost) DC-DC | Eleva la tensión de la batería | 12 V → 24 V DC |
| Potencia | Salidas reguladas | Distribuyen la energía a lógica y potencia | 3.3 V, 5 V y 24 V DC |
| Cómputo | Jetson Nano | Corre ROS 2; las tres Pico se conectan a ella | Por confirmar |
| Control | Raspberry Pi Pico 1 — volante | Controla el driver del volante | Lógica 3.3 V |
| Control | Raspberry Pi Pico 2 — freno y embrague | Controla los drivers de los pistones de freno y embrague | Lógica 3.3 V |
| Control | Raspberry Pi Pico 3 — palanca y acelerador | Controla el driver de la palanca y el del pistón del acelerador | Lógica 3.3 V |
| Potencia de salida | Driver del volante (DM860H) | Entrega corriente al motor del volante | 24 V |
| Potencia de salida | Driver de la palanca (el más pequeño) | Entrega corriente al mecanismo de la palanca | 24 V |
| Potencia de salida | Drivers de pistones (3 × DM860H, uno por pistón) | Entregan corriente a cada pistón | 24 V |
| Comunicación | Antenas (encima de la caja) | Reciben señal externa | Tipo y conexión por confirmar |

---

## Cableado y señales

Las conexiones internas forman dos redes: la de **alimentación**, que reparte las tres tensiones, y la de **control**, donde cada Pico se conecta solo con los drivers de su mecanismo.

| Tramo | Origen → destino | Tensión / señal |
|---|---|---|
| Entrada | Batería del tractor → convertidor elevador | 12 V DC |
| Elevación | Convertidor → bus de potencia | 24 V DC |
| Alimentación de potencia | Salida 24 V → los 5 drivers | 24 V DC |
| Alimentación lógica | Salidas 5 V y 3.3 V → Picos y circuitos de señal | 5 V / 3.3 V DC |
| Enlace de control | Jetson Nano ↔ Picos 1, 2 y 3 | micro-ROS |
| Canal volante | Pico 1 → driver del volante | Señal de control |
| Canal freno y embrague | Pico 2 → 2 drivers de pistón | Señal de control (2 salidas) |
| Canal palanca y acelerador | Pico 3 → driver de la palanca + driver del pistón del acelerador | Señal de control (2 salidas) |
| Salida MOTOR | Cada driver → su mecanismo | Potencia 24 V |
| Entrada DATA | Cada mecanismo → su Pico | Retroalimentación de baja tensión |

---

## Fabricación

- **PCB:** sustituye el cableado suelto por pistas de cobre y hace el sistema repetible.
- **Ampacidad:** el calibre de cada cable se eligió según la corriente que lleva.
- **Paro de emergencia por hardware:** un circuito físico que corta la potencia aunque el programa esté colgado.
- **Pruebas realizadas:** continuidad, alimentación, sincronización electrónica y respuesta conjunta bajo condiciones operativas simuladas.

---

## Seguridad

El sistema mueve mandos de un vehículo pesado, así que debe poder detenerse de inmediato y sin depender del software.

- Paro de emergencia físico que corta la alimentación de los drivers.
- Protección por fusible o interruptor termomagnético en el bus de 24 V.
- Posición segura por defecto ante falla: freno aplicado y acelerador en reposo.
- Separación física de cables de potencia y de señal dentro del gabinete.

!!! warning "Por confirmar"
    Modelo del convertidor y del driver de la palanca, alimentación de la Jetson Nano y si va dentro del gabinete, corrientes nominales, fusible en la entrada de 12 V, qué carga usa la salida de 3.3 V y cuál la de 5 V, protocolo de las líneas DATA, calibre del cableado de 24 V, tipo de antenas y ubicación del paro de emergencia.

---

## Fotos

<!-- Agrega fotos en docs/recursos/ y enlázalas así: ![Tablero](recursos/tablero.jpg) -->
