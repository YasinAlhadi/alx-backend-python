#!/usr/bin/env python3
""" Module that takes a list input of any type and returns first element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return first element of list or None"""
    if lst:
        return lst[0]
    else:
        return None
