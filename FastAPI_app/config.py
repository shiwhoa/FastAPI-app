from pydantic import BaseSettings

class Local_Env_Variables(BaseSettings):
    db_hostname:str
    db_port:str
    db_username:str = 'postgres' # this is default if environment variables dont have 'postgres_password' key
    db_password:str = '7875612' # this is default if environment variables dont have 'postgres_username' key
    db_name:str
    secret_key:str
    algorithm:str
    access_token_expiry:int

    # gets above from ".env" file
    class Config:
        env_file=".env"

local_env_var = Local_Env_Variables()
local_env_var.db_password
