import sched
from urllib import response
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from typing import List

from fastapi.middleware.cors import CORSMiddleware


from .routers import posts, users, auth, vote
from .config import local_env_var

from sqlalchemy.orm import Session
from . import sql_alchemy_tables # to access model.py attribures/functions; syntax: models.sql_alchemy_declarative_base
from . import pydantic_FE_req_res_payload

from . import sql_alchemy_postgres_connect
from . import psycopg2_postgres_connect
from . import utils
# ###
from .env import my_host, my_database, my_user, my_pass
from .constants import my_request, find_post, find_post_index




### Creates tables from sql_alchemy engine (if not already created)
sql_alchemy_tables.sql_alchemy_table_engine.metadata.create_all(bind=sql_alchemy_postgres_connect.sql_alchemy_database_engine)
###
### Connect to Postgres DB using psycopg2 (raw sql)
pydantic_psycopg_conn, pydantic_psycopg_cursor = psycopg2_postgres_connect.start_psycopg2_postgres_connection()
###

FastAPI_app = FastAPI()

# FRONT END DOMAIN that can hit our API on my server 127.0.0.1
origins = ["https://www.google.com", "https://www.youtube.com"]
origins = ["*"]
# middleware is a function that runs before any request
FastAPI_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # only specific domains can access FastAPI_app
    allow_credentials=True,
    allow_methods=["*"], # only specific http methods can access FastAPI_app
    allow_headers=["*"], # only specific headers methods can access FastAPI_app
)

# @FastAPI_app.get("/")
# async def main():
#     return {"message": "Hello World"}


FastAPI_app.include_router(posts.router)
FastAPI_app.include_router(users.router)
FastAPI_app.include_router(auth.router)
FastAPI_app.include_router(vote.router)
  
