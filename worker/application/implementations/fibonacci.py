import asyncio
import logging
import math

logger = logging.getLogger('implementations')


async def recursive_fibonacci(number: int) -> int:
    """
    Recursive classic calculation

    :param number:
    :return:
    """
    if number <= 1:
        logger.info(f"Recursive result is {number}")
        return number

    return await recursive_fibonacci(number - 1) + \
        await recursive_fibonacci(number - 2)


async def binet_fibonacci(number: int) -> int:
    """
    Binet solution for fibonacci. No recursion

    :param number:
    :return:
    """
    fibonacci = (
            (
                    (1 + math.sqrt(5)) ** number - (1 - math.sqrt(5)) ** number
            )
            /
            ((2 ** number) * math.sqrt(5))
    )
    return int(fibonacci)


def fibonacci_with_generator(number: int):
    """
    Calculate fibonacci using a generator
    :param number: int
    :return: int
    """
    logger.info(f"Fibonacci task starting for: {number}")
    i = 0
    sequence = []
    while i < number:
        i += 1
        if len(sequence) < 2:
            sequence.append(1)
            yield sequence[-1]
            continue

        new_number = sum(sequence)
        sequence.append(new_number)
        sequence.pop(0)
        yield new_number
