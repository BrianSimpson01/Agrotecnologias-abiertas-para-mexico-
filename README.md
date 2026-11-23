<div align="center">

# 🚜 Agrotecnologías abiertas para México

**Kit de *retrofit* no invasivo para el manejo autónomo de tractores agrícolas**

Ingeniería Mecatrónica · Universidad Iberoamericana Puebla

[![Sitio](https://img.shields.io/badge/Documentación-sitio_web-E00034?style=for-the-badge)](https://briansimpson01.github.io/Agrotecnologias-abiertas-para-mexico-/)
[![ROS 2](https://img.shields.io/badge/ROS_2-Jetson_Nano-82786F?style=for-the-badge&logo=ros)](https://briansimpson01.github.io/Agrotecnologias-abiertas-para-mexico-/software/)
[![MkDocs Material](https://img.shields.io/badge/MkDocs-Material-1A1A1A?style=for-the-badge)](https://squidfunk.github.io/mkdocs-material/)

</div>

---

## Sobre el proyecto

Kit modular que le agrega manejo autónomo a un tractor que ya existe (Kubota B2401), sin cortar, soldar ni tocar su sistema hidráulico o eléctrico. Motores a pasos giran el volante, empujan los pedales y mueven la palanca; una Jetson Nano con ROS 2 planea la ruta con posicionamiento GNSS-RTK.

| Subsistema | Qué hace |
|---|---|
| **Tablero** | Potencia (12 → 24 V), Jetson Nano, 3 Raspberry Pi Pico, drivers y GNSS-RTK |
| **Volante** | NEMA 23 con reducción 3:1, encoder AS5600 y homing automático |
| **Palanca y acelerador** | Mecanismo articulado + pistón del acelerador |
| **Pistones** | Husillos sobre freno, embrague y acelerador |
| **Software** | ROS 2: modelo URDF, simulación en Gazebo y control `goto_point.py` |

## Contenido del repositorio

```text
├── docs/          Páginas del sitio (MkDocs Material)
│   └── recursos/  CAD (SolidWorks), PCB (Altium) y workspace ROS 2 para descargar
├── ros2_ws/       Workspace de ROS 2 (kubota_description, tractor_interfaces)
└── mkdocs.yml     Configuración del sitio
```

## Ver el sitio localmente

```bash
pip install -r requirements.txt
mkdocs serve
```

Abre http://127.0.0.1:8000/. Cada push a `main` publica el sitio en GitHub Pages.

## Equipo

Héctor Cornejo Morales · Ángel Iván Domínguez Cruz · Danna Paola García Sánchez · Pablo Eduardo Manzano López · Héctor Ojeda Serafio · Brian Carl Simpson y Reyes · Apolinar Velázquez Fernández · Emmanuel del Villar Soto
