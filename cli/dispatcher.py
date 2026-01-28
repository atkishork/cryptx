import sys

from cli.manpage import show_manpage

from encoders.base import encode_base, decode_base
from encoders.hex import encode_hex, decode_hex
from encoders.rot import encode_rot, decode_rot
from encoders.binary import encode_binary, decode_binary
from encoders.numeric import (
    encode_decimal, decode_decimal,
    encode_octal, decode_octal
)
from encoders.xor import encode_xor, decode_xor
from encoders.url import encode_url, decode_url


def dispatch(args):
    """
    Core dispatcher for CRYPTX
    Routes algorithm + mode to correct encoder/decoder
    """

    # Safety: allow --man here as well (in case entry missed it)
    if hasattr(args, "man") and args.man:
        show_manpage()
        sys.exit(0)

    algorithm = args.algorithm
    text = args.text

    if not algorithm or not text:
        print("❌ Algorithm and input text are required")
        sys.exit(1)

    try:
        # ---------- BASE ENCODINGS ----------
        if algorithm.startswith("base"):
            result = (
                encode_base(algorithm, text)
                if args.encode
                else decode_base(algorithm, text)
            )

        # ---------- HEX ----------
        elif algorithm == "hex":
            result = encode_hex(text) if args.encode else decode_hex(text)

        # ---------- ROT / CAESAR ----------
        elif algorithm == "rot":
            if args.rot is None:
                raise ValueError("ROT requires -r <value>")
            result = (
                encode_rot(text, args.rot)
                if args.encode
                else decode_rot(text, args.rot)
            )

        # ---------- BINARY ----------
        elif algorithm == "binary":
            result = encode_binary(text) if args.encode else decode_binary(text)

        # ---------- DECIMAL ----------
        elif algorithm == "decimal":
            result = encode_decimal(text) if args.encode else decode_decimal(text)

        # ---------- OCTAL ----------
        elif algorithm == "octal":
            result = encode_octal(text) if args.encode else decode_octal(text)

        # ---------- XOR ----------
        elif algorithm == "xor":
            if args.key is None:
                raise ValueError("XOR requires -k <key>")
            result = (
                encode_xor(text, args.key)
                if args.encode
                else decode_xor(text, args.key)
            )

        # ---------- URL ----------
        elif algorithm == "url":
            result = encode_url(text) if args.encode else decode_url(text)

        # ---------- UNKNOWN ----------
        else:
            raise ValueError(f"Algorithm '{algorithm}' not implemented")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

    # ---------- OUTPUT ----------
    print("\n" + "=" * 45)
    print("        CRYPTX - Encoder / Decoder")
    print("=" * 45)
    print(f"Algorithm : {algorithm}")
    print(f"Mode      : {'ENCODE' if args.encode else 'DECODE'}")
    print(f"Input     : {text}")
    print("-" * 45)
    print(f"Output    : {result}")
    print("=" * 45)
