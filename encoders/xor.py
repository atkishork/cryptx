def xor_transform(text, key):
    result = []
    key_bytes = key.encode()
    key_len = len(key_bytes)

    for i, c in enumerate(text.encode()):
        result.append(c ^ key_bytes[i % key_len])

    return bytes(result)


def encode_xor(text, key):
    return xor_transform(text, key).hex()


def decode_xor(text, key):
    try:
        data = bytes.fromhex(text)
        key_bytes = key.encode()
        key_len = len(key_bytes)
        return bytes(
            b ^ key_bytes[i % key_len] for i, b in enumerate(data)
        ).decode(errors="ignore")
    except ValueError:
        raise ValueError("Invalid XOR input")
