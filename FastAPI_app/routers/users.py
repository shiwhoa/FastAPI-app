from sys import prefix
from .. import sql_alchemy_postgres_connect
from .. import psycopg2_postgres_connect
from .. import utils
from typing import List

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from sqlalchemy.orm import Session
from .. import sql_alchemy_tables # to access model.py attribures/functions; syntax: models.sql_alchemy_declarative_base
from .. import pydantic_FE_req_res_payload



router = APIRouter(
    prefix="/users",
    tags=['Users'] # for sagger ui compartmentalizing
)




@router.post("/", status_code=status.HTTP_201_CREATED, response_model=pydantic_FE_req_res_payload.FE_Res_Create_User_Payload)
def create_user(FE_req_user_payload:pydantic_FE_req_res_payload.FE_Req_Create_User_Payload,db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):
    
    hashed_pydantic_user_password = utils.hash(FE_req_user_payload.FE_resquest_user_password)
    FE_req_user_payload.FE_resquest_user_password = hashed_pydantic_user_password

    new_sql_alchemy_user = sql_alchemy_tables.SQL_Alchemy_Postgres_User_Table(sql_alchemy_user_email = FE_req_user_payload.FE_request_user_email, sql_alchemy_user_password = FE_req_user_payload.FE_resquest_user_password)
    db.add(new_sql_alchemy_user) # not posting a dictionary, but a sql_alchemy_post post
    db.commit()
    db.refresh(new_sql_alchemy_user)

    # print(**new_post.dict()) # keys become keyword argument
    # new_sql_alchemy_post = sql_alchemy_models.SQL_Alchemy_Declarative_Base_Post_Extended(**new_pydantic_post.dict())
    return new_sql_alchemy_user # returns to api

@router.get('/{id}', response_model=pydantic_FE_req_res_payload.FE_Res_Create_User_Payload)
def get_user(id:int, db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):
    sql_alchemy_table= db.query(sql_alchemy_tables.SQL_Alchemy_Postgres_User_Table)
    sql_alchemy_query_1 = sql_alchemy_table.filter(sql_alchemy_tables.SQL_Alchemy_Postgres_User_Table.sql_alchemy_user_id == id)
    sql_alchemy_query_2 = sql_alchemy_query_1.first()


    if not sql_alchemy_query_2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id: {id} does not exist")
    return sql_alchemy_query_2