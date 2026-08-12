import reflex as rx
from Backend.api.sendtodiscord import EnviarDiscord

class ContactValues(rx.State):
    name: str = ""
    email: str = ""
    message: str = ""

    def update_name(self, value: str):
        self.name = value

    def update_email(self, value: str):
        self.email = value

    def update_message(self, value: str):
        self.message = value
    
    def send_webhook(self):
        EnviarDiscord(self.name, self.email, self.message)
        self.name = ""
        self.email = ""
        self.message = ""
        