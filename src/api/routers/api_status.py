""" Endpoints for API status"""

from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class APIStatus(BaseModel):
    status: Literal["OK"] = "OK"


@router.get("/", response_model=APIStatus)
async def get_api_status() -> APIStatus:
    return APIStatus()
