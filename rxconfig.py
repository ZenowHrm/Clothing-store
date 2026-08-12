import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin

config = rx.Config(
    app_name="main",
    api_url="https://clothing-store-y9pr.onrender.com",
    show_badge=False,
    disable_plugins=[SitemapPlugin],
    plugins=[
        rx.plugins.RadixThemesPlugin()
    ]
)