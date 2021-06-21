""" Dummy background task"""

import logging

logger = logging.getLogger(__name__)


async def add(ctx: dict, a: int, b: int) -> int:
    logger.info(f"Passed a={a}, b={b}")
    return a + b
