import reflex as rx
from Frontend.state.editor import EditorState
from Frontend.components.configdesing import retorno_editor

def editor_toolbar() -> rx.Component:
    barra = rx.el.div(
        rx.el.div(
            rx.el.div(
                retorno_editor(),
                
                on_mount= EditorState.cerrar_editor,
                style= {
                    "position": ["relative", "relative", "absolute"],
                    "top": "0",
                    "left": "0",
                    "background-color": rx.cond(EditorState.seccion_editor != "", "#2f353a", "transparent"),
                    "padding": rx.cond(EditorState.seccion_editor != "", "10px", "0px"),
                    "border-radius": ["8px 8px 0 0", "8px 8px 0 0", "0 8px 8px 0"],
                    "min-width": rx.cond(EditorState.seccion_editor != "", ["100%", "100%", "300px"], "0px"),
                    "height": ["auto", "auto", "100%"],
                    "z-index": "30",
                }
            ),
            
            style= {
                "position": "relative",
            }
        ),
        rx.el.div(
            rx.button(
                rx.icon("type_outline", size=15),
                "text",
                on_click= EditorState.add_text,
                background_color= rx.cond(EditorState.seccion_editor == "texto", "#046ebe", "#0090ff"),
                display="flex",
                flex_direction=["column", "column", "row"],
                align_items="center",
                gap=["4px", "4px", "8px"],
                height="auto",
                padding=["8px", "8px", "10px"],
                min_width="70px",
            ),
            rx.button(
                rx.icon("upload", size=15),
                "upload",
                on_click= EditorState.add_archivo_img,
                background_color= rx.cond(EditorState.seccion_editor == "imagen", "#046ebe", "#0090ff"),
                display="flex",
                flex_direction=["column", "column", "row"],
                align_items="center",
                gap=["4px", "4px", "8px"],
                height="auto",
                padding=["8px", "8px", "10px"],
                min_width="70px",
            ),
            rx.button(
                rx.icon("shapes", size=15),
                "shapes",
                on_click= EditorState.add_figura,
                background_color= rx.cond(EditorState.seccion_editor == "figura", "#046ebe", "#0090ff"),
                display="flex",
                flex_direction=["column", "column", "row"],
                align_items="center",
                gap=["4px", "4px", "8px"],
                height="auto",
                padding=["8px", "8px", "10px"],
                min_width="70px",
            ),
            rx.button(
                rx.icon("pencil_line", size=15),
                "draw",
                on_click= EditorState.modo_dibujo, 
                background_color= rx.cond(EditorState.seccion_editor == "dibujo", "#046ebe", "#0090ff"),
                display="flex",
                flex_direction=["column", "column", "row"],
                align_items="center",
                gap=["4px", "4px", "8px"],
                height="auto",
                padding=["8px", "8px", "10px"],
                min_width="70px",
            ),
            
            style= {
                "display": "flex",
                "flex-direction": ["row", "row", "column"],
                "justify-content": ["space-around", "space-around", "flex-start"],
                "padding": "10px",
                "gap": "10px",
            },
        ),
        
        style= {
            "display": "flex",
            "flex-direction": ["column", "column", "row-reverse"],
            "background-color": "#232b31",
        }
    )
    
    return barra