# Frontend/state/store_state.py
import reflex as rx
from Backend.api.products import get_products_from_db, obtener_caracteristicas_unicas, obtener_nuevos_destacados, obtener_mas_vendidos
from Backend.schemas.products import Product
from typing import Any

class StoreState(rx.State):
    # Lista que alimentará la UI
    products: list[Product] = []
    productos_nuevos_destacados: list[Product] = []
    productos_mas_vendidos: list[Product] = []
    
    # Lista de caracteristicas disponibles
    prendas_disponibles: list[str] = []
    cortes_disponibles: list[str] = []
    colores_disponibles: list[str] = []
    tallas_disponibles: list[str] = []

    # Valores por defecto de los filtros
    selected_section: str = "todas"
    selected_prenda: str = "todas"
    selected_corte: str = "todas"
    selected_color: str = "todas"
    selected_talla: str = "todas"

    def load_products(self):
        productos_crudos = get_products_from_db(
            section=self.selected_section,
            prenda=self.selected_prenda,
            corte=self.selected_corte,
            color=self.selected_color,
            talla=self.selected_talla
        )
        
        self.products = [Product(**producto) for producto in productos_crudos]
    
    def load_main_products(self):
        datos_crudos_nuevos = obtener_nuevos_destacados()
        datos_crudos_vendidos = obtener_mas_vendidos()
        
        self.productos_nuevos_destacados = [Product(**producto) for producto in datos_crudos_nuevos]
        
        self.productos_mas_vendidos = [Product(**producto) for producto in datos_crudos_vendidos]

    def cargar_filtros(self):
        self.colores_disponibles = obtener_caracteristicas_unicas("color")
        self.prendas_disponibles = obtener_caracteristicas_unicas("prenda")
        self.cortes_disponibles = obtener_caracteristicas_unicas("corte")
        self.tallas_disponibles = obtener_caracteristicas_unicas("talla")

    # Eventos cuando el usuario interactúa en la pantalla
    def set_prenda(self, value: str):
        self.selected_prenda = value  # <--- Recarga automáticamente los productos

    def set_color(self, value: str):
        self.selected_color = value
    
    def set_corte(self, value: str):
        self.selected_corte = value

    def set_talla(self, value: str):
        self.selected_talla = value
        
    def set_section(self, value: str):
        self.selected_section = value