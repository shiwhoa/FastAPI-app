from os import access
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from sqlalchemy.orm import Session

from .. import sql_alchemy_tables # to access model.py attribures/functions; syntax: models.sql_alchemy_declarative_base
from .. import pydantic_FE_req_res_payload

### from -> import : declares the variable name to be used already
# from . import database
# engine = database.engine
# get_db = database.get_db
from .. import sql_alchemy_postgres_connect
from .. import psycopg2_postgres_connect
from .. import utils
from .. import oauth2


router = APIRouter(tags=['Authentication'])# for swagger ui

@router.post('/login')
def login(FE_req_user_login_payload:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):
    sql_alchemy_table = db.query(sql_alchemy_tables.SQL_Alchemy_Postgres_User_Table)
    sql_alchemy_query_1 = sql_alchemy_table.filter(sql_alchemy_tables.SQL_Alchemy_Postgres_User_Table.sql_alchemy_user_email == FE_req_user_login_payload.FE_request_user_login_username)
    sql_alchemy_query_2 = sql_alchemy_query_1.first()
    if not sql_alchemy_query_2:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"invalid Credentials")

    utils.verify(FE_req_user_login_payload.FE_request_user_login_password, sql_alchemy_query_1.sql_alchemy_user_password)

    if not utils.verify(FE_req_user_login_payload.FE_request_user_login_password, sql_alchemy_query_1.sql_alchemy_user_password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"invalid credentials")

    access_token= oauth2.create_access_token(data= {"sql_alchemy_user_id": sql_alchemy_query_2.sql_alchemy_user_id})

    return {"sql_alchemy_access_token": access_token, "sql_alchemy_token_type": "bearer"}