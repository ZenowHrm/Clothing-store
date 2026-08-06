COLORS = {
    "black": "#101010",
    "white": "#FBFBFB",
    "purple": "#5F3B8F"
}

def hex_to_rgba(hex_color, alpha):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return f"rgba({r}, {g}, {b}, {alpha})"