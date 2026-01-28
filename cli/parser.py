import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        prog="cryptx",
        description="CRYPTX - CTF-focused encoder/decoder tool",
        add_help=True
    )

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("-e", "--encode", action="store_true", help="Encode mode")
    mode.add_argument("-d", "--decode", action="store_true", help="Decode mode")

    parser.add_argument(
        "algorithm",
        nargs="?",
        help="Encoding/decoding algorithm (base64, rot, hex, etc.)"
    )

    parser.add_argument(
        "text",
        nargs="?",
        help="Input text"
    )

    parser.add_argument(
        "-r", "--rot",
        type=int,
        help="ROT shift value (for rot cipher)"
    )

    parser.add_argument(
        "-k", "--key",
        help="Key for XOR encoding/decoding"
    )

    parser.add_argument(
        "--man",
        action="store_true",
        help="Show full manual page"
    )

    return parser
