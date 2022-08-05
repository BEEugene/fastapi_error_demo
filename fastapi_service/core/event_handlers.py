import logging
from typing import Callable
from fastapi import FastAPI

log = logging.getLogger(__name__)


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        log.info("Running app start handler.")
        pass

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        log.info("Running app shutdown handler.")
        pass

    return shutdown
