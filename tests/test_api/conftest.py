""" Fixtures for testing the API"""

from collections.abc import AsyncGenerator

import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from src.api import create_api


@pytest.fixture(scope="session")
async def api() -> AsyncGenerator[FastAPI, None]:
    yield create_api()


@pytest.fixture(scope="session")
async def client(api: FastAPI) -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=api, base_url="http://test") as client:
        yield client
