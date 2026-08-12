import reflex as rx
from Backend.schemas.products import Product
from Backend.api.products import get_product_from_id

class CardState(rx.State):
    cards_in_cart: dict[str, int] = {}
    
    cart_products_details: list[Product] = []
    
    total: float = 0
    
    show_modal: bool = False
    
    def send_to_cart(self, id):
        product = str(id)
        
        if self.cards_in_cart.get(product, 0) > 0:
            if self.cards_in_cart.get(product, 0) < 99:
                self.cards_in_cart[product] += 1
        else:
            self.cards_in_cart[product] = 1
            
            self.update_cart_detail()
        
        self.set_total()
        
    def update_cart_detail(self):
        lista_detail: list[Product] = []
        for prod_id in self.cards_in_cart.keys():
            producto = get_product_from_id(prod_id)
            lista_detail.append(producto)
            
        self.cart_products_details = [Product(**item) for item in lista_detail]

    def remove_to_cart(self, id):
        product = str(id)
        
        if self.cards_in_cart.get(product, 0) > 1:
            self.cards_in_cart[product] -= 1
        elif self.cards_in_cart.get(product, 101) <= 1:
            self.cards_in_cart.pop(product)
            
            self.update_cart_detail()
        
        self.set_total()
    
    def set_total(self):
        valor: float = 0
        
        for i in self.cart_products_details:
            valor += (i.price * self.cards_in_cart[str(i.id)])
        
        self.total = round(valor, 2)
        
    def abrir_modal(self):
        self.show_modal = True
    def cerrar_modal(self):
        self.show_modal = False
    def cambiar_estado_modal(self, valor: bool):
        self.show_modal = valor