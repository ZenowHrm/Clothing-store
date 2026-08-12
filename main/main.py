import reflex as rx

#----Estados

#----Componentes

#----Paginas
from pages.principal import Pagprincipal
from pages.gallery import Galeria
from pages.contact import Contact
from pages.notfoundpage import Pag404
from pages.design import DesignPage

app = rx.App(
    show_built_with_reflex=False,
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin="anonymous"),
        rx.script(src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"),
        rx.script(src="/editor.js"),
    ],
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Comic+Neue:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap",
    ],
    style={
        "font_family": "'Comic Neue', cursive, sans-serif",
    },
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

app.add_page(
    Contact,
    route="/contact",
    title="TeeVibes Store | Contacto",
    description="Contáctanos para más información",
    meta=metadatos
)

app.add_page(
    DesignPage,
    route="/design",
    title="TeeVibes Store | Diseño",
    description="Crea tu propia prenda personalizada",
    meta=metadatos,
)

app.add_page(
    Pag404,
    route="/404",
    title="TeeVibes Store | Página no encontrada",
    description="Página no encontrada",
    meta=metadatos
)