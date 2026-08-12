import reflex as rx
from theme import COLORS, hex_to_rgba

def Pag404():
    return rx.center(
        rx.el.div(
            rx.heading("404", font_size="6em", color=COLORS["white"], padding="2rem"),
            rx.text("Página no encontrada", font_size="2em", color=hex_to_rgba(COLORS["white"], 0.7)),
            rx.text("Apartado no terminado", font_size="1em", color=hex_to_rgba(COLORS["purple"], 0.7)),
            rx.link(
                "Volver al inicio",
                href="/",
                font_size="1.5em",
                color=COLORS["purple"],
                _hover={"text_decoration": "underline"},
            ),
            
            style= {
                "width": "100%",
                "height": "100%",
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "center",
                "align-items": "center"
            }
        ),
        height="100dvh",
        width="100%",
        bg=hex_to_rgba(COLORS["black"], 0.9),
    )