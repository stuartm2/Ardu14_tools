import sys

from io import StringIO
from intelhex import IntelHex


DEFAULT_START_ADDR = 0x0F20


def get_hex(start_addr: int, prog: list[int]) -> str:
    ih = IntelHex()
    ih.frombytes(prog, offset=start_addr)

    with StringIO() as sio:
        ih.write_hex_file(sio)
        return sio.getvalue()


def get_prog() -> list[int]:
    while True:
        prog = input("Program? ('' exits)")
        if prog == '':
            sys.exit(0)

        binprog = prog.split()
        try:
            binprog = list(map(lambda s: int(s, base=16), binprog))
            if any(map(lambda i: i < 0 or i > 255, binprog)):
                raise ValueError("Not 8-bit")
            return binprog
        except ValueError:
            print("All values must be unsigned 8-bit hex (0xNN or NN)")


def get_start_addr() -> int:
    while True:
        start_addr = input(f"Start address (default: 0x{DEFAULT_START_ADDR:04x})? ")
        if start_addr == '':
            return DEFAULT_START_ADDR
        elif start_addr.isnumeric():
            return int(start_addr)
        else:
            try:
                return int(start_addr, base=16)
            except ValueError:
                print("Must be number or blank")
