# Agrotecnologías abiertas para México

Documentación del proyecto hecha con **MkDocs + Material**.

## Contenido

- `docs/`: páginas del sitio (MkDocs).
- `ros2_ws/`: workspace de ROS 2 (modelo del Kubota y nodo de control).

## Ver localmente

```bash
pip install -r requirements.txt
mkdocs serve
```

Abre http://127.0.0.1:8000/

## Publicación

Cada push a `main` publica el sitio en GitHub Pages (rama `gh-pages`) mediante `.github/workflows/ci.yml`.

Sitio: https://briansimpson01.github.io/Agrotecnologias-abiertas-para-mexico-/
