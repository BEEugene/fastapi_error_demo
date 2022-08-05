from typing import Any

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey, TIMESTAMP, VARCHAR


# how the PG tables looks like
@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Superuser(Base):
    user_id = Column(UUID(as_uuid=True), unique=True, primary_key=True)
    email = Column(VARCHAR(length=100))
    is_superuser = Column(Boolean(), default=False)
    hashed_password = Column(String, nullable=False)


class App(Base):
    app_id = Column(UUID(as_uuid=True), unique=True, primary_key=True)
    app_ver = Column(String)
    app_name = Column(VARCHAR(length=100), unique=True)
    app_exec_line = Column(String)

class User(Base):
    user_id = Column(UUID(as_uuid=True), unique=True, primary_key=True)
    email = Column(VARCHAR(length=100))
    personal_private_key = Column(String, nullable=True)

class License(Base):
    subscription_id = Column(UUID(as_uuid=True), unique=True, primary_key=True)

    user_id = Column(UUID(as_uuid=True), ForeignKey(User.user_id))
    start_date = Column(TIMESTAMP)
    end_date = Column(TIMESTAMP)
    license_private_key = Column(String, nullable=True)

    last_use = Column(TIMESTAMP)
    access_counter = Column(Integer)

    app_name = Column(String, ForeignKey(App.app_name))
    app_ver = Column(String)

