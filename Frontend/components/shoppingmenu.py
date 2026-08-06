import reflex as rx
from Frontend.state.cardsutils import CardState
from Frontend.components.card import card_shoping

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
                rx.box(
                    rx.foreach(
                        CardState.cart_products_details, 
                        lambda c: card_shoping(c),
                    ),
                    
                    style= {
                        "width": "100%",
                        "overflow-y": "scroll"
                    }
                ),
                
                top="auto",
                left="auto",
                height="100dvh",
                width="20em",
                padding="2em",
                background_color="white",
                
            )
        ),
        
        direction="right",
    )
    
    return shoppi