def show_manpage():
    # ANSI colors
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"

    line = "-" * 90

    print(f"""
{CYAN}{line}{RESET}
{BOLD}{MAGENTA}{"CRYPTX".center(90)}{RESET}
{WHITE}{"A powerful encoder / decoder CLI tool for CTFs".center(90)}{RESET}
{CYAN}{line}{RESET}

{BOLD}{WHITE}Author Name:{RESET} {GREEN}Kishor Kumar{RESET}
{BOLD}{WHITE}GitHub     :{RESET} {GREEN}https://github.com/atkishork{RESET}

{CYAN}{line}{RESET}

{BOLD}{YELLOW}NAME{RESET}
    {BOLD}cryptx{RESET} — multi-purpose encoder/decoder for CTFs and cybersecurity tasks

{BOLD}{YELLOW}SYNOPSIS{RESET}
    {GREEN}cryptx -e <algorithm> <text> [options]{RESET}
    {GREEN}cryptx -d <algorithm> <text> [options]{RESET}

{BOLD}{YELLOW}DESCRIPTION{RESET}
    CRYPTX is a Linux command-line utility designed for Capture-The-Flag (CTF)
    challenges, penetration testing, and cryptography practice.

    It provides fast access to commonly used encoders, decoders, classical
    ciphers, numeric conversions, and web-safe transformations.

{BOLD}{YELLOW}SUPPORTED ALGORITHMS{RESET}
    {CYAN}Base Encodings:{RESET}
        base32, base45, base58, base62, base64, base85

    {CYAN}Classical Ciphers:{RESET}
        rot        (requires -r value)

    {CYAN}Numeric & Binary:{RESET}
        hex, binary, decimal, octal

    {CYAN}Other:{RESET}
        xor        (requires -k key)
        url

{BOLD}{YELLOW}OPTIONS{RESET}
    {GREEN}-e{RESET}              Encode mode
    {GREEN}-d{RESET}              Decode mode
    {GREEN}-r <n>{RESET}          ROT / Caesar shift value (1–25)
    {GREEN}-k <key>{RESET}        XOR key
    {GREEN}-h{RESET}              Show help
    {GREEN}--man{RESET}           Show this manual page

{BOLD}{YELLOW}EXAMPLES{RESET}
    {GREEN}cryptx -e base64 "hello"{RESET}
    {GREEN}cryptx -d hex 68656c6c6f{RESET}
    {GREEN}cryptx -e rot -r 13 "hello"{RESET}
    {GREEN}cryptx -e xor "secret" -k key{RESET}

{BOLD}{YELLOW}NOTES{RESET}
    • Designed for fast use during CTFs
    • Offline-friendly (no internet required)
    • Easy to extend with new encoders
    • Clean, scriptable CLI output

{BOLD}{YELLOW}AUTHOR{RESET}
    Kishor Kumar
    https://github.com/atkishork

{BOLD}{YELLOW}LICENSE{RESET}
    MIT License

{CYAN}{line}{RESET}
""")
