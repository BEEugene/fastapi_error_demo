import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi_service.core.config import settings
from fastapi_service.schemas import schemas
from fastapi_service import crud
from fastapi_service.models.models import Base

SQLALCHEMY_DATABASE_URI = \
    'postgresql://{USER}:{PASS}@{SERVER}:{PORT}/{DB}'.format(
        USER="postgres",
        PASS="pass",
        SERVER="localhost",  # change to prod
        PORT="5432",
        DB="fastapi_error")


engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

sess = SessionLocal()

user = crud.suser.get_by_email(sess, email=settings.FIRST_SUPERUSER)
if not user:
    suuser_in = schemas.SuCreate(
        user_id = uuid.uuid4(),
        email=settings.FIRST_SUPERUSER,
        password=settings.FIRST_SUPERUSER_PASSWORD,
        is_superuser=True,
    )
    user = crud.suser.create(sess, obj_in=suuser_in)  # noqa: F841
