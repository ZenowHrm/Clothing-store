import reflex as rx
from Frontend.components.toolbardesing import editor_toolbar

def DesignPage():
    canva = rx.el.div(
        rx.el.div(
            
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.button(
                            rx.el.svg(
                                rx.el.path(
                                    fill="currentColor",
                                    d="m18.054 7.252-2.296-2.296a.75.75 0 0 1 1.06-1.06l2.83 2.828a1.75 1.75 0 0 1 0 2.475l-2.832 2.831a.75.75 0 0 1-1.06-1.06l2.219-2.22H8a4.25 4.25 0 0 0 0 8.5h4a.75.75 0 0 1 0 1.5H8a5.75 5.75 0 0 1 0-11.5h10c.018 0 .036 0 .054.002Z",
                                ),
                                class_name="x1lliihq x5yr21d xh8yej3",
                                width="24",
                                height="24",
                                view_box="0 0 24 24",
                                xmlns="http://www.w3.org/2000/svg",
                                transform="scale(-1, 1)",
                                transform_origin="center",
                            ),
                            on_click= rx.call_script("window.deshacer()"),
                        ),
                        rx.button(
                            rx.el.svg(
                                rx.el.path(
                                    fill="currentColor",
                                    d="m18.054 7.252-2.296-2.296a.75.75 0 0 1 1.06-1.06l2.83 2.828a1.75 1.75 0 0 1 0 2.475l-2.832 2.831a.75.75 0 0 1-1.06-1.06l2.219-2.22H8a4.25 4.25 0 0 0 0 8.5h4a.75.75 0 0 1 0 1.5H8a5.75 5.75 0 0 1 0-11.5h10c.018 0 .036 0 .054.002Z",
                                ),
                                class_name="x1lliihq x5yr21d xh8yej3",
                                width="24",
                                height="24",
                                view_box="0 0 24 24",
                                xmlns="http://www.w3.org/2000/svg",
                            ),
                            on_click= rx.call_script("window.rehacer()"),
                        ),
                        rx.button(
                            rx.icon("trash"),
                            on_click= rx.call_script("window.borrarSeleccionado()"),
                        ),
                    ),
                    rx.button(
                        "Guardar Imagen",
                        rx.icon("download", size=15),
                        
                        background_color= "#59CA79",
                        on_click= rx.call_script("window.exportarPNG('disingTeeVibes.png')")
                    ),
                    
                    style= {
                        "display": "flex",
                        "justify-content": ["space-between", "space-between", "flex-end"],
                        "padding": "10px",
                        "gap": "10px",
                        "background-color": "#0090ff",
                        "position": "relative",
                        "z-index": "10",
                    }
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.canvas(
                            id="lienzo-canva",
                            style= {
                                "width": "100%",
                                "height": "100%",
                            }
                        ),

                        id="canvas-wrapper",
                        style= {
                            "border-radius": "8px",
                            "width": "1000px",
                            "height": "1000px",
                            "transform-origin": "0 0",
                            "position": "absolute",
                            "will-change": "transform"
                        }
                    ),
                    
                    id="canvas-container",
                    style= {
                        "height": "calc(100% - 2rem)",
                        "width": "100%",
                        "position": "relative", 
                        "overflow": "hidden",  
                        "z-index": "1",
                        "touch-action": "none",
                    }
                ),
                
                style= {
                    "flex": "1",
                    "height": "100dvh",
                }
            ),
            editor_toolbar(),
            
            style= {
                "display": "flex",
                "flex-direction": ["column", "column", "row-reverse"],
                "justify-content": "flex-end",
                "width": "100%",
                "height": "100%",
                "position": "relative",
                "z-index": "20"
            }
        ),
        
        on_mount= rx.call_script("initCanvas(); setupZoomPan();"),
        style= {
            "width": "100dvw",
            "height": "100dvh",
            "overflow": "hidden"
        }
    )
    
    return canva