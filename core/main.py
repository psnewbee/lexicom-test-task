from fastapi import FastAPI
from .api import api
from core.common import settings


app = FastAPI(title=settings.PROJECT_NAME, __version__="0.0.1", docs=settings.DOCS_URL)

app.include_router(router=api.router, prefix=settings.API_PREFIX)
