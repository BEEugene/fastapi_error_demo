import os
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    # most options here were generated automatically
    APP_VERSION: str = "0.1.0"
    IS_DEBUG:bool = True

    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "8e8adca10afd6aebdf257757a90d1575e17672890162f730f940acaad2e6f061" #secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl
    # BACKEND_CORS_ORIGINS s a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'

    PROJECT_NAME: str = "fastapi_service"
    SENTRY_DSN: Optional[HttpUrl] = None

    EMAILS_ENABLED: bool = False


    FIRST_SUPERUSER: EmailStr = "some@any.com"
    FIRST_SUPERUSER_PASSWORD: str = "any"
    FIRST_SUPERUSER_NAME: str = "some"
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True
    # manual settings
    HOST_CLIENT:str = "http://localhost:3000"

    HOST_CLIENT_https: str = "https://localhost:3000"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [HOST_CLIENT]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

settings = Settings()
