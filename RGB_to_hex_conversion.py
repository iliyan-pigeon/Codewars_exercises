def rgb(r, g, b):
    if r > 255:
        r = 255
    elif r < 0:
        r = 0

    if g > 255:
        g = 255
    elif g < 0:
        g = 0

    if b > 255:
        b = 255
    elif b < 0:
        b = 0

    hex_value = hex_value = f"{r:02x}{g:02x}{b:02x}"
    return hex_value.upper()
