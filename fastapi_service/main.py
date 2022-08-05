import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from fastapi_service.api.api_v1.api import api_router
from fastapi_service.core.config import settings
from fastapi_service.core.event_handlers import (start_app_handler,
                                                 stop_app_handler)

log = logging.getLogger(__name__)

def get_app(mode="prod") -> FastAPI:

    fast_app = FastAPI(title=settings.PROJECT_NAME,
                       version=settings.APP_VERSION,
                       debug=settings.IS_DEBUG)
                       # openapi_url=f"{settings.API_V1_STR}/openapi.json")

    fast_app.include_router(api_router, prefix=f"{settings.API_V1_STR}")
    fast_app.mode = mode
    logger = log.getChild("get_app")
    logger.info("adding startup")
    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    logger.info("adding shutdown")
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))

    return fast_app


app = get_app()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
