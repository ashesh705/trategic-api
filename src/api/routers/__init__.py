""" List of all enabled routers"""

from .api_status import router as api_status
from .router import Router

routers = [Router(prefix="/api-status", api_router=api_status)]
