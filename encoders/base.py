import base64
import base58
import base45
import base62


def encode_base(algo, text):
    data = text.encode()

    if algo == "base64":
        return base64.b64encode(data).decode()

    elif algo == "base32":
        return base64.b32encode(data).decode()

    elif algo == "base85":
        return base64.b85encode(data).decode()

    elif algo == "base58":
        return base58.b58encode(data).decode()

    elif algo == "base62":
        return base62.encodebytes(data)

    elif algo == "base45":
        return base45.b45encode(data).decode()

    elif algo == "base92":
        raise ValueError("Base92 decoding supported only (encode later)")

    else:
        raise ValueError("Unsupported base encoder")


def decode_base(algo, text):
    data = text.encode()

    if algo == "base64":
        return base64.b64decode(data).decode(errors="ignore")

    elif algo == "base32":
        return base64.b32decode(data).decode(errors="ignore")

    elif algo == "base85":
        return base64.b85decode(data).decode(errors="ignore")

    elif algo == "base58":
        return base58.b58decode(data).decode(errors="ignore")

    elif algo == "base62":
        return base62.decodebytes(text).decode(errors="ignore")

    elif algo == "base45":
        return base45.b45decode(data).decode(errors="ignore")

    elif algo == "base92":
        raise ValueError("Base92 decoding supported only (encode later)")

    else:
        raise ValueError("Unsupported base decoder")
