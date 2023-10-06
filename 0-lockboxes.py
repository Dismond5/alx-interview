def canUnlockAll(boxes):

    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for ky in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = ky in boxes[idx] and ky != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
