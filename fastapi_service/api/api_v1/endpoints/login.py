from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from fastapi_service.schemas import schemas
from fastapi_service import crud
from fastapi_service.api import deps
from fastapi_service.core import security
from fastapi_service.core.config import settings


router = APIRouter()


@router.post("/login/access-token", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    OAuth2 compatible app_ver login, get an access app_ver for future requests
    """
    print("form_data", form_data)
    suser = crud.suser.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not suser:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.suser.is_active(suser):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            suser.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }



