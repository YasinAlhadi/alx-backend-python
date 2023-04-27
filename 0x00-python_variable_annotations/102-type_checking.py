#!/usr/bin/env python3
"""add type annotations to the function"""

from typing import List, Any, TypeVar, Iterable


T = TypeVar('T')


def zoom_array(lst: Iterable[T], factor: Any = 2) -> List[T]:
    """add type annotations to the function"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
