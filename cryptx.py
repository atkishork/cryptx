#!/usr/bin/env python3

import sys

from cli.parser import get_parser
from cli.dispatcher import dispatch
from cli.manpage import show_manpage


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.man:
        show_manpage()
        sys.exit(0)

    if not args.encode and not args.decode:
        parser.error("one of -e (encode) or -d (decode) is required")

    dispatch(args)


if __name__ == "__main__":
    main()
