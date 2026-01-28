def rot_transform(text, shift):
    result = []

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result.append(
                chr((ord(char) - base + shift) % 26 + base)
            )
        else:
            result.append(char)

    return "".join(result)


def encode_rot(text, shift):
    return rot_transform(text, shift)


def decode_rot(text, shift):
    return rot_transform(text, -shift)
