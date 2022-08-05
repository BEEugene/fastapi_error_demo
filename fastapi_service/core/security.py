from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

from fastapi_service.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)




def generate_private_key():

    KEY_SIZE = 2048
    PUBLIC_EXP = 65537
    private_key = rsa.generate_private_key(
        public_exponent=PUBLIC_EXP,
        key_size=KEY_SIZE,
        backend=default_backend()
    )
    private_key_enc_str = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b'DPDCsecretAPPpass') #.NoEncryption()
    ).decode()
    return private_key, private_key_enc_str

def load_enc_private(string_key, password):
    return serialization.load_pem_private_key(
        bytes(string_key,"UTF-8"), bytes(password,"UTF-8"))

def get_public_key(private_key):
    public_key = private_key.public_key()
    return public_key
