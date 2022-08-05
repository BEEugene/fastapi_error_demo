from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fastapi_service.core.security import generate_private_key, get_public_key
from fastapi_service.schemas import schemas
from fastapi_service.models import models
from fastapi_service import crud
from fastapi_service.api import deps
# from fastapi_service.core.config import settings
# from fastapi_service.core.utils import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[schemas.License])
def issue_license(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    user = crud.user.get_by_email(db, email=current_user.email)
    prk = generate_private_key()
    pbk = get_public_key(prk)


    # users = crud.user.get_multi(db, skip=skip, limit=limit)
    # return users