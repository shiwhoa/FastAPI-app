from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
from pydantic.types import conint


pydantic_base = BaseModel

# GET does not have payload

class FE_Req_Post_Payload(pydantic_base): # Post extends type:pydantic BaseModel
    FE_request_title:str # creates Post.title attribute
    FE_request_content:str # creates Post.content attribute
    FE_request_published:bool = True # default value is True if value does not exist

    FE_request_rating:Optional[int] = None # default value is None if value does not exist; if exists IT MUST BE INTEGER OR ERROR

# class Request_(Pydantic_BaseModel_Post_Extended):
#     pass

class FE_Req_Update_Payload(FE_Req_Post_Payload):
    pass




class FE_Res_Create_User_Payload(pydantic_base):
    sql_alchemy_user_id:int
    sql_alchemy_user_email:EmailStr
    # sql_alchemy_user_password:str
    class Config:
        orm_mode = True




class FE_Res_Post_Payload(pydantic_base):
    sql_alchemy_title:str # creates Post.title attribute
    sql_alchemy_content:str # creates Post.content attribute
    sql_alchemy_user_id:int
    sql_alchemy_user: FE_Res_Create_User_Payload
    class Config:
        orm_mode = True
    # FE_response_published:bool = True # default value is True if value does not exist

    # FE_response_rating:Optional[int] = None # default value is None if value does not exist; if exists IT MUST BE INTEGER OR ERROR

class FE_Res_Post_Payload_V2(pydantic_base):
    SQL_Alchemy_Postgres_Posts_Table:FE_Res_Post_Payload
    votes:int
    class Config:
        orm_mode = True















class FE_Req_Create_User_Payload(pydantic_base):
    FE_request_user_email:EmailStr
    FE_resquest_user_password:str

class FE_Req_Create_User_Login_Payload(pydantic_base):
    FE_request_user_login_email:EmailStr
    FE_request_user_login_password:str




class FE_Res_Create_User_Login_Payload(pydantic_base):
    # sql_alchemy_user_id:int
    sql_alchemy_user_email:EmailStr
    # sql_alchemy_user_password:str
    class Config:
        orm_mode = True


class FE_Req_Token(pydantic_base):
    FE_request_access_token:str
    FE_request_token_type:str

class FE_Req_Token_data(pydantic_base):
    FE_request_id:Optional[str] = None



class FE_Req_Vote_Payload(pydantic_base):
    FE_request_liked_post_id:int
    FE_request_liked_by_user_id:int
    dir:conint(le=1)