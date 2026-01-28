def encode_binary(text):
    return " ".join(format(ord(c), "08b") for c in text)


def decode_binary(binary_str):
    try:
        chars = binary_str.split()
        return "".join(chr(int(b, 2)) for b in chars)
    except ValueError:
        raise ValueError("Invalid binary input")
