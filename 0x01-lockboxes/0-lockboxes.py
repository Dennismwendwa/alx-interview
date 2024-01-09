#!/usr/bin/python3
"""This method uses stack to keep track of open boxes"""


def canUnlockAll(boxes):
    """This method checks if all boxes can be opened"""
    box_status = [False] * len(boxes)
    box_status[0] = True

    stack = [0]

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and not box_status[key]:
                box_status[key] = True
                stack.append(key)

    return all(box_status)
