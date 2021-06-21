""" Entry point for the API"""

from fastapi import FastAPI
from fastapi.logger import logger

from src.config import get_config

from .routers import routers


def create_api() -> FastAPI:
    api = FastAPI()

    config = get_config()
    logger.info(f"Initialized API in {config.mode.value} mode")

    for router in routers:
        logger.info(f"Mapping route {router.prefix}")
        api.include_router(router.api_router, prefix=router.prefix)

    return api
