import asyncio
import logging
import os

from helpers import configure_logging_from_json
from implementations.fibonacci import (binet_fibonacci,
                                       recursive_fibonacci)

logger = logging.getLogger('worker')


if __name__ == "__main__":
    configure_logging_from_json('configuration/logging.json')
    logger.info("Application is starting")
    tasks = [asyncio.Task(recursive_fibonacci(int(os.getenv("NUMBER", 25)))),
             asyncio.Task(binet_fibonacci(int(os.getenv("NUMBER", 25))))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    logger.info("Application is closing")
