from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
from settings import Settings

settings = Settings()
auth_scheme = HTTPBearer()

match settings.auth_scheme:
    case "bearer":
        auth_scheme = HTTPBearer()
    case "Oauth2":
        auth_scheme = OAuth2PasswordBearer()

def authenticate(token: Annotated[HTTPAuthorizationCredentials, Depends(auth_scheme)]):
    if token.credentials != settings.token:
        raise HTTPException(status_code=401, detail="Invalid Token")
