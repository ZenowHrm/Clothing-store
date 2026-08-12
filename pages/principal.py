import reflex as rx
from theme import COLORS, hex_to_rgba

#----Estados
from Frontend.state.listaproductos import StoreState
#----Componentes
from Frontend.components.layout import Menu
from Frontend.components.footer import Footer
from Frontend.components.card import product_card


def Pagprincipal():
    
    pag = rx.el.div(
        rx.el.style(
            """
            * {
                padding: 0;
                margin: 0;
                box-sizing: border-box;
            }
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
            @keyframes flotarInfinito {
                0%, 100% {
                    /* Comienza y termina en su posición original */
                    transform: translateY(0);
                    animation-timing-function: ease-out;
                }
                50% {
                    /* En la mitad de la animación, sube 10 píxeles */
                    transform: translateY(-10px);
                    animation-timing-function: ease-in;
                }
            }
            
            @media (max-width: 600px) {
                .frase {
                    font-size: 1rem;
                }
                .titulo {
                    font-size: 4rem;
                }
                .section-we{
                    font-size: 1rem;
                }
                .we-titulo{
                    font-size: 3rem;
                }
                .we-redes_container{
                    flex-direction: column;
                    gap: 10px;
                }
                .titulo-sect2 {
                    font-size: 1.5rem;
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
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Si no existe en la calle, créalo tú.",
            
                        class_name="frase",
                        style= {
                            "font-size": "3rem"
                        }
                    ),
                    rx.el.h1(
                        "TeeVibes Store",
            
                        class_name="titulo",
                        style= {
                            "font-size": "7rem",
                            "font-family": "'Lucida Console', 'Courier New', monospace",
                        }
                    ),
                    rx.el.div(
                        rx.link(
                            rx.button(
                                "Customizar Pieza",
                                rx.icon("arrow_right", size=20),
                
                                style= {
                                    "background": "rgba(255, 255, 255, 0.22)",
                                    "box-shadow": "0 4px 30px rgba(0, 0, 0, 0.1)",
                                    "backdrop-filter": "blur(11.6px)",
                                    "-webkit-backdrop-filter": "blur(11.6px)",
                                    "border": "1px solid rgba(255, 255, 255, 0.3)",
                                    "padding": "20px",
                                    "font-size": "1rem"
                                }
                            ),
                            
                            href= "/design"
                        ),
                        rx.link(
                            rx.button(
                                "contáctanos",
                
                                style= {
                                    "box-shadow": "0px 0px 20px #222",
                                    "background": hex_to_rgba(COLORS["purple"], 0.8),
                                    "padding": "20px",
                                    "font-size": "1rem"
                                }
                            ),
                            
                            href= "/contact"
                        ),
            
                        style= {
                            "display": "flex",
                            "gap": "10px"
                        }
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.image(
                                    "/camisa.svg",
            
                                    style= {
                                        "width": ["25px","30px"],
                                        "height": ["25px","30px"],
                                    }
                                ),
                                rx.el.div(
                                    rx.text(
                                        "Prenda",
            
                                        style= {
                                            "font-size": "0.6rem", 
                                            "opacity": "0.8",
                                        }
                                    ),
                                    rx.select.root(
                                        rx.select.trigger(
                                            color=COLORS["black"],                              
                                            bg=COLORS["white"],
                                            font_size="0.8rem",
                                            padding="0",
                                            width=["65px", "77px"],
                                        ),
            
                                        rx.select.content(
                                            rx.select.item("Todas", value="todas"),
                                            rx.foreach(
                                                StoreState.prendas_disponibles,
                                                lambda c: rx.select.item(f"{c}", value=c)
                                            ),
            
                                            bg=COLORS["white"],
                                            color=COLORS["black"],
                                            border="1px solid #333",
                                            font_size="0.8rem"
                                        ),
            
                                        value= StoreState.selected_prenda,
                                        on_change= StoreState.set_prenda,
            
                                    ),
            
                                    style= {
                                        "padding": "0 10px"
                                    }
                                ),
            
                                style= {
                                    "display": "flex",
                                    "justify-content": "center",
                                    "align-items": "center",
                                    "width": "fit-content"
            
                                }
                            ),
                            rx.el.div(
                                rx.image(
                                    "/cuello.svg",
            
                                    style= {
                                        "width": ["25px","30px"],
                                        "height": ["25px","30px"],
                                    }
                                ),
                                rx.el.div(
                                    rx.text(
                                        "Corte",
            
                                        style= {
                                            "font-size": "0.6rem", 
                                            "opacity": "0.8",
                                        }
                                    ),
                                    rx.select.root(
                                        rx.select.trigger(
                                            color=COLORS["black"],                              
                                            bg=COLORS["white"],
                                            font_size="0.8rem",
                                            padding="0",
                                            width=["65px", "77px"]
                                        ),
            
                                        rx.select.content(
                                            rx.select.item("Todas", value="todas"),
                                            rx.foreach(
                                                StoreState.cortes_disponibles,
                                                lambda c: rx.select.item(f"{c}", value=c)
                                            ),
            
                                            bg=COLORS["white"],
                                            color=COLORS["black"],
                                            border="1px solid #333",
                                            font_size="0.8rem"
                                        ),
            
                                        value= StoreState.selected_corte,
                                        on_change= StoreState.set_corte,
                                    ),
            
                                    style= {
                                        "padding": "0 10px"
                                    }
                                ),
            
                                style= {
                                    "display": "flex",
                                    "justify-content": "center",
                                    "align-items": "center",
                                    "width": "fit-content"
            
                                }
                            ),
                            rx.el.div(
                                rx.image(
                                    "/paleta.svg",
            
                                    style= {
                                        "width": ["25px","30px"],
                                        "height": ["25px","30px"],
                                    }
                                ),
                                rx.el.div(
                                    rx.text(
                                        "Color",
            
                                        style= {
                                            "font-size": "0.6rem", 
                                            "opacity": "0.8",
                                        }
                                    ),
                                    rx.select.root(
                                        rx.select.trigger(
                                            color=COLORS["black"],                              
                                            bg=COLORS["white"],
                                            font_size="0.8rem",
                                            padding="0",
                                            width=["65px", "77px"],
                                        ),
            
                                        rx.select.content(
                                            rx.select.item("Todas", value="todas"),
                                            rx.foreach(
                                                StoreState.colores_disponibles,
                                                lambda c: rx.select.item(f"{c}", value=c)
                                            ),
            
                                            bg=COLORS["white"],
                                            color=COLORS["black"],
                                            border="1px solid #333",
                                            font_size="0.8rem"
                                        ),
            
                                        value= StoreState.selected_color,
                                        on_change= StoreState.set_color,
            
                                    ),
            
                                    style= {
                                        "padding": "0 10px"
                                    }
                                ),
            
                                style= {
                                    "display": "flex",
                                    "justify-content": "center",
                                    "align-items": "center",
                                    "width": "fit-content"
            
                                }
                            ),
                            rx.el.div(
                                rx.image(
                                    "/regla.svg",
            
                                    style= {
                                        "width": ["25px","30px"],
                                        "height": ["25px","30px"],
                                    }
                                ),
                                rx.el.div(
                                    rx.text(
                                        "Tallas",
            
                                        style= {
                                            "font-size": "0.6rem", 
                                            "opacity": "0.8",
                                        }
                                    ),
                                    rx.select.root(
                                        rx.select.trigger(
                                            color=COLORS["black"],                              
                                            bg=COLORS["white"],
                                            font_size="0.8rem",
                                            padding="0",
                                            width=["65px", "77px"],
                                        ),
            
                                        rx.select.content(
                                            rx.select.item("Todas", value="todas"),
                                            rx.foreach(
                                                StoreState.tallas_disponibles,
                                                lambda c: rx.select.item(f"{c}", value=c)
                                            ),
            
                                            bg=COLORS["white"],
                                            color=COLORS["black"],
                                            border="1px solid #333",
                                            font_size="0.8rem"
                                        ),
            
                                        value= StoreState.selected_talla,
                                        on_change= StoreState.set_talla,
            
                                    ),
            
                                    style= {
                                        "padding": "0 10px"
                                    }
                                ),
            
                                style= {
                                    "display": "flex",
                                    "justify-content": "center",
                                    "align-items": "center",
                                    "width": "fit-content",
                                }
                            ),
                            
                            style= {
                                "display": "flex",
                                "flex-wrap": "wrap",
                                "justify-content": "space-around",
                                "flex": "1"
                            }
                        ),
                        rx.el.a(rx.button(rx.icon("search")), _hover={"text-decoration": "underline"}, href="/gallery"),
                        
                        on_mount= StoreState.cargar_filtros,
                        style= {
                            "background": COLORS["white"],
                            "width": "100%",
                            "min-height": "1rem",
                            "margin": "1rem 0",
                            "border-radius": "20px",
                            "color": "#000000",
                            "font-family": "'Lucida Console', 'Courier New', monospace",
                            "padding": "0.5rem 1rem",
                            "display": "flex",
                            "align-items": "center"
                        }
                    ),
            
            
            
                ),
            
                style= {
                    "flex": "1",
                    "display": "flex",
                    "flex-direction": "column",
                    "justify-content": "center",
                    "margin": "1rem"
                }
            ),
            rx.el.div(
                rx.el.p("Ver mas"),
                rx.icon(tag="chevron_down", size=20),
            
                style= {
                    "display": "inline-block",
                    "animation-name": "flotarInfinito",
                    "animation-duration": "2s",
                    "animation-iteration-count": "infinite",
                    "animation-fill-mode": "both",
                    "opacity": "0.6",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center",
                    "padding": "10px"
                }
            ),
            
            style= {
                "width": "100%",
                "height": "100dvh",
                "background-image": "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/background.png')",
                "background-size": "cover",
                "background-position": "center",
                "display": "flex",
                "flex-direction": "column",
                "justify-content": "center",
                "align-items": "center",
            }
        ),
        rx.el.section(
            #Sobre nosotros
            rx.el.div(
                rx.el.h3(
                    rx.el.b("Sobre nosotros"),
        
                    style= {
                        "text-align": "center",
                        "color": COLORS["purple"]
                    }
                ),
                rx.el.h2(
                    "TeeVibes Store",
        
                    class_name= "we-titulo",
                    style= {
                        "font-size": "5rem",
                        "text-align": "center",
                    }
                ),
                rx.el.p(
                    'Somos una marca de ropa enfocada en la Generación Z y jóvenes creativos. Nosotros ponemos la estructura y el usuario le inyecta su propio "estilo" o diseño. No seguimos temporadas, lanzamos Drops. La estética mezcla el minimalismo urbano con gráficos experimentales.',
        
                    style= {
                        "padding": "0 0 1rem 0"
                    }
                ),
                rx.el.div(
                    rx.el.h4(
                        rx.el.b("Estamos en Caracas"),
        
                        style= {
                            "font-size": "2rem"
                        }
                    ),
                    rx.el.p(
                        "Caracas es la capital y ciudad más poblada de Venezuela. Desde el siglo XIX, ha sido el epicentro del poder político de la nación venezolana. Se encuentra en la Región Capital de Venezuela a 12 km del mar Caribe, dentro de un valle montañoso en el que cursa el río Guaire.",
        
                        style= {
                            "padding": "0 0 1rem 0"
                        }
                    ),
        
                    style= {
                        "width": "80%"
                    }
                ),
        
                style= {
                    "max-width": "1200px",
                    "padding": "1rem",
                    "display": "flex",
                    "flex-direction": "column",
                    "align-items": "center"
                }
            ),
        
            class_name= "section-we",
            style= {
                "width": "100%",
                "background": COLORS["white"],
                "color": COLORS["black"],
                "font-size": "1.5rem",
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
                "padding": "2rem 1rem"
            }
        ),
        rx.el.section(
            #Nuevo y destacado
            rx.el.div(
                rx.el.h3(
                    rx.el.b("Nuevo y Destacado"),
                
                    class_name="titulo-sect2",
                    style= {
                        "font-size": "3rem",
                        "color": COLORS["black"],
                        "text-align": "start",
                        "padding": "0 1rem"
                    }
                ),
                
                style= {
                    "width": "100%",
                    "max-width": "1300px",
                }
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(StoreState.productos_nuevos_destacados, product_card),
                    
                    style= {
                        "display": "flex",
                        "flex-wrap": "wrap",
                        "gap": "1rem",
                        "justify-content": "center"
                    }
                ),
                
                on_mount=StoreState.load_main_products,
                style= {
                    "max-width": "1300px",
                }
            ),
            rx.link(
                rx.button(
                    "Ver mas",
                    
                    on_click=StoreState.set_section("nuevo"),
                    style= {
                        "padding": "1.5rem 3rem",
                        "margin": "1rem",
                        "font-size": "2rem",
                        "background": hex_to_rgba(COLORS["purple"], 0.8),
                        "_hover": {
                            "background": hex_to_rgba(COLORS["purple"], 0.6)
                        }
                    }
                ),
                
                href="/gallery"
            ),
            
            style= {
                "width": "100%",
                "background": COLORS["white"],
                "display": "flex",
                "align-items": "center",
                "flex-direction": "column",
                "padding": "2rem 0"
            }
        ),
        rx.el.section(
            #wallpaper
            rx.el.div(
                rx.el.div(
                    rx.image("/wallpaper.png", style={"object-fit": "cover","position": "absolute","top": "0","left": "0","z-index": "5"}),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.text(rx.el.b("TeeVibes"), style={"font-size": "3rem", "text-align": "center", "text-shadow": "0 0 5px #000000"}),
                        rx.text("Mucho mas que solo ropa", style={"font-size": "2rem", "text-align": "center", "text-shadow": "0 0 5px #000000"}),
                    ),
                    
                    style= {
                        "padding": "1rem 2rem",
                        "z-index": "6",
                        "display": "flex",
                        "justify-content": "center",
                        "width": "100%",
                        "height": "100%",
                        "background": f"linear-gradient({hex_to_rgba(COLORS["purple"], 0.5)}, {hex_to_rgba(COLORS["purple"], 0.5)})"
                    }
                ),
                
                style= {
                    "width": "90%",
                    "max-width": "1000px",
                    "overflow": "hidden",
                    "display": "flex",
                    "align-items": "center",
                    "position": "relative",
                    "border-radius": "50px"
                }
            ),
            
            style= {
                "background": "white",
                "display": "flex",
                "justify-content": "center",
            }
        ),
        rx.el.section(
            #Mas vendido
            rx.el.div(
                rx.el.h3(
                    rx.el.b("Mas Vendido"),
            
                    class_name="titulo-sect2",
                    style= {
                        "font-size": "3rem",
                        "color": COLORS["black"],
                        "text-align": "start",
                        "padding": "0 1rem"
                    }
                ),
            
                style= {
                    "width": "100%",
                    "max-width": "1300px",
                }
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(StoreState.productos_mas_vendidos, product_card),
            
                    style= {
                        "display": "flex",
                        "flex-wrap": "wrap",
                        "gap": "1rem",
                        "justify-content": "center"
                    }
                ),
            
                on_mount=StoreState.load_main_products,
                style= {
                    "max-width": "1300px",
                }
            ),
            rx.link(
                rx.button(
                    "Ver mas",
                
                    on_click=StoreState.set_section("mas_vendido"),
                    style= {
                        "padding": "1.5rem 3rem",
                        "margin": "1rem",
                        "font-size": "2rem",
                        "background": hex_to_rgba(COLORS["purple"], 0.8),
                        "_hover": {
                            "background": hex_to_rgba(COLORS["purple"], 0.6)
                        }
                    }
                ),
                
                href="/gallery"
            ),
        
            style= {
                "width": "100%",
                "background": COLORS["white"],
                "display": "flex",
                "align-items": "center",
                "flex-direction": "column",
                "padding": "2rem 0"
            }
        ),
        rx.el.section(
            #Contactanos
            rx.el.text(
                "Contactanos",
                
                style= {
                    "font-size": "3rem"
                }
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h5(
                        rx.el.b("Redes"),
                        style={
                            "color": COLORS["purple"]
                        }
                    ),
                    rx.el.div(
                        rx.el.p(
                            rx.image("https://cdn-icons-png.flaticon.com/512/1384/1384031.png", width="1.5rem", height="1.5rem"),
                            " @teevibes.store",
            
                            style= {
                                "display": "flex",
                                "gap": "10px",
                                "align-items": "center"
                            }
                        ),
                        rx.el.p(
                            rx.image("https://cdn-icons-png.flaticon.com/512/2175/2175193.png", width="1.5rem", height="1.5rem"),
                            " TeeVibes Official",
            
                            style= {
                                "display": "flex",
                                "gap": "10px",
                                "align-items": "center"
                            }
                        ),
                        rx.el.p(
                            rx.icon("message-circle"),
                            " +58 412-5550199",
            
                            style= {
                                "display": "flex",
                                "gap": "10px",
                                "align-items": "center"
                            }
                        ),
            
                        style= {
                            "display": "flex",
                            "flex-direction": "column",
                            "gap": "10px"
                        }
                    )
                ),
                rx.el.div(
                    rx.el.h5(
                        rx.el.b("Horarios de atención"),
                        style={
                            "color": COLORS["purple"]
                        }
                    ),
                    rx.el.div(
                        rx.el.p(
                            rx.icon("calendar"),
                            " Lunes a Viernes: 9:00 AM - 6:00 PM",
            
                            style= {
                                "display": "flex",
                                "gap": "10px",
                                "align-items": "center"
                            }
                        ),
                        rx.el.p(
                            rx.icon("clock"),
                            " Sábados: 10:00 AM - 4:00 PM",
            
                            style= {
                                "display": "flex",
                                "gap": "10px",
                                "align-items": "center"
                            }
                        ),
                        rx.el.p(
                            rx.icon("shopping-bag"),
                            " Tienda Online: 24/7",
            
                            style= {
                                "display": "flex",
                                "gap": "10px",
                                "align-items": "center"
                            }
                        ),
            
                        style= {
                            "display": "flex",
                            "flex-direction": "column",
                            "gap": "10px"
                        }
                    )
                ),
            
                class_name= "we-redes_container",
                style={
                    "display": "flex",
                    "flex-direction": "row",
                    "justify-content": "space-between",
                    "width": "100%",
                    "max-width": "700px",
                    "padding": "1rem",
                }
            ),
            
            style= {
                "background": f"linear-gradient({hex_to_rgba(COLORS["white"], 0.9)}, {hex_to_rgba(COLORS["white"], 0.8)}), url('/icons.png')",
                "background-size": "cover",
                "background-position": "center",
                "background-attachment": "fixed",
                "display": "flex",
                "flex-direction": "column",
                "align-items": "center",
                "width": "100%",
                "padding": "2rem 1rem",
                "color": COLORS["black"],
            }
        ),
        
        rx.el.footer(
            Footer(),
        )
    )
    
    return pag 