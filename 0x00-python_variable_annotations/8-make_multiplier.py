#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Return function that multiplies float by multiplier """
    def multiply_by_multiplier(num: float) -> float:
        """ Return product of multiplier and num """
        return num * multiplier
    return multiply_by_multiplier
