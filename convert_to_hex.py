import sys

import lib


def main() -> None:
    start_addr = lib.get_start_addr()
    prog = lib.get_prog()
    hex = lib.get_hex(start_addr, prog)
    print(f"\n{hex}")


if __name__ == '__main__':
    main()
