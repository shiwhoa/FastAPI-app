from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import pydantic_FE_req_res_payload, sql_alchemy_tables,sql_alchemy_postgres_connect, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(FE_req_payload:pydantic_FE_req_res_payload.FE_Req_Vote_Payload, db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):
    sql_alchemy_table = db.query(sql_alchemy_tables.SQL_Alchemy_Postgres_Votes_Table)
    sql_alchemy_query_1 = sql_alchemy_table.filter(sql_alchemy_tables.SQL_Alchemy_Postgres_Votes_Table.sql_alchemy_liked_post_id == FE_req_payload.FE_request_liked_post_id,
    sql_alchemy_tables.SQL_Alchemy_Postgres_Votes_Table.sql_alchemy_liked_by_user_id == FE_req_payload.FE_request_liked_by_user_id)
    sql_alchemy_query_2 = sql_alchemy_query_1.first()
    
    if (FE_req_payload.dir == 1):
        if sql_alchemy_query_2:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user already voted on this post")
        
        new_vote = sql_alchemy_tables.SQL_Alchemy_Postgres_Votes_Table(sql_alchemy_liked_post_id = FE_req_payload.FE_request_liked_post_id, sql_alchemy_liked_by_user_id = FE_req_payload.FE_request_liked_by_user_id)
        db.add(new_vote)
        db.commit()
        return 'success voted'

    elif (FE_req_payload.dir == 0):
        if sql_alchemy_query_2:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"vote does not exist")
        
        sql_alchemy_query_1.delete(synchronize_session=False)
        db.commit()

        return 'success delete'
    
    else:
        pass