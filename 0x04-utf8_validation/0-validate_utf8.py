#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Function that return true if the data is utf-8
    """
    num_bytes_to_check = 0

    for num in data:
        if num >= 128:
            if num_bytes_to_check == 0:
                mask = 1 << 7
                while num & mask:
                    num_bytes_to_check += 1
                    mask >>= 1

                if num_bytes_to_check == 0 or num_bytes_to_check > 4:
                    return False
                num_bytes_to_check -= 1
            else:
                if num >> 6 != 0b10:
                    return False
                num_bytes_to_check -= 1
        elif num_bytes_to_check != 0:
            return False
    return num_bytes_to_check == 0
