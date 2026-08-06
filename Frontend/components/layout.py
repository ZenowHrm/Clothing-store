import reflex as rx
from theme import COLORS, hex_to_rgba
from Frontend.components.logo import Logo
from Frontend.state.navmenu import MenuState
from Frontend.components.shoppingmenu import Shopping_cart

def Menu() -> rx.Component:
    menu = rx.el.div(
        rx.el.style(
            """
            .menu-btn {
                display: none;
            }
            .overlay {
                display: none;
            }
            
            @media (max-width: 600px) {
                .header-container {
                    padding: 1rem 1.5rem !important; 
                }
                .menu-btn {
                    display: block;
                    cursor: pointer;
                }
                .nav-container {
                    position: fixed;
                    top: 0;
                    left: -100%; 
                    width: 60%;
                    height: 100dvh;
                    background: white;
                    color: black;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    transition: left 0.3s ease-in-out; 
                    box-shadow: 2px 0 10px rgba(0,0,0,0.2);
                }
                .nav-container.open {
                    left: 0; 
                }
                .ul-container {
                    flex-direction: column !important;
                    gap: 2rem !important;
                    font-size: 1.2rem;
                }
                .overlay.open {
                    display: block;
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100vw;
                    height: 100dvh;
                    background: rgba(0,0,0,0.4);
                }
            }
            """
        ),
        rx.el.div(
            class_name=rx.cond(MenuState.is_open, "overlay open", "overlay"),
            on_click=MenuState.toggle_menu
        ),
        rx.el.div(
            rx.icon(
                tag="menu", 
                class_name="menu-btn", 
                size=28, 
                on_click=MenuState.toggle_menu
            ),
            rx.el.a(
                Logo(COLORS["white"], COLORS["black"]),
                href="/",
                style= {
                    "width": "35px",
                    "height": "35px",
                    "border-radius": "9999px",
                    "overflow": "hidden",
                }
            ),
            style= {
                "display": "flex",
                "align-items": "center",
                "gap": "15px"
            }
        ),
        rx.el.nav(
            rx.el.ul(
                rx.el.li(rx.el.a("Menú principal", _hover={"text-decoration": "underline"}, href="/", on_click=MenuState.toggle_menu)),
                rx.el.li(rx.el.a("Catalogo", _hover={"text-decoration": "underline"}, href="/gallery", on_click=MenuState.toggle_menu)),
                rx.el.li(rx.el.a("Diseñar", _hover={"text-decoration": "underline"}, href="/design", on_click=MenuState.toggle_menu)),
                rx.el.li(rx.el.a("Contacto", _hover={"text-decoration": "underline"}, href="/contact", on_click=MenuState.toggle_menu)),
                
                class_name="ul-container",
                style= {
                    "display": "flex",
                    "flex-direction": "row",
                    "gap": "1rem",
                    "padding": "0",
                    "list-style": "none"
                }
            ),
            class_name=rx.cond(MenuState.is_open, "nav-container open", "nav-container"),
        ),
        Shopping_cart(),
        
        class_name="header-container",
        style={
            "display": "flex",
            "justify-content": "space-between",
            "align-items": "center",
            "padding": "1rem 5rem",
            "width": "100%",
            "max-width": "1000px",
            "font-size": "1rem",
            "margin": "auto",
        }
    )
    
    return menu