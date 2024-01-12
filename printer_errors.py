def printer_error(s):
    error_count = sum(1 for char in s if char > 'm')

    return f"{error_count}/{len(s)}"