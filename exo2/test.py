# coding: utf-8
"""
This module contains unit tests for the methods in utils file.
"""

from sublist_split import sublist_split
import pytest


def test_sublist_split_error_raised():

    with pytest.raises(ValueError):
        sublist_split([], 14, 12)


# TODO