#!/usr/bin/python3
""" This defines a function canUnlockAll that solves the lockbox problem """


def canUnlockAll(boxes):
    """ Determines if all the boxes in the list of lists can be opened.

    Args:
        boxes (list of lists): A list containing a list of n number of boxes
                               with keys inside

    Returns: True if all the boxes can be opened, false otherwise.
    """
    num_boxes = len(boxes)
    box_array = []
    key_array = []
    box = 0
    i = 0
    for box_num in range(0, num_boxes):
        box_array.append(box_num)
    #print("box array = {}".format(box_array))
    while i < num_boxes:
        box += 1
        for key_num in boxes[i]:
            if key_num not in key_array:
                key_array.append(key_num)
            if key_num in box_array:
                for k in boxes[key_num]:
                    if k not in key_array:
                        key_array.append(k)
        #print("Key_array in iteration {}: {}".format(i, key_array))
        for key in key_array:
            if key == box:
                if box in box_array:
                    box_array.remove(box)
                    #print("Box removed is: {}".format(box))
                    break
                #else:
                    #print("Box {} not in box_array and not removed".format(box))
        #print("box_array after iteration {}: {}".format(i, box_array))
        i += 1
        if len(box_array) == 1:
            return True

    return False
