#!/usr/bin/python3
""" Defines a UTF-8 validator function """


def validUTF8(data):
    """ Determines if a given dataset represents valid UTF-8 encoding

        Args:
            data(list): A list of integers representing the dataset

        Returns:
            True: if the dataset represents a valid UTF-8 encoding
            False: if the dataset doesn't represent a valid UTF-8 encoding
    """
    for i in data:
        if i > 127:
            return False
        else:
            return True
