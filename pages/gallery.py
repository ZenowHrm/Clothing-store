import reflex as rx
from theme import COLORS, hex_to_rgba

#----States
from Frontend.state.listaproductos import StoreState
#----Componentes
from Frontend.components.footer import Footer
from Frontend.components.layout import Menu
from Frontend.components.carrusel import Carrusel
from Frontend.components.card import product_card

def crear_sections():
    elementos = {
        "Prenda": [StoreState.prendas_disponibles, StoreState.selected_prenda, StoreState.set_prenda],
        "Corte": [StoreState.cortes_disponibles, StoreState.selected_corte, StoreState.set_corte],
        "Color": [StoreState.colores_disponibles, StoreState.selected_color, StoreState.set_color],
        "Tallas": [StoreState.tallas_disponibles, StoreState.selected_talla, StoreState.set_talla],
    }
    
    def esquema(i):
        return rx.el.div(
            rx.text(i, font_size="0.8rem", color=COLORS["purple"]),
            rx.select.root(
                rx.select.trigger(
                    color=COLORS["black"],                              
                    bg=COLORS["white"],
                    font_size="1rem",
                    padding="5px",
                    width=["59px", "90px", "90px"],
                    border="solid 1px #000000"
                ),

                rx.select.content(
                    rx.select.item("Todas", value="todas"),
                    rx.foreach(
                        elementos[i][0],
                        lambda c: rx.select.item(f"{c}", value=c)
                    ),

                    bg=COLORS["white"],
                    color=COLORS["black"],
                    border="1px solid #333",
                    font_size="1rem"
                ),

                value= elementos[i][1],
                on_change= elementos[i][2],
            )
        )
    
    section = rx.el.div(
        *[esquema(c) for c in elementos],
        rx.el.div(
            rx.text("Seccion", font_size="0.8rem", color=COLORS["purple"]),
            rx.select.root(
                rx.select.trigger(
                    color=COLORS["black"],                              
                    bg=COLORS["white"],
                    font_size="1rem",
                    padding="5px",
                    width=["100%", "90px", "90px"],
                    border="solid 1px #000000"
                ),

                rx.select.content(
                    rx.select.item("Todas", value="todas"),
                    rx.select.item("Nuevo", value="nuevo"),
                    rx.select.item("Destacado", value="destacado"),
                    rx.select.item("Mas vendido", value="mas_vendido"),

                    bg=COLORS["white"],
                    color=COLORS["black"],
                    border="1px solid #333",
                    font_size="1rem"
                ),

                value= StoreState.selected_section,
                on_change= StoreState.set_section,
            ),
            
            flex=["1", "0", "0"]
        ),
        
        flex_direction= "row",
        style= {
            "display": "flex",
            "flex": "1",
            "flex-wrap": "wrap",
            "color": COLORS["black"],
            "gap": "1rem"
        }
    )
    
    return section

def Galeria():
    gal = rx.el.div(
        rx.el.style(
            """
            body {
            background-color: white;
            scrollbar-width: thin;
            scrollbar-color: rgba(150, 150, 150, 0.4) transparent;
            }
            
            ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
            }
            
            ::-webkit-scrollbar-track {
            background: transparent;
            }
            
            ::-webkit-scrollbar-thumb {
            background: rgba(150, 150, 150, 0.4);
            border-radius: 10px;
            }
            
            ::-webkit-scrollbar-thumb:hover {
            background: rgba(150, 150, 150, 0.7);
            }
            """
        ),
        rx.el.header(
            Menu(),
        
            style= {
                "position": "sticky",
                "width": "100%",
                "top": "0",
                "left": "0",
                "z-index": "9999",
                "background": COLORS["white"],
                "color": COLORS["black"]
            }
        ),
        rx.el.section(
            #carrusel
            Carrusel()
        ),
        rx.el.section(
            #catalogo
            rx.el.div(
                crear_sections(),
                rx.button(
                    rx.icon("search"),
                    
                    on_click=StoreState.load_products
                ),
                
                on_mount= StoreState.cargar_filtros,
                style={
                    "width": "100%",
                    "max-width": "1300px",
                    "padding": "1rem",
                    "display": "flex",
                    "justify-content": "space-between",
                    "align-items": "end",
                    "gap": "10px"
                }
            ),
            rx.el.div(
                rx.el.div(
                    rx.cond(StoreState.products, rx.foreach(StoreState.products, product_card), rx.text("No hay resultados", color="black",font_size=["2rem","5rem","5rem"],width="100%",height="100%",text_align="center")),
                    style= {
                        "display": "flex",
                        "flex-wrap": "wrap",
                        "gap": "1rem",
                        "justify-content": "center"
                    }
                ),
            
                on_mount=StoreState.load_products,
                style= {
                    "max-width": "1300px",
                }
            ),
            
            style= {
                "width": "100%",
                "min-height": "100dvh",
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
                "background": "white"
            }
        ),
        rx.el.footer(
            #footer
            Footer(),
        )
        
    )
    
    return gal