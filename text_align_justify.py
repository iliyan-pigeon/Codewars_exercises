def text_justify(text, width):
    words = text.split()
    lines, line, line_length = [], [], 0

    for word in words:
        if line_length + len(line) + len(word) <= width:
            line.append(word)
            line_length += len(word)
        else:
            lines.append(line)
            line, line_length = [word], len(word)

    if line:
        lines.append(line)

    justified_lines = []
    for i, line in enumerate(lines):
        line_length = sum(len(word) for word in line)
        spaces_to_insert = width - line_length
        if len(line) == 1 or i == len(lines) - 1:
            justified_line = ' '.join(line)
            justified_lines.append(justified_line)
        else:
            spaces, extra_spaces = divmod(spaces_to_insert, len(line) - 1)
            justified_line = line[0]
            for j in range(1, len(line)):
                spaces_to_add = spaces + (1 if j <= extra_spaces else 0)
                justified_line += ' ' * spaces_to_add + line[j]
            justified_lines.append(justified_line)

    return '\n'.join(justified_lines)

# Example usage
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor."
width = 30
justified_text = text_justify(text, width)
print(justified_text)