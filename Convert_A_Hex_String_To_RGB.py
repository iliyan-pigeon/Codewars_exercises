def hex_string_to_rgb(hex_string):
    # Remove '#' if present
    hex_color = hex_string.lstrip('#')

    # Convert hex to RGB
    rgb = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    return {'r': r, 'g': g, 'b': b}


# Example usage
hex_color_code = "#1a2b3c"
rgb_values = hex_string_to_rgb(hex_color_code)
print(f"Hex: {hex_color_code} -> RGB: {rgb_values}")