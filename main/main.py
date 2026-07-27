import reflex as rx
from fastapi import FastAPI

from Backend.schemas.user import router as user

backend_app = FastAPI()
app = rx.App()

backend_app.include_router(user, tags=["User"])
app._api.mount("/api", backend_app)

def index() -> rx.Component:
    main = rx.el.div(
        rx.el.h1(
            "Hola mundo"
        ),
        style= {
            "background": "#09f"
        }
    )
    
    return main

app.add_page(index, route="/")