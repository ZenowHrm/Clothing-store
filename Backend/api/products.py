from Backend.database import supabase

def get_product_from_id(id):
    query = supabase.table("products").select("*")
    query = query.eq("id", id)
    response = query.execute()
    return response.data[0] if response.data else {}

def get_products_from_db(
    section: str = "todas",
    prenda: str = "todas",
    corte: str = "todas",
    color: str = "todas",
    talla: str = "todas"
    ):
    query = supabase.table("products").select("*")

    # 1. Filtro de sección (Marketing)
    if section and section != "todas":
        if section == "nuevo":
            query = query.eq("is_new", True)
        elif section == "destacado":
            query = query.eq("is_featured", True)
        elif section == "mas_vendido":
            query = query.eq("is_bestseller", True)

    # 2. Filtros dinámicos en el JSONB "attributes"
    json_filters = {}
    if prenda and prenda != "todas": json_filters["prenda"] = prenda
    if corte and corte != "todas": json_filters["corte"] = corte
    if color and color != "todas": json_filters["color"] = color
    if talla and talla != "todas": json_filters["talla"] = talla

    # Si hay al menos un filtro activo, aplicamos el .contains
    if json_filters:
        query = query.contains("attributes", json_filters)

    response = query.execute()
    return response.data

def obtener_caracteristicas_unicas(caracteristica) -> list[str]:
    # 1. Consultamos únicamente la columna JSON 'attributes' de la tabla
    res = supabase.table("products").select("attributes").execute()
    
    # 2. Extraemos el valor de la clave (ej. 'color') de cada registro
    valores_unicos = set()
    for item in res.data:
        atributos = item.get("attributes")
        # Validamos que 'attributes' sea un diccionario y que exista la clave
        if isinstance(atributos, dict) and atributos.get(caracteristica):
            valores_unicos.add(str(atributos[caracteristica]))
            
    # 3. Retornamos la lista ordenada alfabéticamente
    return sorted(list(valores_unicos))

def obtener_nuevos_destacados(limite: int = 8):
    query = (
        supabase.table("products")
        .select("*")
        .or_("is_featured.eq.true,is_new.eq.true")
        .order("created_at", desc=True)
        .limit(limite)
    )
    
    res = query.execute()
    return res.data or []

def obtener_mas_vendidos(limite: int = 8):
    query = (
        supabase.table("products")
        .select("*")
        .eq("is_bestseller", True)       
        .order("created_at", desc=True)
        .limit(limite)
    )
    
    res = query.execute()
    return res.data or []