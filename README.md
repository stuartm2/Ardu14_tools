# Tools and other info for my MK14 Emulator

Based on [dadecoza/Ardu14](https://github.com/dadecoza/Ardu14) - currently requires [my fork](https://github.com/stuartm2/Ardu14).

The Gerber board and 3D-printed back cover are available in this repository.

![MK14 Emulator PCB](MK14-OLEDI2C.png)

## BOM

 - 1x I2C 0.91-inch OLED Display, SSD1306, 128x32 (eg: https://www.ebay.co.uk/itm/313604343917)
 - 1x USB to TTL Serial CH340N Module (eg: https://www.ebay.co.uk/itm/405251361500)
 - 1x Atmega328P DIP28
 - 1x IC socket DIP28 (recommended, see 'known issues' below)
 - 1x ceramic resonator, 16MHz, gnd on centre pin
 - 1x 10k resistor
 - 21x tac switches
 - 4x M3x5mm screws (prefer flanged button head)

## Known Issues

 - The USB-C power board doesn't support proper USB-C cables so a conventional Micro-USB accessory cable with a USB-C adaptor is recommended. It might require some experiementation to get the right combination.
 - The board is missing a capacitor so a USB-Serial programmer won't be able to reset the board. It should be possible to manually reset the board at the appropriate time but may be more reliable to remove the Atmega328 and program it off-board.
 - The reset button is the Arduino reset so doesn't perform a soft reset per the original system.

## Support Tools

Requires [PySerial](https://pypi.org/project/pyserial/) and [IntelHex](https://pypi.org/project/intelhex/) Python libraries to be installed.

### convert_to_hex.py

Interactive tool to convert hex-encoded programs to IntelHex format for uploading to the emulator.

Example usage:
```
python3 convert_to_hex.py

Start address (default: 0x0f20)?
Program? ('' exits) 90 00 C4 00 31 C4 0D 35 C4 AA CD 00 90 F4

:0E0F20009000C40031C40D35C4AACD0090F479
:00000001FF
```

The output can be copied and uploaded to the emulator using your preferred serial tool.

### upload.py

Interactive tool to convert hex-encoded programs to IntelHex format and upload directly to the emulator.

Example usage:
```
python3 upload.py /dev/cu.usbserial-1410

Start address (default: 0x0f20)?
Program? ('' exits) 90 00 C4 00 31 C4 0D 35 C4 AA CD 00 90 F4
```

Then run the uploaded program on the emulator in the usual way.
