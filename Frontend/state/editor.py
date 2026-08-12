import reflex as rx

class EditorState(rx.State):
    
    seccion_editor = ""
    
    #---text
    textovalues = {
        "fuente": 'Arial',
        "color": '#000000',
        "tamano": 32
    }
    FuentesDisponibles = [
        'Arial', 'Courier New', 'Georgia', 'Times New Roman', 
        'Verdana', 'Impact', 'Comic Sans MS', 'Trebuchet MS'
    ]
    
    #---shape
    FigurasDisponibles = [
        'rectangulo', 'circulo', 'triangulo', 'linea'
    ]
    color_figura = "#6f3ce7"
    figura_seleccionada = "circulo"
    hueco = "false"
    
    #---draw
    activo_dibujo = False
    tamano_pincel = [1]
    
    def cerrar_dibujo(self):
        if self.activo_dibujo:
                self.activo_dibujo = False
                return rx.call_script("window.toggleModoDibujo()")
    
    def add_text(self):
        if self.seccion_editor == "texto":
            self.seccion_editor = ""
        else:
            self.seccion_editor = "texto"
        
        return self.cerrar_dibujo()

    def add_archivo_img(self):
        if self.seccion_editor == "imagen":
            self.seccion_editor = ""
        else:
            self.seccion_editor = "imagen"
        
        return self.cerrar_dibujo()
    
    def add_figura(self):
        if self.seccion_editor == "figura":
            self.seccion_editor = ""
        else:
            self.seccion_editor = "figura"
        
        return self.cerrar_dibujo()
    
    def modo_dibujo(self):
        if self.seccion_editor == "dibujo":
            self.seccion_editor = ""
        else:
            self.seccion_editor = "dibujo"
    
    def cerrar_editor(self):
        self.tamano_pincel = [1]
        self.seccion_editor = ""
        
        if self.activo_dibujo:
            self.activo_dibujo = False
    
    #------Seccion de Texto------#
    def agregar_texto(self):
        return rx.call_script(f"window.agregarTexto('Doble clic para editar', {self.textovalues})")
    
    def cambiar_fuente(self, fuente: str):
        fuente_nueva = fuente
        return rx.call_script(f"window.cambiarFuenteTexto('{fuente_nueva}')")
    
    def cambiar_color(self, color: str):
        color_nuevo = color
        return rx.call_script(f"window.cambiarColorSeleccionado('{color_nuevo}')")
    
    #------Seccion de Imagenes------#
    def agregar_imagen(self):
        return rx.call_script("window.agregarImagenDesdeArchivo(document.getElementById('input-imagen-editor').files[0])")
    
    #------Seccion de formas------#
    def set_figura_value(self, value):
        self.figura_seleccionada = value
    def set_color_value(self, value):
        self.color_figura = value
    def set_hueco_value(self, value):
        valor = value
        if valor:
            self.hueco = "true"
        else:
            self.hueco = "false"

    def agregar_figura(self):
        return rx.call_script(f"window.agregarFigura('{self.figura_seleccionada}', '{self.color_figura}', {self.hueco})")
    
    #------Seccion de dibujo------#
    def iniciar_dibujo(self):
        if not self.activo_dibujo:
            self.activo_dibujo = True
        else:
            self.activo_dibujo = False

        return rx.call_script("window.toggleModoDibujo()")
    
    def cambiar_color_dibujo(self, color: str):
        color_nuevo = color
        return rx.call_script(f"window.cambiarColorPincel('{color_nuevo}')")
    
    def cambiar_tamano_pincel(self, tamano: list[float]):
        self.tamano_pincel = tamano
        return rx.call_script(f"window.cambiarTamanoPincel({self.tamano_pincel[0]})")