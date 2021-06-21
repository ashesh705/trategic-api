""" Test cases for the dummy background task"""

import pytest

from src.tasks import add


@pytest.mark.asyncio
async def test_add() -> None:
    res = await add({}, 2, 3)
    assert res == 5
