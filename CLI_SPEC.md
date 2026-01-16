CRYPTX CLI SPEC

Modes:
- Encode: -e
- Decode: -d

Syntax:
cryptx -e <algorithm> <text> [options]
cryptx -d <algorithm> <text> [options]

Algorithms:
base32 base45 base58 base62 base64 base85 base92
rot (requires -r)
hex
binary
octal
decimal
xor (requires -k)
url

Global Flags:
-h / --help
--man

Rules:
- Exactly one of -e or -d must be used
- rot requires -r
- xor requires -k
- Clear error messages
