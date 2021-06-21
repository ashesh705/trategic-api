""" Custom router to use"""

from fastapi import APIRouter
from pydantic import BaseModel, validator


class Router(BaseModel):
    prefix: str
    api_router: APIRouter

    @validator("prefix")
    def is_valid_prefix(cls, v: str) -> str:
        if not v.startswith("/"):  # pragma: no cover
            raise ValueError(f"Invalid prefix {v}, must start with /")

        return v

    class Config:
        arbitrary_types_allowed = True
