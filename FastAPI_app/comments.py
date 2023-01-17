#main.py




### from -> import : declares the variable name to be used already
# from . import database
# engine = database.engine
# get_db = database.get_db




@FastAPI_app.get("/") 
# function1(function2)
# function1 = FastAPI_app.get("/") 
# function2 = root


# @FastAPI_app.get("/sqlalchemy")
# def test_posts(db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db)): # db.type:Session; Session is sqlalchemy.ORM; get_db: Call SQL query engine session using yield function
#     sql_alchemy_query = db.query(sql_alchemy_models.SQL_Alchemy_Declarative_Base_Post_Extended) # from models.py get Post class; get all results of the class
#     print(sql_alchemy_query)
#     query_results = sql_alchemy_query.all()
#     return {"data": query_results}


async def root(): # async only needed if performing an asynchoronous task, optional
    return {"message" : "Hello World"}

# root = FastAPI_app.get("/")(original_function = root)
# root.type = wrFastAPI_apper(*args, ** kwargs)
# root() # wrFastAPI_apper() : return original_function() -> return {"message" : "Hello World"}



# @FastAPI_app.post("/createposts")
# def createposts(varname:dict = Body(...)): # dict type var
#     print(type(varname))
#     print(varname) # in this terminal
#     return {"new_post"} # returns to api

# createposts = FastAPI_app.post("/")(original_function = createposts)
# createposts.type = wrFastAPI_apper(*args, ** kwargs)
# createposts() # wrFastAPI_apper(varname = Body(...)) : return original_function() -> return {"message" : "Hello World"}


# @FastAPI_app.post("/createposts_BaseModel")
# def createposts(new_post:pydantic_models.Pydantic_BaseModel_Post_Extended): # post type var
#     print(type(new_post))
#     print(new_post) # in this terminal
#     print(new_post.dict())
#     return {"new_post_BaseModel"} # returns to api





    # my_posts[updated_post] = updated_post_dict





PYDANTIC POST TABLE ROUTER


@router.get("/", response_model=List[pydantic_FE_req_res_payload.FE_Res_Post_Payload])
    ### with pydantic
# def get_posts():
    # pydantic_cursor.execute("""select * from posts""") # cursor.execute is SQL command
    # my_posts = pydantic_cursor.fetchall()
    # print(my_posts)
    ###

    ### with sqlalchemy



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=pydantic_FE_req_res_payload.FE_Res_Post_Payload)
### with pydantic
# def createposts(new_post:pydantic_models.Pydantic_BaseModel_Post_Extended): # post type var
#     pydantic_cursor.execute("""insert into posts (title, content, published) values (%s, %s, %s) returning *""", (new_post.title, new_post.content, new_post.published))
#     new_post = pydantic_cursor.fetchone()
#     pydantic_conn.commit()
#     # print(type(new_post))
#     # print(new_post) # in this terminal
#     # print(new_post.dict())
#     # new_post_dict = new_post.dict()
#     # new_post_dict['id'] = randrange(0, 99999)
#     # my_posts.FastAPI_append(new_post_dict)




@router.get("/{id}", response_model=pydantic_FE_req_res_payload.FE_Res_Post_Payload) # id is path parameter inputted by user
def get_post(id:int, db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):


    # pydantic_cursor.execute("""select * from posts where id =%s""", (str(id)))
    # post_requested = pydantic_cursor.fetchone()
    # # print(id)
    # # post_requested = find_post(id)
    # if not post_requested:
    #     # response.status_code  = status.HTTP_404_NOT_FOUND
    #     # return {'message': 'post not found'}
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int, db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):
    # pydantic_cursor.execute("""delete from posts where id = %s returning *""", (str(id)))
    # deleted_post = pydantic_cursor.fetchone()
    # pydantic_conn.commit()

    # # post_index_requested = find_post_index(id)
    # if deleted_post == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with {id} does not exist')
    # my_posts.pop(deleted_post)
        # db.refresh(sql_alchemy_query_filter)



@router.put("/{id}", response_model=pydantic_FE_req_res_payload.FE_Res_Post_Payload)
def put_update_post(id:int, FE_req_post_payload_1:pydantic_FE_req_res_payload.FE_Req_Post_Payload, db:Session = Depends(sql_alchemy_postgres_connect.get_sql_alchemy_db_session)):
    # pydantic_cursor.execute("""update posts set title = %s, content = %s, published = %s where id = %s returning *""", (updated_post.pydantic_title, updated_post.pydantic_content, updated_post.pydantic_published, str(id)))
    # updated_post = pydantic_cursor.fetchone()
    # pydantic_conn.commit()
    # # updated_post_dict = updated_post.dict()
    # # updated_post_dict['id'] = id

    # # updated_post = find_post_index(id)
    # if updated_post == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with {id} does not exist')
    # return {"data": updated_post}

        # print(list(updated_pydantic_post.dict().values()))
    
    # sql_alchemy_query_filter.update(updated_post.dict(), synchronize_session=False)
    # db.commit()
    # updated_sql_alchemy_post = sql_alchemy_models.SQL_Alchemy_Declarative_Base_Post_Extended(sql_alchemy_title = updated_pydantic_post.pydantic_title, sql_alchemy_content = updated_pydantic_post.pydantic_content, sql_alchemy_published = updated_pydantic_post.pydantic_published)

    # sql_alchemy_query_result = sql_alchemy_query_filter.first()