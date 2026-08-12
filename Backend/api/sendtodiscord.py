import os
import requests
from dotenv import load_dotenv
import datetime

fecha = datetime.datetime.now()

def EnviarDiscord(usuario, correo, mensaje):
    load_dotenv()
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("Error: No se encontró la URL del Webhook de Discord.")
        return False

    data = {
        "username": "TeeVibes | Notificaciones", 
        "avatar_url": "https://i.postimg.cc/GhbhFbJP/image.png", 
        
        "embeds": [
            {
                "title": "💡 ¡Nueva Propuesta Recibida!",
                "color": 3447003, 
                "fields": [
                    {
                        "name": "👤 Usuario",
                        "value": usuario,
                        "inline": True
                    },
                    {
                        "name": "📧 Correo",
                        "value": correo,
                        "inline": True
                    },
                    {
                        "name": "📝 Mensaje",
                        "value": mensaje,
                        "inline": False
                    }
                ],
                "footer": {
                    "text": f"Fecha de envio: {fecha}",
                    "icon_url": "https://i.imgur.com/AfFp7pu.png"
                }
            }
        ]
    }

    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            return True
        else:
            print(f"Error al enviar a Discord: {response.status_code}")
            return False
    except Exception as e:
        print(f"Excepción al conectar con Discord: {e}")
        return False