from re import A
from socketserver import StreamRequestHandler
from sys import prefix

from FastAPI_app import oauth2
from .. import sql_alchemy_postgres_connect
from .. import psycopg2_postgres_connect
from .. import utils
from typing import List, Optional

from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import sql_alchemy_tables # to access model.py attribures/functions; syntax: models.sql_alchemy_declarative_base
from .. import pydantic_FE_req_res_payload
from .. import oauth2


router = APIRouter(
    prefix="/posts",
    tags=['Posts'] # for swagger ui
)




@router.get("/", response_model=List[pydantic_FE_req_res_payload.FE_Res_Post_Payload_V2])

def get_posts(db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session), limit:int = 1, skip:int = 0, search:Optional[str] = ""):# default limit is 1, can set it using query parameters
    
    # RESPONSE_MODEL = SELECT COLUMNS
    
    # FROM TABLE
    sql_alchemy_table = db.query(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table) 
    # WHERE = SELECT ROWS
    sql_alchemy_query_1 = sql_alchemy_table.filter(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table.sql_alchemy_title.contains(search))
    # LIMIT
    sql_alchemy_query_2 = sql_alchemy_query_1.limit(limit)
    # OFFSET
    sql_alchemy_query_3 = sql_alchemy_query_2.offset(skip)
    # RETURN
    sql_alchemy_return =sql_alchemy_query_3.all()

    # FROM TABLE
    sql_alchemy_table_1 = db.query(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table, func.count(sql_alchemy_tables.SQL_Alchemy_Postgres_Votes_Table.sql_alchemy_liked_post_id).label("votes"))
    # LEFT OUTER JOIN ON
    sql_alchemy_query_1_1 = sql_alchemy_table_1.join(sql_alchemy_tables.SQL_Alchemy_Postgres_Votes_Table, sql_alchemy_tables.SQL_Alchemy_Postgres_Votes_Table.sql_alchemy_liked_post_id == sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table.sql_alchemy_id, isouter=True )
    # GROUP BY
    sql_alchemy_query_1_2 = sql_alchemy_query_1_1.group_by(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table.sql_alchemy_id)
    
    print(sql_alchemy_query_1_2)
    sql_alchemy_return_1 = sql_alchemy_query_1_2.all()
 
    ###
    return sql_alchemy_return_1 # list items, need to put list in response model



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=pydantic_FE_req_res_payload.FE_Res_Post_Payload)

def createposts(FE_req_post_payload_1:pydantic_FE_req_res_payload.FE_Req_Post_Payload, db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)): #, user_id:int = Depends(oauth2.get_current_user)    
    
    # RESPONSE_MODEL = SELECT COLUMNS

    # INSERT INTO  and VALUES
    sql_alchemy_insert_into_values = sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table(sql_alchemy_title = FE_req_post_payload_1.FE_request_title, sql_alchemy_content = FE_req_post_payload_1.FE_request_content, sql_alchemy_published = FE_req_post_payload_1.FE_request_published)
    print(sql_alchemy_insert_into_values)

    # MODIFICATION COMMIT
    db.add(sql_alchemy_insert_into_values) # not posting a dictionary, but a sql_alchemy_post post
    db.commit()
    db.refresh(sql_alchemy_insert_into_values)

    return sql_alchemy_insert_into_values # non list items, dont need to put list in response model


@router.get("/{id}", response_model=pydantic_FE_req_res_payload.FE_Res_Post_Payload) # id is path parameter inputted by user

def get_post(id:int, db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):

    # RESPONSE_MODEL = SELECT COLUMNS

    # FROM TABLE
    sql_alchemy_table = db.query(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table)
    # WHERE = SELECT ROWS
    sql_alchemy_query_1 = sql_alchemy_table.filter(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table.sql_alchemy_id == id)
    # RETURN
    sql_return = sql_alchemy_query_1.first()
    print(sql_return)

    return sql_return


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):

    # RESPONSE_MODEL = SELECT COLUMNS

    # FROM TABLE
    sql_alchemy_table = db.query(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table)
    # WHERE = SELECT ROWS
    sql_alchemy_query_1 = sql_alchemy_table.filter(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table.sql_alchemy_id == id)
    # DELETE
    sql_alchemy_query_1.delete(synchronize_session=False)

    # MODIFICATION COMMIT
    db.commit()


    
    return sql_alchemy_query_1


@router.put("/{id}", response_model=pydantic_FE_req_res_payload.FE_Res_Post_Payload)
def put_update_post(id:int, FE_req_post_payload_1:pydantic_FE_req_res_payload.FE_Req_Post_Payload, db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):

    sql_alchemy_table = db.query(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table)
    sql_alchemy_query_1 = sql_alchemy_table.filter(sql_alchemy_tables.SQL_Alchemy_Postgres_Posts_Table.sql_alchemy_id == id)
    
    updated_pydantic_post_val_list = list(FE_req_post_payload_1.dict().values())
    print('-1')
    sql_alchemy_query_1.update({"sql_alchemy_title": updated_pydantic_post_val_list[0], "sql_alchemy_content":updated_pydantic_post_val_list[1], "sql_alchemy_published":updated_pydantic_post_val_list[2]}, synchronize_session=False)
    db.commit()

    print(sql_alchemy_query_1.first())
    return sql_alchemy_query_1.first()