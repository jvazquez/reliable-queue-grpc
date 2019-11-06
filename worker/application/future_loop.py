import asyncio
import logging
import os

from helpers import configure_logging_from_json
from implementations.fibonacci import binet_fibonacci

logger = logging.getLogger('worker')


def display_fibonacci_calculation(future):
    logger.info(f"Binet calculation is {future.result()}")


if __name__ == "__main__":
    configure_logging_from_json('configuration/logging.json')
    logger.info("Application is starting")
    loop = asyncio.get_event_loop()
    task = loop.create_task(binet_fibonacci(int(os.getenv("NUMBER", 25))))
    task.add_done_callback(display_fibonacci_calculation)
    loop.run_until_complete(task)
    logger.info("Application is closing")
