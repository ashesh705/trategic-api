""" Test endpoints for API status"""

import pytest
from fastapi import status
from fastapi.logger import logger
from httpx import AsyncClient

from src.api.routers.api_status import APIStatus


@pytest.mark.asyncio
async def test_api_status(client: AsyncClient) -> None:
    response = await client.get("/api-status")

    data = response.json()
    logger.debug(data)

    assert response.status_code == status.HTTP_200_OK
    assert data == APIStatus()
