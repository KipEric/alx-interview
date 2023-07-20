#!/usr/bin/python3
"""
script that check for key to unlock a box
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    """
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    return len(keys) == len(boxes)
