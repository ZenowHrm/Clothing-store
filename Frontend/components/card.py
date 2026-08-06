import reflex as rx
from theme import COLORS, hex_to_rgba

from Frontend.state.cardsutils import CardState

def product_card(product: dict) -> rx.Component:
    card = rx.card(
        rx.el.style(
            """
            @media (max-width: 600px) {
                .container-card {
                    width: 160px;
                    height: 310px;
                }
                .sect1 {
                    height: 130px
                }
                .tag {
                    padding: 2px 5px;
                    font-size: 0.7rem;
                }
                .tag-container {
                    bottom: 0.5rem;
                    left: 0.5rem;
                    gap: 3px
                }
                .textcard-container {
                    flex-direction: column;
                    justify-content: center;
                    align-items: end;
                }
                .card-button {
                    font-size: 0.6rem
                }
                .text-card{
                    font-size: 1rem
                }
            }
            """
        ),
        rx.link(
            rx.el.div(
                rx.card(
                    rx.image(
                        product.card_image_url,
                        style={
                            "width": "100%",
                            "height": "100%",
                            "object-fit": "cover",
                        }
                    ),
                    rx.el.div(
                        rx.cond(product.is_new, rx.text("New", class_name="tag", style={"background": "green", "color": "white", "padding": "5px 10px"}), rx.el.div()),
                        rx.cond(product.is_featured, rx.text("Featured", class_name="tag", style={"background": "gold", "color": "white", "padding": "5px 10px"}), rx.el.div()),
                        rx.cond(product.is_bestseller, rx.text("Bestseller", class_name="tag", style={"background": "purple", "color": "white", "padding": "5px 10px"}), rx.el.div()),
                        
                        class_name="tag-container",
                        style={
                            "position": "absolute",
                            "bottom": "1rem",
                            "left": "1rem",
                            "display": "flex",
                            "justify-content": "flex-start",
                            "gap": "10px"
                        }
                    ),
                    
                    class_name="sect1",
                    style={
                        "width": "100%",
                        "height": "260px",
                        "position": "relative",
                        "overflow": "hidden",
                        "padding": "0",
                    }
                ),
                rx.el.div(
                    rx.box(
                        rx.el.div(
                            rx.text(rx.el.b(product.title), class_name="text-card", style={"font-size": "1.25rem", "font-weight": "bold"}),
                            rx.text(product.attributes.prenda)
                        ),
                        rx.el.div(
                            rx.text(rx.el.b(product.price), class_name="text-card", style={"font-size": "1.5rem"}),
                            rx.text("USD", style={"font-size": "0.7rem"}),
                            style={
                                "display": "flex",
                                "flex-direction": "column",
                                "align-items": "end",
                                "justify-content": "flex-end"
                            }
                        ),
                        
                        class_name="textcard-container",
                        style={
                            "display": "flex",
                            "justify-content": "space-between",
                            "flex-direction": "row",
                            "align-items": "center",
                            "width": "100%"
                        }
                    ),
                    rx.button(
                        rx.icon("shopping_cart", size=20),
                        "Añadir al Carrito",
                        
                        class_name="card-button",
                        on_click=CardState.send_to_cart(product.id).prevent_default.stop_propagation,
                        style={
                            "width": "100%",
                            "background": COLORS["purple"],
                            "transition": "transform 0.2s ease, color 0.2s ease, background 0.2s ease",
                            "_hover": {
                                "transform": "scale(1.03)",
                                "background": hex_to_rgba(COLORS["purple"], 0.3),
                                "color": COLORS["purple"]
                            },
                            "_active": {
                                "background": hex_to_rgba(COLORS["purple"], 0.7),
                            }
                        }
                    ),
                    style={
                        "display": "flex",
                        "flex-direction": "column",
                        "justify-content": "space-between",
                        "flex-grow": "1",
                        "width": "100%",
                        "padding-top": "0.75rem",
                    }
                ),
                style={
                    "display": "flex",
                    "flex-direction": "column",
                    "width": "100%",
                    "height": "100%",
                    "justify-content": "space-between",
                }
            ),
            href=f"/gallery/{product.slug}",
            underline="none",
            color_scheme="gray",
            color="black",
            style={
                "width": "100%",
                "height": "100%",
                "display": "block",
            }
        ),
        
        class_name="container-card",
        style={
            "width": "300px",
            "height": "450px",
            "display": "flex",
            "flex-direction": "column",
            "overflow": "hidden",
            "transition": "outline 0.3s ease",
            "_hover": {
                "outline": f"5px solid {COLORS['purple']}"
            }
        }
    )
    
    return card

def card_shoping(product):
    card = rx.card(
        rx.el.div(
            rx.el.img(
                src=product.card_image_url,
                width="100%",
                height="100%",
                object_fit= "cover"
            ),
            
            style={
                "min-width": "60px",
                "width": "60px",
                "height": "60px",
                "border-radius": "10px",
                "overflow": "hidden"
            }
        ),
        rx.el.div(
            rx.text(product.title),
            rx.text(product.attributes.prenda, opacity=0.8, font_size="0.8rem"),
            
            style= {
                "color": COLORS["black"]
            }
        ),
        rx.el.div(
            rx.button(
                rx.icon("arrow_big_up"),
                on_click= CardState.send_to_cart(product["id"]),
                width="30px",
                height="20px",
                padding="5px",
            ),
            rx.input(
                value=CardState.cards_in_cart[product.id],
                type="number",
                width="2rem",
                height="30px",
                max_length=4,
            ),
            rx.button(
                rx.icon("arrow_big_down"),
                on_click= CardState.remove_to_cart(product["id"]),
                width="30px",
                height="20px",
                padding="5px",
            ),
            
            style= {
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
                "gap": "5px"
            }
        ),
        
        style= {
            "display": "flex",
            "flex-direction": "row",
            "align-items": "center",
            "gap": "10px"
        }
    )
    
    return card