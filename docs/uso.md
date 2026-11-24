---
icon: material/book-open-variant
---

# Uso

Cómo revisar, encender, operar y apagar el kit con seguridad.

!!! danger "Regla de oro"
    Ante cualquier movimiento raro, **primero corta la energía** y después averigua qué pasó. Nunca metas las manos en el tablero ni cerca de un mecanismo mientras tenga energía.

---

## Antes de encender

Revisa esto cada vez, con el tablero apagado y el motor del tractor apagado:

- [ ] Nadie está sentado en el tractor ni cerca de los pedales, el volante o la palanca.
- [ ] El tractor está en un lugar plano y despejado, con el freno de mano puesto.
- [ ] Los tres mecanismos están bien sujetos a su base y a los mandos.
- [ ] Ningún cable está suelto, pelado o atorado en una parte que se mueve.
- [ ] Sabes dónde está el paro de emergencia para apagar todo de golpe.
- [ ] Las antenas están firmes y su cable bien conectado.

---

## Encendido

Enciende primero lo que piensa y al final lo que mueve.

1. Conecta el tablero a la batería del tractor (12 V).
2. Verifica que la Jetson Nano y las tres Pico encendieron (sus luces indicadoras).
3. Confirma que los tres mecanismos están en su posición de descanso.
4. Activa la energía de los motores (24 V).
5. Espera el **homing** del volante: busca sus dos topes y se centra en 0.0 rad. No toques el volante mientras tanto.
6. Inicia el programa de manejo.

## Operación

- ROS 2 recibe la posición del GNSS-RTK y los obstáculos del LiDAR.
- `goto_point.py` ([ver Software](software.md)) lleva el tractor hacia cada punto con **control proporcional** y se da por llegado a menos de 0.25 m.
- Las órdenes se saturan a 0.7 rad/s de velocidad angular y 1.2 m/s de velocidad lineal; el tractor alcanza como máximo 0.83 m/s.
- El modelo usa la geometría del tractor: distancia entre ejes 1.56 m; ancho de vía 0.85 m atrás y 0.73 m adelante.

## Apagado

Al revés que el encendido.

1. Detén el programa de manejo.
2. Espera a que los mecanismos regresen a descanso (freno aplicado, nada empujando el acelerador).
3. Corta la energía de los motores.
4. Desconecta el tablero de la batería del tractor.

!!! note "Por confirmar"
    Ubicación exacta de cada interruptor y comando para iniciar el programa de manejo.

---

## Si algo sale mal

| Qué notas | Qué hacer |
|---|---|
| Un mecanismo se mueve solo o no se detiene | Apaga todo con el paro de emergencia y aléjate de los mandos |
| Olor a quemado, humo o un cable caliente | Corta la alimentación principal y no vuelvas a encender hasta revisar |
| Un mecanismo no se mueve | Apaga y revisa que sus cables de potencia y de información estén bien conectados |
| El tractor no sigue el camino | Detén el programa y revisa las antenas, el USB del UM982 y el USB del radio en la Jetson |
| La posición brinca o tiene error de metros | No están llegando las correcciones: revisa el radio del rover y que la estación base esté encendida y transmitiendo |
| `hardware_error` activo en la telemetría | Se cortó el enlace UART o el I2C del encoder del volante: revisa ese cableado |

---

## Pruebas de campo

Es la única etapa pendiente. Sirve para medir el **error de seguimiento de ruta**: qué tanto se separa el tractor de la línea que debía recorrer.

1. Planear una ruta de prueba.
2. Grabar la posición real con GNSS-RTK durante el recorrido.
3. Comparar punto por punto contra la ruta planeada.
4. Resumir la desviación lateral con el **RMSE** (raíz del error cuadrático medio).

!!! warning "Definir la referencia"
    El objetivo de 5 % de error necesita una referencia: porcentaje de la longitud de la ruta, del ancho de trabajo o un RMSE lateral en metros. Definirla antes de las pruebas.
