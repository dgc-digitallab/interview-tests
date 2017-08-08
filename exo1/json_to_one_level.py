# coding: utf-8


def json_to_one_level(obj, parent=None):
    """
    Take a dict and update all the path to be on one level.
    Arguments:
        output (dict): The dict to proceed.
        parent (unicode): The parent key. Used only with recursion.
    Return:
        dict: The updated obj.
    """
