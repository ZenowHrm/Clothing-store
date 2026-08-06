import reflex as rx
from Frontend.state.indexcarrusel import CarouselState


def Carrusel() -> rx.Component:
    carrusel_style = {
        "min_width": "100%",
        "height": "500px",
    }

    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.foreach(
                    CarouselState.images,
                    lambda img: rx.image(src=img, style=carrusel_style)
                ),
                style={
                    "display": "flex",
                    "width": "100%",
                    "height": "100%",
                    "transform": f"translateX(-{CarouselState.current_index * 100}%)",
                    "transition": "transform 0.5s ease-in-out",
                }
            ),

            rx.el.button(
                "❮",
                on_click=CarouselState.prev_slide,
                style={
                    "position": "absolute",
                    "top": "50%",
                    "left": "15px",
                    "transform": "translateY(-50%)",
                    "background": "rgba(0, 0, 0, 0.3)",
                    "color": "white",
                    "border": "none",
                    "padding": "10px 15px",
                    "cursor": "pointer",
                    "border_radius": "50%",
                    "font_size": "18px",
                }
            ),

            rx.el.button(
                "❯",
                on_click=CarouselState.next_slide,
                style={
                    "position": "absolute",
                    "top": "50%",
                    "right": "15px",
                    "transform": "translateY(-50%)",
                    "background": "rgba(0, 0, 0, 0.3)",
                    "color": "white",
                    "border": "none",
                    "padding": "10px 15px",
                    "cursor": "pointer",
                    "border_radius": "50%",
                    "font_size": "18px",
                }
            ),

            rx.el.div(
                rx.foreach(
                    CarouselState.images,
                    lambda _, idx: rx.el.div(
                        on_click=lambda: CarouselState.set_slide(idx),
                        style={
                            "width": "30px",
                            "height": "3px",
                            "background_color": rx.cond(
                                CarouselState.current_index == idx,
                                "white",
                                "rgba(255, 255, 255, 0.5)"
                            ),
                            "cursor": "pointer",
                            "transition": "background-color 0.3s",
                        }
                    )
                ),
                style={
                    "position": "absolute",
                    "bottom": "15px",
                    "left": "50%",
                    "transform": "translateX(-50%)",
                    "display": "flex",
                    "gap": "8px",
                }
            ),

            style={
                "position": "relative",
                "width": "100%",
                "height": "500px",
                "overflow": "hidden",
                "background_color": "#808080", # Fondo gris por si la imagen tarda en cargar
            }
        )
    )