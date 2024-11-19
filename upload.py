import serial
import sys

import lib


def main(port: str) -> None:
    with serial.Serial(port, 9600) as s:
        while True:
            start_addr = lib.get_start_addr()
            prog = lib.get_prog()
            hex = lib.get_hex(start_addr, prog)
            s.write(hex.encode())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 upload.py [port]")
        sys.exit(1)
    main(*sys.argv[1:])
