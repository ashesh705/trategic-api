""" Run modes for the application"""

from enum import Enum
from functools import cache

from pydantic import BaseSettings, Field


class Mode(Enum):
    """Different possible modes of operation for the application"""

    PRODUCTION = "PRODUCTION"
    DEVELOPMENT = "DEVELOPMENT"
    TESTING = "TESTING"


@cache
def get_mode() -> Mode:
    """Return the current mode of operation"""

    class _M(BaseSettings):
        mode: Mode = Field(default=Mode.PRODUCTION, env="run_mode")

        class Config:
            env_file = ".env"

    return _M().mode
