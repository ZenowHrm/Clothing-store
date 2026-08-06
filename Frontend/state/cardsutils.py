import reflex as rx
from Backend.schemas.products import Product
from Backend.api.products import get_product_from_id

class CardState(rx.State):
    cards_in_cart: dict[str, int] = {}
    
    cart_products_details: list[Product] = []
    
    def send_to_cart(self, id):
        product = str(id)
        
        if self.cards_in_cart.get(product, 0) > 0:
            if self.cards_in_cart.get(product, 0) < 99:
                self.cards_in_cart[product] += 1
        else:
            self.cards_in_cart[product] = 1
            
            self.update_cart_detail()
        
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