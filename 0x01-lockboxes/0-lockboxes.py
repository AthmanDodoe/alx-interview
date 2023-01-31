#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    opened_boxes = set()
    opened_boxes.add(0)
    queue = [0]

    while queue:
        box = queue.pop(0)
        keys = boxes[box]
        for key in keys:
            if key not in opened_boxes:
                opened_boxes.add(key)
                queue.append(key)

    if len(opened_boxes) == len(boxes):
        return True
    else:
        return False
