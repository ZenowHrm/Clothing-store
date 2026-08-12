import reflex as rx

from theme import COLORS
from Frontend.components.layout import Menu
from Frontend.components.footer import Footer
from Backend.api.sendtodiscord import EnviarDiscord
from Frontend.state.contactvalues import ContactValues

def Contact() -> rx.Component:
    contacto = rx.el.div(
        rx.el.style(
            """
            @keyframes cambiarColor {
                0% {
                    background-color: transparent;
                    color: white
                }
                100% {
                    background-color: #FBFBFB;
                    color: #101010
                }
            }
            """
        ),
        rx.el.header(
            Menu(),
        
            style= {
                "position": "fixed",
                "width": "100%",
                "top": "0",
                "left": "0",
                "z-index": "9999",
                "animation": "cambiarColor linear both",
                "animation-timeline": "scroll(root)",
                "animation-range": "0px 200px"
            }
        ),
        rx.vstack(
            rx.text("Contact Us", font_size="3rem", font_weight="bold", text_shadow="0 0 10px #000000"),
            rx.text("Te intereza esta pagina? contactame para más información", font_size="1.2rem", color="white", text_align="center", text_shadow="0 0 10px #000000"),
            rx.form(
                rx.vstack(
                    rx.input(placeholder="Your Name", required=True, value=ContactValues.name, on_change=ContactValues.update_name, style={"width": "100%", "padding": "10px", "margin": "10px 0",}),
                    rx.input(placeholder="Your Email", type="email", required=True, value=ContactValues.email, on_change=ContactValues.update_email, style={"width": "100%", "padding": "10px", "margin": "10px 0"}),
                    rx.text_area(placeholder="Your Message", required=True, value=ContactValues.message, on_change=ContactValues.update_message, style={"width": "100%", "padding": "10px", "margin": "10px 0"}),
                    rx.button("Submit", type="submit", on_click=lambda e: ContactValues.send_webhook, style={"width": "100%", "background": "blue", "color": "white", "padding": "10px 20px", "border": "none", "cursor": "pointer"}),

                    style= {
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "width": "fit-content",
                        "background-color": COLORS["black"],
                        "min-width": "300px",
                        "padding": "1rem",
                        "border-radius": "25px"
                    }
                ),
                
                style= {
                    "width": "fit-content",
                }
            ),
            style={
                "max_width": "100%", 
                "height": "100dvh", 
                "margin": "0 auto", 
                "padding": "20px",
                "display": "flex",
                "justify-content": "center",
                "align-items": "center",
                "background-image": "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/wallpaper.png')",
                "background-size": "cover",
                "background-position": "center",
            }
        ),
        rx.el.footer(
            Footer(),
        )
    )
    
    return contacto