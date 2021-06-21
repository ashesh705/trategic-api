""" Entry point for the background task processor"""

from .dummy import add


class WorkerSettings:
    functions: list = [add]
