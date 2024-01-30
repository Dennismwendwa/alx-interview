#!/usr/bin/python3
"""
This script determines if given data set is valid UTF-8 encoded
Its uses bitwise to check the leading bits which contains data
about the format used.

Note: In UTF-8 characters can be encoded using 1 - 4 bytes.
single-byte character (1 byte)
    - Binary: '0xxxxxxx'
    - Example: '01000001' (represents the ASCII 'A')
Two-byte Character (2 bytes)
    - Binary: '110xxxxx 10xxxxxx'
    - Example: '11000010 10000001' (character outside the ASCII range)
Three-byte character (3 bytes):
    - Binary: '1110xxxx 10xxxxxx 10xxxxxx'
    - Example: '11100010 10000010 10000001' (character outside the ASCII range
Four-byte character (4 bytes)
    - Binary: '11110xxx 10xxxxxx 10xxxxxx 10xxxxxx'
    - Example: '11110000 10000000 10000000 10000000' (character outside the
                                                      ASCII range)

 'x' -> in the binary representation indicates the bits used to
        encode the character's code point
 The leading bits determines the format.
 The trailing bits contain information about the character
"""


def validUTF8(data):
    """This checking if this is valid UTF8 encoded data"""
    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                num_bytes = 1
            elif (num >> 4) == 0b1110:
                num_bytes = 2
            elif (num >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
