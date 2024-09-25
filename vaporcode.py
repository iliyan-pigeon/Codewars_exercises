def vaporcode(s):
    vaporwave = ""

    for ch in s:
        if ch != " ":
            vaporwave += f"{ch.upper()}  "

    return vaporwave[:-2]
