import reflex as rx
from theme import COLORS, hex_to_rgba

from Frontend.components.logo import Logo

def Footer() -> rx.Component:
    
    footer = rx.el.div(
        rx.el.style(
            """
            @media (max-width: 450px) {
                .logo-footer_container{
                    display: flex;
                    flex-direction: row;
                }
                .logo-footer {
                    order: 99;
                    position: relative;
                    right: 100px;
                    top: 100px
                }
                .logo-footer svg{
                    width: 230px;
                    height: 230px;
                }
            }
            """
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    Logo(hex_to_rgba(COLORS["purple"], 0), COLORS["white"]),
                    
                    class_name="logo-footer",
                    style= {
                        "width": "100px",
                        "height": "100px"
                    }
                ),
                rx.el.p(
                    'Somos una marca de moda urbana para la Generación Z y mentes creativas bajo el lema "Tu estética, tus reglas". Más que prendas, ofrecemos lienzos en blanco.',

                    style= {
                        "font-size": "0.8rem",
                        "color": hex_to_rgba(COLORS["white"], 0.7),
                    }
                ),
                
                class_name="logo-footer_container",
                style= {
                    "flex": "1",
                    "min-width": "200px",
                    "display": "flex",
                    "flex-direction": "column",
                }
            ),
            rx.el.div(
                rx.el.p(
                    "Servicios"
                    
                ),
                rx.el.p(
                    "Personalización", rx.el.br(),
                    "Venta", rx.el.br(),
                    "Impresión", rx.el.br(),
                    "Estampado", rx.el.br(),
                    "Asesoría", rx.el.br(),
                    "Fabricación",
                    
                    style= {
                        "font-size": "0.8rem",
                        "color": hex_to_rgba(COLORS["white"], 0.7),
                    }
                ),
                
                style= {
                    "flex": "1",
                    "min-width": "200px",
                }
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.p("Redes"),
                        rx.el.div(
                            rx.el.p(
                                "@teevibes.store",
                
                                style= {
                                    "display": "flex",
                                    "align-items": "center"
                                }
                            ),
                            rx.el.p(
                                "TeeVibes Official",
                
                                style= {
                                    "display": "flex",
                                    "align-items": "center"
                                }
                            ),
                            rx.el.p(
                                "+58 412-5550199",
                
                                style= {
                                    "display": "flex",
                                    "align-items": "center"
                                }
                            ),
                
                            style= {
                                "display": "flex",
                                "flex-direction": "column",
                                "font-size": "0.8rem",
                                "color": hex_to_rgba(COLORS["white"], 0.7),
                            }
                        )
                    ),
                    rx.el.div(
                        rx.el.p("Horarios de atención"),
                        rx.el.div(
                            rx.el.p(
                                "Lunes a Viernes: 9:00 AM - 6:00 PM",
                
                                style= {
                                    "display": "flex",
                                    "align-items": "center"
                                }
                            ),
                            rx.el.p(
                                "Sábados: 10:00 AM - 4:00 PM",
                
                                style= {
                                    "display": "flex",
                                    "align-items": "center"
                                }
                            ),
                            rx.el.p(
                                "Tienda Online: 24/7",
                
                                style= {
                                    "display": "flex",
                                    "align-items": "center"
                                }
                            ),
                
                            style= {
                                "display": "flex",
                                "flex-direction": "column",
                                "font-size": "0.8rem",
                                "color": hex_to_rgba(COLORS["white"], 0.7),
                            }
                        ),
                        
                        style= {
                            "margin": "10px 0 0 0"
                        }
                    ),

                    style={
                        "display": "flex",
                        "flex-direction": "column",
                        "justify-content": "space-between"
                    }
                ),
                
                style= {
                    "flex": "1",
                    "min-width": "200px",
                }
            ),
            
            style= {
                "max-width": "1000px",
                "display": "flex",
                "justify-content": "space-between",
                "gap": "10px",
                "flex-wrap": "wrap",
            }
        ),
        rx.el.div(
            rx.el.p(
                "© 2026 Santiago Maya. Todos los derechos reservados.",
                
                style= {
                    "color": hex_to_rgba(COLORS["white"], 0.5),
                    "font-size": "1rem",
                    "padding": "1rem 0 0 0",
                    "text-align": "center"
                }
            )
        ),
        
        style= {
            "display": "flex",
            "flex-direction": "column",
            "align-items": "center",
            "width": "100%",
            "padding": "2rem",
            "background-image": f"linear-gradient({hex_to_rgba(COLORS["purple"], 0.9)}, {hex_to_rgba(COLORS["purple"], 0.8)}), url('https://img.magnific.com/foto-gratis/fondo-blanco-sucio-cemento-natural-o-textura-antigua-piedra-como-pared-patron-retro-banner-pared-conceptual-grunge-material-o-construccion_1258-21333.jpg?semt=ais_test_b&w=740&q=80')"
        }
    )
    
    return footer