""" Configure logging for the application"""

import pathlib
from logging.config import dictConfig

import yaml


def configure_logging() -> None:
    """Configure logging for the application"""

    config_root = pathlib.Path(__file__).parent
    source_root = config_root.parent
    project_root = source_root.parent

    file = project_root / "logging.yaml"
    with file.open() as f:
        config = yaml.safe_load(f)

    dictConfig(config)
