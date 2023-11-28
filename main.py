from fastapi import FastAPI
from config import settings
from core.application import factory
from api.api_routes import api_router

app: FastAPI = factory.create(
    title=settings.app.TITLE,
    rest_routers=(api_router, ),
    startup_tasks=[],
    shutdown_tasks=[],
)
