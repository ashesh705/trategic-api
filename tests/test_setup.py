""" Tests to check that the test environment has been loaded correctly"""

from src.config import Mode, get_mode


def test_mode() -> None:
    assert get_mode() == Mode.TESTING
