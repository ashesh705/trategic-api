""" Global fixtures for the project"""

import asyncio
from asyncio import AbstractEventLoop
from collections.abc import Generator

import pytest
from pytest import MonkeyPatch

from src.config import Mode


@pytest.fixture(scope="session")
def monkeypatch() -> Generator[MonkeyPatch, None, None]:
    patch = MonkeyPatch()
    yield patch

    patch.undo()


@pytest.fixture(scope="session", autouse=True)
def set_mode(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("RUN_MODE", Mode.TESTING.value)


@pytest.fixture(scope="session")
def event_loop() -> Generator[AbstractEventLoop, None, None]:
    loop = asyncio.get_event_loop()
    yield loop

    loop.close()
