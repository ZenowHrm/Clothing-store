import reflex as rx

class MenuState(rx.State):
    is_open: bool = False

    def toggle_menu(self):
        self.is_open = not self.is_open