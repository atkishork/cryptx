def encode_decimal(text):
    return " ".join(str(ord(c)) for c in text)


def decode_decimal(text):
    try:
        return "".join(chr(int(n)) for n in text.split())
    except ValueError:
        raise ValueError("Invalid decimal input")


def encode_octal(text):
    return " ".join(format(ord(c), "o") for c in text)


def decode_octal(text):
    try:
        return "".join(chr(int(n, 8)) for n in text.split())
    except ValueError:
        raise ValueError("Invalid octal input")
