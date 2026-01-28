def encode_hex(text):
    return text.encode().hex()


def decode_hex(text):
    try:
        return bytes.fromhex(text).decode(errors="ignore")
    except ValueError:
        raise ValueError("Invalid hex input")
