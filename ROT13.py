def rot13(message):
    deciphered_message = []

    for ch in message:
        if ord(ch) == 32:
            deciphered_message.append(ch)

        elif 97 <= ord(ch) <= 109 or 65 <= ord(ch) <= 77:
            new_ch = chr(ord(ch)+ 13)
            deciphered_message.append(new_ch)

        elif 110 <= ord(ch) <= 122 or 78 <= ord(ch) <= 90:
            new_ch = chr(ord(ch) - 13)
            deciphered_message.append(new_ch)

        else:
            deciphered_message.append(ch)

    return "".join(deciphered_message)


print(rot13("EBG13 rknzcyr."))