from pydantic import BaseModel
from typing import Any, List, Optional

class Product(BaseModel):
    id: Optional[str] = ""
    title: str = ""
    slug: str = ""
    description: Optional[str] = ""
    price: float = 0.0
    is_new: bool = False
    is_featured: bool = False
    is_bestseller: bool = False
    card_image_url: str = ""
    gallery_images: List[str] = []
    attributes: dict[str, Any] = {}