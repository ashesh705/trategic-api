""" Dummy test cases to check repo setup"""

import pytest

from src.dummy import dummy


@pytest.mark.asyncio
async def test_dummy() -> None:
    res = await dummy()
    assert res is True
