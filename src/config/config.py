""" Mode-specific configuration for the application"""

from functools import cache

from pydantic import BaseSettings

from .logging import configure_logging
from .mode import Mode, get_mode

# Configure logging globally
configure_logging()


class Config(BaseSettings):
    title = "Trategic"
    description = "API for the Trategic project"

    mode: Mode


class _ProdConfig(Config):
    mode: Mode = Mode.PRODUCTION


class _DevConfig(Config):
    mode: Mode = Mode.DEVELOPMENT


class _TestConfig(Config):
    mode: Mode = Mode.TESTING


@cache
def get_config() -> Config:
    """Return the configuration for the application"""

    mode = get_mode()
    if mode == Mode.PRODUCTION:  # pragma: no cover
        return _ProdConfig()
    elif mode == Mode.DEVELOPMENT:  # pragma: no cover
        return _DevConfig()
    elif mode == Mode.TESTING:
        return _TestConfig()
    else:
        raise NotImplementedError
