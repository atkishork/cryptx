from urllib.parse import quote, unquote


def encode_url(text):
    return quote(text)


def decode_url(text):
    return unquote(text)
