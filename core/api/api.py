from fastapi import APIRouter
from .endpoints import (
    healthcheck_router,
    notebook_router,
)

router: APIRouter = APIRouter()

router.include_router(healthcheck_router, prefix='/healthcheck', tags=['healthcheck'])
router.include_router(notebook_router, prefix='/notebook', tags=['notebook'])
