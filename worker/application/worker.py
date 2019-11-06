import asyncio
import logging
import os

import aioredis

from helpers import configure_logging_from_json
from implementations.fibonacci import (binet_fibonacci,
                                       recursive_fibonacci)

logger = logging.getLogger('worker')


async def main():
    # redis = await aioredis.create_redis_pool('redis://localhost')
    while True:
        logger.info("I am a loop!")
        await asyncio.sleep(1)
    # fibonacci_binet = await binet_fibonacci(number)
    # fibonacci_recursive = await recursive_fibonacci(number)
    # logger.info(f"Binet: {fibonacci_binet}, Recursive: {fibonacci_recursive}")

if __name__ == "__main__":
    configure_logging_from_json('configuration/logging.json')
    logger.info("Application is starting")
    # asyncio.run(main(int(os.getenv("NUMBER", 25))))
    try:
        loop = asyncio.get_event_loop()
        asyncio.ensure_future(main())
        loop.run_forever()
    except Exception:
        logger.exception("Caught an error in the loop.")
    finally:
        logger.info("Application is closing")
        loop.close()
