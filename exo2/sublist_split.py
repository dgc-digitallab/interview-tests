# coding: utf-8

import math

def sublist_split(items, parts=None, count_per_sublist=None):
    """
    This method split a list of items in several sub lists to make paralleling process easier.
    /!\ You can't give parts & count_per_sublist at the same time.
    Args:
        items (list): A list of items to split in parts.
        parts (int): Number of part.
        count_per_sublist (int): Number of item per list.

    Returns:
        (list): A list of lists.
    """
    # XOR
    if not ((parts and not count_per_sublist) or (not parts and count_per_sublist)):
        raise ValueError(u"You need to specify parts or count_per_sublist parameters")

    # TODO