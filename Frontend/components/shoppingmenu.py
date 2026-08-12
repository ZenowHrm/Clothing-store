import reflex as rx
from Frontend.state.cardsutils import CardState
from Frontend.components.card import card_shoping
from theme import COLORS, hex_to_rgba

def Shopping_cart():
    shoppi = rx.drawer.root(
        rx.drawer.trigger(
            rx.button(
                rx.icon(tag="shopping_cart", size=15),
                "Carrito",
                style={
                    "display": "flex",
                    "justify-content": "center",
                    "background": "purple",
                    "padding": "5px 10px",
                    "min-width": "85px"
                }
            ),
        ),
        rx.drawer.overlay(z_index="999"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.el.div(
                    rx.el.div(
                        rx.text(
                            "Tu carrito",
                            color=COLORS["black"],
                            font_size="3rem",
                            text_align="right"
                        ),
                        style={"flex-shrink": "0"}
                    ),
                    
                    rx.el.div(
                        rx.cond(
                            CardState.cards_in_cart,
                            rx.el.div(
                                rx.el.div(
                                    rx.foreach(
                                        CardState.cart_products_details, 
                                        lambda c: card_shoping(c)
                                    ),
                                    style={
                                        "flex": "1",
                                        "min-height": "0",   
                                        "overflow-y": "auto",
                                        "display": "flex",
                                        "flex-direction": "column",
                                        "gap": "10px"
                                    }
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.text(CardState.total, color="black",font_size="2rem"),
                                        rx.text("Subtotal", color="black",opacity=0.8),
                                    ),
                                    rx.drawer.close(
                                        rx.button(
                                            "PAGAR PEDIDO",
                                            on_click=CardState.abrir_modal
                                        )
                                    ),
                                    
                                    style={
                                        "flex-shrink": "0",   
                                        "padding-top": "10px",
                                        "display": "flex",
                                        "flex-direction": "row",
                                        "align-items": "center",
                                        "justify-content": "space-between"
                                    }
                                ),
                                style={
                                    "flex": "1",
                                    "min-height": "0", 
                                    "display": "flex",
                                    "flex-direction": "column",
                                    "width": "100%",
                                }
                            ),
                            rx.el.div(
                                rx.text(
                                    "No hay nada en tu carrito",
                                    color=COLORS["black"],
                                    font_size="1.3rem"
                                ),
                                style={
                                    "width": "100%",
                                    "height": "100%",
                                    "display": "flex",
                                    "justify-content": "center",
                                    "align-items": "center"
                                }
                            )
                        ),
                        style={
                            "flex": "1",
                            "min-height": "0",    
                            "display": "flex",
                            "flex-direction": "column",
                            "width": "100%",
                        }
                    ),
                    
                    style={
                        "display": "flex",
                        "flex-direction": "column",
                        "height": "100%",
                        "width": "100%",
                    }
                ),
                
                top="auto",
                left="auto",
                height="100dvh",
                width=["80%", "30em", "30em"],
                padding="2em",
                background_color="white",
                style={
                    "display": "flex",
                    "flex-direction": "column",
                    "box-sizing": "border-box"
                }
            )
        ),
        direction="right",
    )
    
    modal_pago = rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title("¡Función no disponible!"),
            rx.dialog.description(
                "La acción que vas a realizar no está disponible en estos momentos, si te interesa la página puedes contactarme. ",
                rx.el.br(),
                rx.el.br(),
                "También puedes visitar mi ", 
                rx.link("portafolio", href="https://portfoliosantimy.onrender.com"), 
                " para ver más cosas interesantes y contactarte conmigo directamente.",
            ),
            rx.button(
                "Cerrar", 
                size="3", 
                on_click=CardState.cerrar_modal,
                margin="1rem 0 0 0"
            ),
        ),
        
        open=CardState.show_modal,
        on_open_change=CardState.cambiar_estado_modal,
    )
    
    return rx.fragment(shoppi, modal_pago)