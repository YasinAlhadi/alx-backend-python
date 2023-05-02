#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import random
from time import perf_counter
from typing import Generator, List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    start = perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = perf_counter()
    return end - start
