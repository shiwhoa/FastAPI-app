from jose import JWTError, jwt
from datetime import datetime, timedelta
from FastAPI_app import pydantic_FE_req_res_payload, sql_alchemy_postgres_connect
from . import pydantic_FE_req_res_payload
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import local_env_var

from FastAPI_app.utils import verify


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY=local_env_var.secret_key
ALGORITHM=local_env_var.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=local_env_var.access_token_expiry

def create_access_token(data:dict):
    to_encode= data.copy() # copying payload
    expire= datetime.utcnow()+ timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES) # time before expiry
    to_encode.update({"exp": expire}) # attach expire to copied data dict

    encoded_jwt= jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM) # encode data

    return encoded_jwt

def verify_access_token(token:str, credentials_exception):\

    try:
        payld = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        sql_alchemy_user_id:str = payld.get("sql_alchemy_user_id")
        if sql_alchemy_user_id is None:
            raise credentials_exception
        token_data = pydantic_FE_req_res_payload.FE_Req_Token_data(FE_request_id= sql_alchemy_user_id)
    except JWTError:
        raise credentials_exception

    return token_data

def get_current_user(token:str = Depends(oauth2_scheme), db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate", headers = {"WWW-Authenticate": "Bearer"})

    # db.query()

    return verify_access_token(token, credentials_exception)