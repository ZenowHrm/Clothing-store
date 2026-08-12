import reflex as rx
from Frontend.state.editor import EditorState

def retorno_editor() -> rx.Component:
    retorno = rx.match(
        EditorState.seccion_editor,
        ("texto", texto_toolbar()),
        ("imagen", imagen_toolbar()),
        ("figura", figura_toolbar()),
        ("dibujo", dibujo_toolbar()),
        rx.box()
    )
    return retorno


def texto_toolbar() -> rx.Component:
    return rx.vstack(
        rx.heading("Texto", size="4", margin_bottom="2"),
        rx.button(
            "Agregar Texto",
            on_click=EditorState.agregar_texto,
            width="100%",
            cursor="pointer"
        ),
        rx.divider(margin_y="3"),
        rx.text(
            "Seleccione un texto a cambiar:", 
            size="2", 
            color_scheme="gray", 
            weight="medium"
        ),
        
        rx.select(
            EditorState.FuentesDisponibles,
            placeholder="Cambiar fuente...",
            on_change=EditorState.cambiar_fuente,
            width="100%",
        ),
        
        rx.hstack(
            rx.text("Color:", size="2"),
            rx.input(
                type="color",
                on_change=EditorState.cambiar_color,
                width="100%",
                height="35px", 
                padding="0",  
                cursor="pointer",
                border_radius="md",
                border="1px solid var(--gray-5)", 
            ),
            width="100%",
            align_items="center",
            spacing="3"
        ),
        
        width="100%",
        align_items="stretch",
        spacing="3"
    )


def imagen_toolbar() -> rx.Component:
    return rx.vstack(
        rx.heading("Imagen", size="4", margin_bottom="2"),
        rx.box(
            rx.input(
                type="file",
                accept="image/*",
                id="input-imagen-editor",
                on_change=EditorState.agregar_imagen,
                opacity="0",
                position="absolute",
                top="0",
                left="0",
                width="100%",
                height="100%",
                cursor="pointer",
                z_index="1"
            ),
            rx.vstack(
                rx.icon("image", size=30, color="gray"),
                rx.text(
                    "Arrastre aquí o seleccione un archivo", 
                    size="2", 
                    color="gray", 
                    text_align="center"
                ),
                align_items="center",
                justify="center",
                width="100%",
            ),
            position="relative",
            border="2px dashed var(--gray-7)",
            border_radius="md",
            padding="2em",
            width="100%",
            bg="var(--gray-2)",
            _hover={"bg": "var(--gray-3)"}, 
        ),
        width="100%",
        align_items="stretch"
    )


def figura_toolbar() -> rx.Component:
    return rx.vstack(
        rx.heading("Figura", size="4", margin_bottom="2"),
        
        rx.text("Forma", size="2", weight="bold"),
        rx.select(
            EditorState.FigurasDisponibles,
            value=EditorState.figura_seleccionada,
            on_change=EditorState.set_figura_value,
            name="figura",
            width="100%"
        ),
        
        rx.hstack(
            rx.vstack(
                rx.text("Color", size="2", weight="bold"),
                rx.input(
                    type="color",
                    value=EditorState.color_figura,
                    on_change=EditorState.set_color_value,
                    name="color",
                    height="2.5em",
                    padding="0",
                    cursor="pointer",
                    width="100%"
                ),
                width="100%"
            ),
            rx.vstack(
                rx.text("Relleno", size="2", weight="bold"),
                rx.checkbox(
                    "Hueco",
                    on_change=EditorState.set_hueco_value,
                    name="hueco",
                    size="2"
                ),
                justify="center",
                height="100%"
            ),
            width="100%",
            spacing="4"
        ),
        
        rx.button(
            "Agregar Figura", 
            type="submit",
            on_click=EditorState.agregar_figura,
            width="100%",
            margin_top="3",
            cursor="pointer"
        ),
        width="100%",
        align_items="stretch",
        spacing="3"
    )


def dibujo_toolbar() -> rx.Component:
    return rx.vstack(
        rx.heading("Dibujo", size="4", margin_bottom="2"),
        rx.button(
            "Modo Dibujo",
            on_click=EditorState.iniciar_dibujo,
            background_color=rx.cond(EditorState.activo_dibujo, "#10446c", "#0090ff"),
            width="100%",
            cursor="pointer"
        ),
        
        rx.hstack(
            rx.text("Color", size="2", weight="bold"),
            rx.input(
                type="color",
                on_change=EditorState.cambiar_color_dibujo,
                height="2.5em",
                padding="0",
                cursor="pointer",
                flex="1"
            ),
            width="100%",
            align_items="center",
            spacing="3",
            margin_top="2"
        ),
        
        rx.vstack(
            rx.text("Grosor del pincel", size="2", weight="bold"),
            rx.slider(
                value=EditorState.tamano_pincel,
                on_change=EditorState.cambiar_tamano_pincel,
                on_value_commit=EditorState.cambiar_tamano_pincel,
                width="100%"
            ),
            width="100%",
            align_items="stretch",
            margin_top="2"
        ),
        width="100%",
        align_items="stretch",
        spacing="4"
    )