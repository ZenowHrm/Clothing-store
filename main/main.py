import reflex as rx
from theme import COLORS, hex_to_rgba

#----Estados

#----Componentes

#----Paginas
from pages.principal import Pagprincipal
from pages.gallery import Galeria

app = rx.App(
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin="anonymous"),
    ],
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap",
    ],
    style={
        "font_family": "'Comic Neue', cursive, sans-serif",
    }
)

metadatos = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
]

app.add_page(
    Pagprincipal,
    route="/",
    title="TeeVibes Store | Inicio",
    description="Encuentra los mejores estilos personalizados",
    meta=metadatos
)

app.add_page(
    Galeria,
    route="/gallery",
    title="TeeVibes Store | Galeria",
    description="Encuentra los mejores estilos personalizados",
    meta=metadatos
)