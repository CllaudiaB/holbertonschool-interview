#!/usr/bin/python3
"""Lockboxes"""


def a(boxes):
    """
    Write a method that determines if all the boxes can be opened
    Return True if all boxes can be opened, else return False
    """

    keys = boxes[0]
    i = 0

    for key in keys:
        for i in range(len(boxes[key])):
            if boxes[key][i] < len(boxes) and boxes[key][i] not in keys:
                keys.append(boxes[key][i])

    return(len(keys) == len(boxes))
